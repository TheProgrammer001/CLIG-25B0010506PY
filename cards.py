"""
CLIU-25B0010506PY — Card data and ASCII art templates for the Blackjack game

This module provides:
- Definitions for card ranks and suits (types)
- A mapping from card ranks to their Blackjack point values
- ASCII art templates for each card suit and rank display (including special 10 cards)
- Functions to generate random cards and render cards as ASCII art strings
- A hidden card template for dealer’s face-down cards

Functions:
- get_rand_cards(): Returns two random card ranks and suits as lists
- generate_card(rank, suit): Returns ASCII art string for a specific card
- side_by_side(*cards): Utility function to print multiple ASCII cards side-by-side

Author: Dr. Programmer, 2025
"""


from random import choices


card_ranks = ['K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10]
card_types = ["Heart", "Diamond", "Club", "Spade"]

points = {
    'K': 10, 'Q': 10, 'J': 10, 'A': [1, 11], '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10':10
}

# Heart
heart_template = """
.-------.
|X_  _  |
|( \/ ) |
| \  /  |
|  \/ X |
`-------'
"""

heart_10 = """
.-------.
|10_  _ |
| ( \/ )|
|  \  / |
|   \/10|
`-------'
"""

#   Diamond
diamond_template = """
.------.
|X /\  |
| /  \ |
| \  / |
|  \/ X|
`------'
"""

diamond_10 = """
.------.
|10/\  |
| /  \ |
| \  / |
|  \/10|
`------'
"""

# Club
club_template = """
.------.
|X     |
|  ⬤   |
| ⬤ ⬤  |
|  ⊥  X|
`------'
"""

club_10 = """
.------.
|10    |
|  ⬤   |
| ⬤ ⬤  |
|  ⊥ 10|
`------'
"""

# spade
spade_template = """
.------.
|X     |
|  /\  |
| (__) |
|  ⊥  X|
`------'
"""

spade_10 = """
.------.
|10    |
|  /\  |
| (__) |
|  ⊥ 10|
`------'
"""

hidden_card = """
.------.
|?     |
|HIDDEN|
| CARD |
|     ?|
`------'
"""

templates = {
    "Heart": {
        "default": heart_template,
        "10": heart_10
    },
    "Diamond":{
        "default": diamond_template,
        "10": diamond_10
    },
    "Spade": {
        "default": spade_template,
        "10": spade_10
    },
    "Club": {
        "default": club_template,
        "10": club_10
    }
}

# heart and diamond is red. spade and club is black

def get_rand_cards():

    rand_card_ranks = choices(card_ranks, k=2)
    rand_card_suits = choices(card_types, k=2)

    return rand_card_ranks, rand_card_suits


def generate_card(rank, suit):
    template_type = "10" if rank == 10 else "default"
    template = templates[suit][template_type]
    card = template.replace('X', str(rank))

    return card

