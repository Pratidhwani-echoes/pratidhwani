MISSION = {
    "slug": "x-33",
    "name": "X-33",
    "artifact": "VentureStar demonstrator",
    "era": "1996 – 2001 · cancelled before first flight",
    "accent": "#b9a7ff",
    "tagline": "A spaceplane meant to make orbit routine, grounded by its own fuel tank.",
    "star": {"x": 49, "y": 52, "radius": 3.4},
    "pages": [
        {
            "title": "A spaceship that was supposed to pay for itself",
            "body": [
                "I am the X-33, a half-scale, uncrewed demonstrator built by Lockheed Martin's Skunk Works for NASA's Reusable Launch Vehicle programme. I am a lifting body about twenty metres long, with no wings to speak of, two linear aerospike engines at the back, and a shape that generates lift by being the right kind of wedge.",
                "My job was to fly a series of suborbital hops from Edwards Air Force Base, reaching speeds above Mach 10 and landing on a runway, to prove the technologies for VentureStar: a full-size, single-stage-to-orbit spaceplane that would launch satellites without throwing anything away.",
                "| The promise was economic before it was scientific. A vehicle that needs no new rocket for every flight changes what going to space costs.",
            ],
        },
        {
            "title": "The aerospike and the empty tank",
            "body": [
                "A conventional rocket bell is tuned for one altitude. My linear aerospike engines used a wedge-shaped plug nozzle, and the exhaust adjusted itself against the surrounding air pressure as I climbed. Two XRS-2200 engines produced roughly 410,000 pounds of thrust between them in a package flatter and lighter than a cluster of bells.",
                "The airframe was composite, the thermal protection was metallic rather than tile, and the propellant tanks were the real bet. Liquid hydrogen needs a large, light, very well insulated tank. My tanks were built as honeycomb sandwich structures of carbon-epoxy skins around a lightweight core: strong, stiff, and far lighter than aluminium.",
                "Every kilogram saved in the tank is a kilogram that can be payload, or the difference between reaching orbit and not.",
            ],
        },
        {
            "title": "The tyranny of the mass fraction",
            "body": [
                "A single-stage-to-orbit vehicle is almost all propellant. Roughly ninety per cent of the mass at takeoff has to be liquid hydrogen and oxygen; the structure, engines, landing gear and payload share what is left. There is no booster to drop and no second stage to take over, so every structural decision is a calculation about the last few per cent.",
                "That is why the composite tank mattered so much. It was tested at Marshall Space Flight Center in 1999 through a series of cryogenic and structural load cycles, filled with liquid hydrogen at minus 253 degrees Celsius, pressurised, loaded, and drained while engineers watched on monitors.",
                "| The tank was not a detail. On a vehicle like me, the tank is the mission.",
            ],
        },
        {
            "title": "The evening of 3 November",
            "body": [
                "The fifth test cycle appeared to finish normally. About fifteen minutes after the hydrogen was drained, during warm-up, one lobe of the tank separated: the outer skin and core peeled away from the inner skin. The investigation found microcracks in the composite facesheets that let hydrogen seep into the honeycomb core, where nitrogen outside was drawn in and trapped. Warming gas expanded inside the core and prised the layers apart. A piece of Teflon tape left during manufacture had created a weak spot.",
                "The fix was known even before the failure: fill the core with closed-cell foam. It would have added about 500 kilograms exactly where the vehicle could least afford it. The team switched to an aluminium-lithium tank, which was heavier still. The schedule slipped, the money ran out, and in March 2001 the programme was closed without a flight.",
                "I never flew. The engines were tested, the tank was not, and the lesson is not that composites are bad — it is that a single-stage vehicle has no margin for a stack of small, individually survivable mistakes.",
            ],
        },
        {
            "overview": True,
            "title": "What I was for",
            "body": [
                "I existed to retire the risk in a reusable, single-stage launch vehicle: aerospike propulsion, lightweight composite structures, metallic thermal protection, and autonomous flight control. My engines and my structural failures produced data that later reusable vehicles have used, and my cancellation marked the moment NASA stepped back from building its own next-generation launcher.",
                "The commercial reusable rockets that fly today take a different route — staged, not single-stage, and privately financed. But they inherited my argument: that reuse, not performance, is what changes the price of reaching orbit.",
            ],
            "facts": [
                ("Programme", "NASA Reusable Launch Vehicle / X-33, 1996–2001"),
                ("Builder", "Lockheed Martin Skunk Works"),
                ("Vehicle", "Uncrewed suborbital demonstrator, about 20 m long"),
                ("Engines", "Two XRS-2200 linear aerospike engines, about 1,800 kN total"),
                ("Propellant", "Liquid oxygen and liquid hydrogen"),
                ("Funding", "About $922 million from NASA plus $357 million from Lockheed Martin"),
                ("Failure", "Composite hydrogen tank debonded during testing, 3 November 1999"),
                ("Fate", "Programme closed in March 2001; never flew"),
            ],
        },
    ],
    "quiz": [
        {
            "q": "The X-33 was a demonstrator for which orbital vehicle?",
            "options": ["VentureStar", "Delta Clipper", "X-37B", "Space Shuttle"],
            "answer": 0,
            "why": "The X-33 was a half-scale technology demonstrator for VentureStar, a proposed single-stage-to-orbit spaceplane.",
        },
        {
            "q": "What kind of engine did the X-33 use?",
            "options": ["Linear aerospike", "Solid rocket motor", "Nuclear thermal", "Ion drive"],
            "answer": 0,
            "why": "Two XRS-2200 linear aerospike engines used a plug nozzle that adjusted to altitude as the vehicle climbed.",
        },
        {
            "q": "What failed during testing in November 1999?",
            "options": [
                "An aerospike engine",
                "The composite liquid hydrogen tank",
                "The landing gear",
                "The flight computer",
            ],
            "answer": 1,
            "why": "One lobe of the composite hydrogen tank debonded during warm-up after a cryogenic load test.",
        },
        {
            "q": "Why was the tank's weight so critical?",
            "options": [
                "It had to fit inside the payload bay",
                "A single-stage-to-orbit vehicle is about ninety per cent propellant, leaving very little mass for structure",
                "It was the only pressurised part of the vehicle",
                "The runway could not carry more",
            ],
            "answer": 1,
            "why": "With no boosters or stages to drop, the structure had to be extremely light; a heavier tank pushed the design out of its mass budget.",
        },
        {
            "q": "Which effect helped destroy the tank?",
            "options": [
                "Lightning strike",
                "Cryopumping of gases into the honeycomb core",
                "A software error in the autopilot",
                "Micrometeoroid impact",
            ],
            "answer": 1,
            "why": "Hydrogen seeped through microcracks and nitrogen was cryopumped into the core, raising internal pressure and separating the skin from the core.",
        },
    ],
}
