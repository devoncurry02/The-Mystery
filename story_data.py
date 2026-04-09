Story = {
    "card1": {
        "image": "new york.png",
        "text": [
            [
                "The sun sets on New York, bringing a coolness to the air.",
                "",
                "(Left click anywhere to continue)"
            ],
            [
                "Your name is Don Peters, and you are an FBI investigator. You",
                "recieved a call from a museum executive saying that they",
                "recieved an anonymous text about a robbery being planned."
            ]
        ],
        "hitboxes": [
            {"x": 0, "y": 0, "width": 1536, "height": 1024, "next_card": "card2"}
        ]
    },
    "card2": {
        "image": "museum.png",
        "text": [
            [
                "The museum's gala event is tonight, and the centerpiece of",
                "the event is what has the museum executive so worried. The",
                "'Mote in The Eye' is a priceless diamond that the museum..."
            ],
            [
                "recently acquired. Security is on high alert, but they have",
                "had mysterious dissapearances of precious items on display",
                "before."
            ]
        ],
        "hitboxes": [
            {"x": 572, "y": 250, "width": 300, "height": 200, "next_card": "card3"}
        ]
    },
    "card3": {
        "image": "inside museum.png",
        "text": [
            [
                "The museum is filled with quite chatter, and you see the",
                "'Mote in The Eye' on display in the center of the room."
            ],
            [
                "(Try clicking on different areas, people, and objects to",
                "choose your path forward.)"
            ]
        ],
        "hitboxes": [
            {"x": 0, "y": 0, "width": 410, "height": 330, "next_card": "card4a"},
            {"x": 1140, "y": 215, "width": 210, "height": 220, "next_card": "card4b"},
            {"x": 635, "y": 360, "width": 200, "height": 200, "next_card": "card4c"}
        ]
    },
    "card4a": {
        "image": "hallway.png",
        "text": [
            [
                "Guests are walking around the gallery and eating in the",
                "dining area."
            ]
        ],
        "hitboxes": [
            {"x": 1110, "y": 210, "width": 426, "height": 600, "next_card": "card3"},
            {"x": 725, "y": 361, "width": 57, "height": 79, "next_card": "card4a1"},
            {"x": 400, "y": 824, "width": 700, "height": 200, "next_card": "card3"}
        ]
    },
    "card4a1": {
        "image": "office.png",
        "text": [
            [
                "President's Office."
            ]
        ],
        "hitboxes": [
            {"x": 500, "y": 200, "width": 500, "height": 600, "next_card": "card4a"},
        ]
    },
    "card4b": {
        "image": "executive and guard.png",
        "text": [
            [
                "You decide to talk to the museum's executive."
            ],
            [
                "EXECUTIVE: Oh, thank you for coming so quickly agent",
                "Peters. My name is Mr. Withers, let me give you a",
                "quick rundown of the situation."
            ],
            [
                "HEAD OF SECURITY: actually sir, I think it would be best if",
                "I gave the rundown."
            ]
        ],
        "hitboxes": [
            {"x": 700, "y": 200, "width": 180, "height": 220, "next_card": "card3"}
        ]
    },
    "card4c": {
        "image": "display case.png",
        "text": [
            [
                "The display case is secured with advanced locking mechanisms."
            ]
        ],
        "hitboxes": [
            {"x": 0, "y": 0, "width": 1536, "height": 1024, "next_card": "card3"}
        ]
    }
}