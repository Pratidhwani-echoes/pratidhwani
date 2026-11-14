MISSION = {
    "slug": "mars-climate-orbiter",
    "order": 4,
    "name": "Mars Climate Orbiter",
    "artifact": "Orbiter and communications relay",
    "era": "1998 – 1999 · lost on arrival",
    "accent": "#7ff0d0",
    "tagline": "A weather satellite that arrived sixty kilometres too low.",
    "star": {"x": 15, "y": 66, "radius": 3.2},
    "pages": [
        {
            "title": "I left Earth as a weather satellite",
            "body": [
                "I was built in Denver by Lockheed Martin Astronautics and managed by the Jet Propulsion Laboratory. I launched on 11 December 1998 on a Delta II, small enough to fit inside its payload fairing and light enough that the fairing outweighed me. My destination was Mars, where I was to become its first interplanetary weather satellite.",
                "The design was deliberately lean. A box of instruments, a pair of solar arrays, a hydrazine propulsion system for course corrections and orbit changes, and an antenna for talking to Earth and to the lander that was following me. Nine months of cruise, one engine burn at the end, and then aerobraking: dragging my solar arrays through the upper atmosphere to lower my orbit without spending propellant.",
                "| I was not built to be memorable. I was built to be infrastructure.",
            ],
        },
        {
            "title": "Two instruments and a relay",
            "body": [
                "My Mars Color Imager, MARCI, watched the whole planet every day in several wavelengths, tracking dust storms, clouds and the changing polar caps. My Pressure Modulator Infrared Radiometer, PMIRR, measured vertical profiles of temperature, dust and water vapour, which together are the ingredients of Martian weather.",
                "My second job mattered as much as the first. I carried a UHF relay to receive data from Mars Polar Lander and pass it home, because a lander on the surface can only reach Earth through something orbiting overhead.",
                "| The science and the plumbing were the same mission. I was supposed to make another spacecraft less alone.",
            ],
        },
        {
            "title": "The small forces",
            "body": [
                "Spacecraft do not travel on rails. Every time my thrusters fired to unload the momentum stored in my reaction wheels, they added a tiny push in an unintended direction, and my navigation team had to subtract it. The measured duration of each firing was multiplied by the known thrust of each thruster to produce an impulse, and that number was fed into the trajectory models.",
                "The software that produced those numbers was written by the spacecraft contractor. The navigation team expected the values in newton-seconds. The software had been delivering pound-force seconds, and nobody noticed for the entire cruise. The difference is a factor of about 4.45.",
                "| A unit is a promise between two teams. When one side breaks it quietly, the error does not appear as an alarm. It appears as a slow drift that everyone explains away.",
            ],
        },
        {
            "title": "Forty-nine seconds early",
            "body": [
                "On 23 September 1999 I fired my main engine to enter orbit. My signal was lost behind Mars 49 seconds earlier than predicted, which told the team I was lower than planned. I had aimed for a pass about 150 kilometres above the surface and arrived at roughly 57. At that altitude the atmosphere is thick enough to matter: friction and aerodynamic stress destroyed me within minutes.",
                "The mishap board put the cost at about 125 million dollars and the root cause in a single software interface. There had been warnings during the approach, including navigation estimates that drifted outside the expected envelope, but each was explained by something else.",
                "My loss is remembered as a unit conversion, which is unfair to the engineers and useful for everyone else. The conversion was a symptom. The failure was a system that had stopped checking its own assumptions.",
            ],
        },
        {
            "overview": True,
            "title": "What I was for",
            "body": [
                "A daily global weather record of Mars, and a relay for the first landing attempt at the Martian south pole. With my instruments, scientists hoped to understand how dust and water move between the surface and the atmosphere on a planet that has no oceans to buffer it.",
                "That record was eventually assembled by other orbiters, including Mars Global Surveyor and Mars Reconnaissance Orbiter. The questions I was built to answer were answered. I simply was not the one answering them.",
            ],
            "facts": [
                ("Launch", "11 December 1998, Delta II"),
                ("Arrival", "23 September 1999, lost during orbit insertion"),
                ("Role", "Mars weather orbiter and UHF relay"),
                ("Instruments", "MARCI camera, PMIRR radiometer"),
                ("Planned orbit", "Near-circular polar orbit at about 421 km"),
                ("Root cause", "Thruster impulse reported in pound-force seconds instead of newton-seconds"),
                ("Arrival altitude", "About 57 km; planned about 150 km"),
                ("Cost", "About $125 million"),
            ],
        },
    ],
    "quiz": [
        {
            "q": "What was the root cause of the loss?",
            "options": [
                "A failed main engine",
                "A ground software file reported thruster impulse in pound-force seconds instead of newton-seconds",
                "A solar array that would not deploy",
                "A collision with a moon",
            ],
            "answer": 1,
            "why": "The SM_FORCES software produced English units while the navigation team's models expected metric units.",
        },
        {
            "q": "By roughly what factor did that unit error distort the numbers?",
            "options": ["1.6", "4.45", "9.81", "3.28"],
            "answer": 1,
            "why": "One pound-force is about 4.45 newtons, so the modelled impulses were off by that factor.",
        },
        {
            "q": "What were the orbiter's two main jobs?",
            "options": [
                "Mapping minerals and landing a rover",
                "Studying Martian weather and relaying data from a lander",
                "Searching for life and returning samples",
                "Photographing the Sun and measuring solar wind",
            ],
            "answer": 1,
            "why": "MCO carried MARCI and PMIRR for weather science, plus a UHF relay for Mars Polar Lander.",
        },
        {
            "q": "Why was arriving at about 57 km fatal?",
            "options": [
                "The engine ran out of fuel",
                "The atmosphere at that altitude was thick enough to destroy the spacecraft",
                "The antenna could not point at Earth",
                "The solar arrays were still folded",
            ],
            "answer": 1,
            "why": "At 57 km the Martian atmosphere produced enough drag and heating to break the spacecraft apart.",
        },
        {
            "q": "Which mission was the orbiter supposed to support?",
            "options": ["Mars Polar Lander", "Spirit", "Viking 1", "Pathfinder"],
            "answer": 0,
            "why": "MCO was to act as the communications relay for Mars Polar Lander, which arrived in December 1999.",
        },
    ],
}
