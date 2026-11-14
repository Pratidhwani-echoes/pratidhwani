MISSION = {
    "slug": "mars-polar-lander",
    "order": 5,
    "name": "Mars Polar Lander",
    "artifact": "South polar lander and Deep Space 2",
    "era": "1999 · lost during descent",
    "accent": "#ff9aa8",
    "tagline": "A lander sent to read the climate record written in polar ice.",
    "star": {"x": 85, "y": 62, "radius": 3.2},
    "pages": [
        {
            "title": "South, where the ice is",
            "body": [
                "I launched on 3 January 1999, a few weeks after Mars Climate Orbiter, and I was aimed further south than anything had gone before: about 76 degrees south, on the layered plains at the edge of the Martian polar cap. No spacecraft had landed in a polar region of Mars. I was built to be the first.",
                "My descent was designed to be fast and autonomous. A heat shield, a parachute, then legs out, radar to find the ground, backshell away, and a set of throttleable hydrazine engines to bring me down the last kilometre. Five and a half minutes from the top of the atmosphere to the surface, with no human in the loop.",
                "| I had one chance and no way to describe it afterwards. My transmitter was switched off during entry, as planned. Whatever happened, happened in silence.",
            ],
        },
        {
            "title": "The payload",
            "body": [
                "My main instrument package was MVACS: a stereo surface imager, a two-metre robotic arm with a camera on its wrist, a meteorology mast with wind and temperature sensors, and a thermal analyser designed to bake small samples of soil and identify the gases released. A descent camera, MARDI, would have photographed the landing site on the way down. A Russian LIDAR measured dust and clouds above me, and a small microphone from the Planetary Society would have recorded the wind.",
                "I also carried two Deep Space 2 microprobes, each about the size of a basketball. They were designed to be released during descent, hit the surface at speed, and drive a small penetrator into the ground to test for water ice.",
                "| Between us we would have measured the air, the soil, the ice and the sound of an alien planet in the same season.",
            ],
        },
        {
            "title": "Layered time",
            "body": [
                "The south polar layered deposits are a stack of ice and dust, built up and eroded over millions of years. Each layer is a page: a change in the tilt of Mars, a change in its orbit, a period when the atmosphere was thicker or thinner. Reading the layers is one way to reconstruct a climate history that no weather station was present to record.",
                "Landing in southern summer meant permanent daylight and relatively mild conditions, but it also meant the seasonal carbon dioxide frost was retreating. Understanding where the frost goes, and how water vapour moves between the cap and the atmosphere, was central to the mission.",
                "| I was sent to the place where Mars keeps its memory, to see whether it is written in water.",
            ],
        },
        {
            "title": "3 December 1999",
            "body": [
                "I entered the atmosphere on schedule. My carrier signal stopped as planned. It never came back. Orbiting spacecraft listened for me, Mars Global Surveyor tried to relay, and the team sent commands for weeks. Nothing answered, and the two Deep Space 2 probes were never heard either.",
                "The review board had no telemetry to work with, only the design. It concluded that the most probable cause was a false touchdown indication during my descent: my landing legs generated a brief electrical transient as they locked into place, my software treated it as contact with the ground, and my engines shut down about 40 metres up. I fell the rest of the way at roughly 50 miles per hour.",
                "The fix would have been a filter in the flight software, a few lines long. The board noted that the transient was known from testing and had never been fully accounted for. Nine years later Phoenix landed successfully in the same polar region, using hardware and lessons that came partly from me.",
            ],
        },
        {
            "overview": True,
            "title": "What I was for",
            "body": [
                "I was the first mission designed to land in a Martian polar region and study the volatile history of the south pole directly. With MVACS, MARDI, LIDAR and the Deep Space 2 probes, I would have sampled soil, measured the weather, photographed the descent and tested for subsurface ice in a single season.",
                "Phoenix eventually answered several of my questions near the north pole, and orbiters mapped the layers I was meant to touch. The layered deposits remain one of the best climate archives in the solar system — and one of the hardest places to land.",
            ],
            "facts": [
                ("Launch", "3 January 1999, Delta II"),
                ("Arrival", "3 December 1999, lost during entry, descent and landing"),
                ("Landing site", "About 76 degrees south, Planum Australe"),
                ("Payload", "MVACS, MARDI descent camera, LIDAR, microphone"),
                ("Hitchhikers", "Two Deep Space 2 microprobes"),
                ("Descent", "About 5.5 minutes, fully autonomous"),
                ("Probable cause", "False touchdown signal shut down the engines about 40 m above the surface"),
                ("Cost", "About $165 million"),
                ("Legacy", "Phoenix landed in the same region in 2008"),
            ],
        },
    ],
    "quiz": [
        {
            "q": "What was Mars Polar Lander sent to study?",
            "options": [
                "The south polar layered deposits and the history of water and dust",
                "The Martian moons",
                "The planet's magnetic field",
                "The solar wind",
            ],
            "answer": 0,
            "why": "The mission targeted the layered terrain near the south pole, a record of past climate and volatiles.",
        },
        {
            "q": "Which two small probes rode along with the lander?",
            "options": ["Viking 3 and 4", "Deep Space 2", "Sojourner and Pathfinder", "MarCO-A and MarCO-B"],
            "answer": 1,
            "why": "Two Deep Space 2 microprobes were designed to impact the surface and penetrate the soil to test for ice.",
        },
        {
            "q": "What is the most probable cause of the loss?",
            "options": [
                "The parachute failed to open",
                "The heat shield separated too early",
                "A false touchdown signal shut down the engines during descent",
                "The spacecraft ran out of power",
            ],
            "answer": 2,
            "why": "Leg deployment produced a transient signal the software read as touchdown, so the engines stopped early.",
        },
        {
            "q": "About how high was the lander when the engines shut down?",
            "options": ["4 metres", "40 metres", "400 metres", "4 kilometres"],
            "answer": 1,
            "why": "The review board estimated shutdown at about 40 metres, leaving the lander to fall and impact at roughly 50 mph.",
        },
        {
            "q": "Which later mission landed successfully in the same polar region?",
            "options": ["Curiosity", "InSight", "Phoenix", "Perseverance"],
            "answer": 2,
            "why": "Phoenix landed near the Martian north pole in 2008, inheriting hardware and lessons from the Mars Polar Lander programme.",
        },
    ],
}
