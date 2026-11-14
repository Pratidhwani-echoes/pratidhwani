"""Pratidhwani - a small museum for missions that never launched.

Progress lives in Flask's signed session cookie, every page is rendered by
Jinja, and the quiz is graded on the server. JavaScript is used only for the
mouse parallax of the starfield.
"""

import os
import random
from pathlib import Path

from flask import Flask, abort, redirect, render_template, request, session, url_for

from content import MISSIONS, MISSIONS_BY_SLUG, build_sky

BASE_DIR = Path(__file__).resolve().parent
MASCOT_FILE = BASE_DIR / "static" / "img" / "ananta-wave.webp"

# Four of five correct answers lights the star.
PASS_MARK = 4

COMPANION = {
    "welcome": (
        "I'm Ananta. I keep the quiet part of the sky - the missions that were "
        "finished, tested, and then never flown. Pick a star and I'll let the "
        "hardware do the talking."
    ),
    "story": [
        "Read it slowly. These machines were built by people who expected them to fly.",
        "Every number here was paid for twice: once in money, once in years.",
        "This is the part I find hardest to explain to visitors.",
        "Nearly there. The last page is where the facts live.",
        "That's the whole story. Ready for five questions?",
    ],
    "quiz": "No pressure. Four right and this star joins the sky.",
    "pass": "You did it! Look up - your star is lit.",
    "fail": "That was close. Walk back through the story and try again; the star will wait.",
    "complete": "All six are lit! This is what the sky would have looked like if they had flown.",
}

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "unfinished-constellation-dev-key"),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)


def completed_slugs():
    """Completed missions, filtered against the registry and kept in story order."""
    stored = session.get("completed", [])
    known = set(stored)
    return [mission["slug"] for mission in MISSIONS if mission["slug"] in known]


def completed_count():
    return len(completed_slugs())


@app.context_processor
def shared_context():
    return {
        "missions": MISSIONS,
        "missions_by_slug": MISSIONS_BY_SLUG,
        "mascot_ready": MASCOT_FILE.exists(),
        "companion": COMPANION,
        "pass_mark": PASS_MARK,
        "sky_dots": SKY_DOTS,
        "completed_total": completed_count(),
        "mission_total": len(MISSIONS),
    }


def _starfield(seed=11, count=110):
    """The parallax starfield is generated in Python, not painted by JavaScript."""
    rng = random.Random(seed)
    dots = []
    for _ in range(count):
        layer = rng.choice((1, 1, 2, 2, 3))
        dots.append(
            {
                "x": round(rng.uniform(0, 100), 2),
                "y": round(rng.uniform(0, 100), 2),
                "size": rng.choice((1, 1, 1, 2, 2, 3)) if layer > 1 else rng.choice((1, 2)),
                "delay": round(rng.uniform(0, 8), 2),
                "duration": round(rng.uniform(3.5, 9), 2),
                "opacity": round(rng.uniform(0.18, 0.8), 2),
                "layer": layer,
            }
        )
    return dots


SKY_DOTS = _starfield()


def get_mission(slug):
    mission = MISSIONS_BY_SLUG.get(slug)
    if mission is None:
        abort(404)
    return mission


@app.get("/")
def landing():
    done = completed_slugs()
    newcomer = request.args.get("new")
    if newcomer not in MISSIONS_BY_SLUG or newcomer not in done:
        newcomer = None
    return render_template(
        "landing.html",
        sky=build_sky(done),
        done=done,
        met=session.get("met", False),
        newcomer=newcomer,
        all_done=len(done) == len(MISSIONS) and bool(MISSIONS),
    )


@app.post("/begin")
def begin():
    session["met"] = True
    return redirect(url_for("landing"))


@app.post("/reset")
def reset():
    session.clear()
    return redirect(url_for("landing"))


@app.get("/artifact/<slug>/")
def artifact_start(slug):
    get_mission(slug)
    return redirect(url_for("artifact_page", slug=slug, page_number=1))


@app.get("/artifact/<slug>/page/<int:page_number>")
def artifact_page(slug, page_number):
    mission = get_mission(slug)
    pages = mission["pages"]
    if page_number < 1:
        return redirect(url_for("artifact_page", slug=slug, page_number=1))
    if page_number > len(pages):
        return redirect(url_for("artifact_quiz", slug=slug))

    page = pages[page_number - 1]
    lines = COMPANION["story"]
    return render_template(
        "story.html",
        mission=mission,
        page=page,
        number=page_number,
        total=len(pages),
        is_last=page_number == len(pages),
        completed=slug in completed_slugs(),
        companion_line=lines[(page_number - 1) % len(lines)],
    )


@app.get("/artifact/<slug>/quiz")
def artifact_quiz(slug):
    mission = get_mission(slug)
    return render_template(
        "quiz.html",
        mission=mission,
        completed=slug in completed_slugs(),
    )


@app.post("/artifact/<slug>/quiz")
def artifact_quiz_submit(slug):
    mission = get_mission(slug)
    was_completed = slug in completed_slugs()
    results = []
    score = 0

    for index, question in enumerate(mission["quiz"]):
        raw = request.form.get(f"q{index}", "")
        try:
            picked = int(raw)
        except (TypeError, ValueError):
            picked = None
        correct = picked == question["answer"]
        score += 1 if correct else 0
        results.append(
            {
                "question": question["q"],
                "options": question["options"],
                "picked": picked,
                "answer": question["answer"],
                "correct": correct,
                "why": question["why"],
            }
        )

    passed = score >= PASS_MARK
    if passed and not was_completed:
        session["completed"] = completed_slugs() + [slug]
        session.modified = True

    return render_template(
        "result.html",
        mission=mission,
        score=score,
        total=len(mission["quiz"]),
        passed=passed,
        was_completed=was_completed,
        newly_added=passed and not was_completed,
        results=results,
        celebrate=(url_for("landing", new=slug) if passed and not was_completed else url_for("landing")),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)), debug=True)
