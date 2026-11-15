"""Artifact registry.

Adding an artifact is three steps and no template edits:

1. Copy any file in ``content/missions/`` and rename it.
2. Give the new ``MISSION`` dict a unique ``slug`` and place its star with
   ``star: {"x": 0-100, "y": 0-100}``.
3. Write four story pages plus one overview page, and exactly five questions.
   Quiz answer keys are 1-based option numbers.

Star positions, progress count, quiz routes, and reset behavior pick new modules
up automatically. Configure constellation connections in ``STAR_LINKS`` below.
"""

from importlib import import_module
from pathlib import Path

STAR_W = 1000
STAR_H = 600

# Add pairs of mission slugs to draw constellation links; leave empty for none.
STAR_LINKS = (
    ("apollo-10", "dawn"),
    ("apollo-10", "voyager-1"),
    ("voyager-2", "voyager-1"),
    ("isee-3", "voyager-2"),
    ("isee-3", "surveyor-3"),
    ("pioneer-10", "surveyor-3"),
    ("isee-3", "dawn"),
    ("apollo-12", "voyager-1"),
    ("apollo-12", "surveyor-3"),
)

REQUIRED_KEYS = (
    "slug",
    "name",
    "artifact",
    "era",
    "accent",
    "tagline",
    "star",
    "pages",
    "quiz",
)


def _validate(mission, filename):
    missing = [key for key in REQUIRED_KEYS if key not in mission]
    if missing:
        raise ValueError(f"{filename}: MISSION is missing {', '.join(missing)}")

    if len(mission["quiz"]) != 5:
        raise ValueError(f"{filename}: a quiz needs exactly five questions")

    for index, question in enumerate(mission["quiz"], start=1):
        if not 1 <= question["answer"] <= len(question["options"]):
            raise ValueError(f"{filename}: question {index} answer must be a 1-based option number")

    if not mission["pages"] or not mission["pages"][-1].get("overview"):
        raise ValueError(f"{filename}: the last page must be the overview page")

    for axis in ("x", "y"):
        if not 0 <= mission["star"][axis] <= 100:
            raise ValueError(f"{filename}: star {axis} must be a percentage between 0 and 100")


def _load():
    folder = Path(__file__).with_name("missions")
    loaded = []
    for path in sorted(folder.glob("*.py")):
        if path.name.startswith("_"):
            continue
        mission = import_module(f"{__name__}.missions.{path.stem}").MISSION
        _validate(mission, path.name)
        loaded.append(mission)

    slugs = [item["slug"] for item in loaded]
    if len(slugs) != len(set(slugs)):
        raise ValueError("two missions share the same slug")
    return loaded


MISSIONS = _load()
MISSIONS_BY_SLUG = {mission["slug"]: mission for mission in MISSIONS}


def build_sky(completed):
    """Project the mission registry and configured links onto sky coordinates."""
    completed = set(completed)
    stars = []
    for index, mission in enumerate(MISSIONS):
        position = mission["star"]
        stars.append(
            {
                "slug": mission["slug"],
                "name": mission["name"],
                "artifact": mission["artifact"],
                "x": round(position["x"] * STAR_W / 100, 1),
                "y": round(position["y"] * STAR_H / 100, 1),
                "r": position.get("radius", 3.4),
                "accent": mission["accent"],
                "done": mission["slug"] in completed,
                "delay": f"{(index % 5) * 0.7:.1f}",
            }
        )

    links = []
    stars_by_slug = {star["slug"]: star for star in stars}
    for first_slug, second_slug in STAR_LINKS:
        if first_slug not in stars_by_slug or second_slug not in stars_by_slug:
            raise ValueError(f"unknown mission slug in STAR_LINKS: {first_slug!r}, {second_slug!r}")
        if first_slug == second_slug:
            raise ValueError(f"STAR_LINKS cannot connect a star to itself: {first_slug!r}")

        first = stars_by_slug[first_slug]
        second = stars_by_slug[second_slug]
        links.append(
            {
                "x1": first["x"],
                "y1": first["y"],
                "x2": second["x"],
                "y2": second["y"],
                "lit": first["done"] and second["done"],
            }
        )

    return {
        "stars": stars,
        "links": links,
        "total": len(stars),
        "done_count": sum(1 for star in stars if star["done"]),
        "percent": round(100 * sum(1 for star in stars if star["done"]) / len(stars)) if stars else 0,
        "all_done": bool(stars) and all(star["done"] for star in stars),
    }
