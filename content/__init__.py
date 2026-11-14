"""Artifact registry.

Adding an artifact is three steps and no template edits:

1. Copy any file in ``content/missions/`` and rename it.
2. Give the new ``MISSION`` dict a unique ``slug`` and ``order`` and place its
   star with ``star: {"x": 0-100, "y": 0-100}``.
3. Write four story pages plus one overview page, and exactly five questions.

The constellation, star links, progress count, quiz route, and reset button all
pick the new module up automatically.
"""

from importlib import import_module
from pathlib import Path

STAR_W = 1000
STAR_H = 600

REQUIRED_KEYS = (
    "slug",
    "name",
    "artifact",
    "era",
    "accent",
    "tagline",
    "order",
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
        if not 0 <= question["answer"] < len(question["options"]):
            raise ValueError(f"{filename}: question {index} has an answer index out of range")

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

    loaded.sort(key=lambda item: item["order"])
    slugs = [item["slug"] for item in loaded]
    if len(slugs) != len(set(slugs)):
        raise ValueError("two missions share the same slug")
    return loaded


MISSIONS = _load()
MISSIONS_BY_SLUG = {mission["slug"]: mission for mission in MISSIONS}


def build_sky(completed):
    """Project the mission registry onto constellation coordinates.

    Stars are chained in ``order``, so a new artifact simply extends the line
    without anyone editing SVG by hand.
    """
    completed = set(completed)
    stars = []
    for mission in MISSIONS:
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
                "delay": f"{(mission['order'] % 5) * 0.7:.1f}",
            }
        )

    links = []
    for first, second in zip(stars, stars[1:]):
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
