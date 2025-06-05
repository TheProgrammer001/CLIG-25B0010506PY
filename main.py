"""
CLIG-25B0010506PY — Command-Line Interactive Blackjack Game

This Python script implements a command-line Blackjack (21) game where a player
competes against the dealer. The player can hit (draw a card) or stand (stop drawing),
and the dealer follows standard Blackjack rules to draw cards until reaching at least 17 points.

Features:
- Visual card display using ASCII art and colored output via the chromafy module.
- Real-time keyboard input handling for 'hit', 'stand', 'play', 'help', and 'quit'.
- Accurate point calculation including proper handling of Aces (counting as 1 or 11).
- Simple game loop with clear user prompts and results.

Usage:
    Run the script directly:
        python blackjack.py

    Controls during the game:
        - Press 'H' to hit (draw a new card).
        - Press 'S' to stand (end your turn).
        - Press 'P' from the main menu to play a new game.
        - Press 'H' from the main menu to display instructions.
        - Press 'Q' from the main menu to quit the program.

Dependencies:
- Python standard libraries: time, random
- External modules: chromafy, keyboard, cards (make sure these are installed or available)

Author:
    Dr. Programmer, 2025

Version:
    1.0.0 (June 5, 2025)

"""


from time import sleep
from random import choice
import chromafy
import keyboard
import cards


title = """
.-------.
|A_  _  |
|( \/ ).------.
| \  / |K /\  |
|  \/  | /  \ |
`------| \  / |
       |  \/ K|
       `------'
 ____  _        _    ____ _  __   _   _    ____ _  __
| __ )| |      / \  / ___| |/ /  | | / \  / ___| |/ /
|  _ \| |     / _ \| |   | ' /_  | |/ _ \| |   | ' / 
| |_) | |___ / ___ \ |___| . \ |_| / ___ \ |___| . \ 
|____/|_____/_/   \_\____|_|\_\___/_/   \_\____|_|\_\\

"""



instructions = """
Welcome to Blackjack!

How to Play:
- The goal is to get your cards' points as close to 21 as possible without going over (busting).
- Number cards count as their number value.
- Face cards (King, Queen, Jack) count as 10 points.
- Aces can count as either 1 or 11 points, whichever helps you more.

Gameplay:
1. You and the dealer both get two cards initially.
2. One of the dealer's cards is shown; the other is hidden.
3. You can choose to 'Hit' (draw another card) or 'Stand' (end your turn).
4. If your total points go over 21, you bust and lose immediately.
5. After you stand, the dealer reveals their hidden card.
6. The dealer will draw cards until their total points are at least 17.
7. The winner is the one with points closest to 21 without going over.
8. If both have the same points, it's a tie.

Controls:
- Press 'H' to Hit (draw a new card).
- Press 'S' to Stand (end your turn).
- Press 'P' from the main menu to Play a new game.
- Press 'H' from the main menu to view these instructions.
- Press 'Q' to Quit the game.

Good luck and have fun!
"""

dealer_points = 0
player_points = 0

def slow_print(text, delay=0.01):
    for ch in text:
        print(ch, end='', flush=True)
        sleep(delay)

def calculate_points(ranks):
    """
    Calculate the total Blackjack points for a list of card ranks.

    Aces count as 11 or 1 to prevent busting.

    Args:
        ranks (list of str): List of card ranks, e.g., ['A', '7', '3'].

    Returns:
        int: The total points value.
    """

    total = 0
    aces = 0

    for rank in ranks:
        if rank == 'A':
            aces += 1
            total += 11  # Assume 11 first
        else:
            total += cards.points[str(rank)]

    # Downgrade Ace(s) from 11 to 1 if we bust
    while total > 21 and aces:
        total -= 10  # Downgrade one Ace from 11 to 1
        aces -= 1

    return total

def dealer_turn():
    dealer_ranks = []
    dealer_suits = []

    for _ in range(2):
        rank = choice(cards.card_ranks)
        suit = choice(cards.card_types)
        dealer_ranks.append(rank)
        dealer_suits.append(suit)

    dealer_points = calculate_points(dealer_ranks)

    while dealer_points < 17:
        rank = choice(cards.card_ranks)
        suit = choice(cards.card_types)
        dealer_ranks.append(rank)
        dealer_suits.append(suit)
        dealer_points = calculate_points(dealer_ranks)

    return dealer_ranks, dealer_suits, dealer_points

def game():
    global player_points

    # Player gets 2 cards
    player_ranks, player_suits = cards.get_rand_cards()
    player_points = calculate_points(player_ranks)

    # Dealer draws 2 hidden cards now, will reveal after player stands
    dealer_ranks, dealer_suits = [choice(cards.card_ranks) for _ in range(2)], [choice(cards.card_types) for _ in range(2)]

    # Create player card drawings
    player_cards = [cards.generate_card(player_ranks[0], player_suits[0]), cards.generate_card(player_ranks[1], player_suits[1])]
    dealer_card1 = cards.generate_card(dealer_ranks[0], dealer_suits[0])

    # Show dealer's one card + hidden card
    print("\nDealer's Cards:")
    for line1, line2 in zip(dealer_card1.splitlines(), cards.hidden_card.splitlines()):
        color1 = [255, 0, 0] if dealer_suits[0] in ['Heart', 'Diamond'] else [0, 0, 0]
        print(f"{chromafy.format(line1, foreground=color1)}     {chromafy.format(line2, foreground=[128, 0, 128])}")

    # Show player's cards
    print("\nPlayer's Cards:")
    for line1, line2 in zip(player_cards[0].splitlines(), player_cards[1].splitlines()):
        color1 = [255, 0, 0] if player_suits[0] in ['Heart', 'Diamond'] else [0, 0, 0]
        color2 = [255, 0, 0] if player_suits[1] in ['Heart', 'Diamond'] else [0, 0, 0]
        print(f"{chromafy.format(line1, foreground=color1)}     {chromafy.format(line2, foreground=color2)}")

    print(f"\nPlayer has {player_points} points.")

    # --- Player's Turn ---
    while True:
        print(chromafy.format("Press 'H' to hit or 'S' to stand", foreground=[0, 255, 255]))
        key = keyboard.read_key()

        if key == 'h':
            new_rank = choice(cards.card_ranks)
            new_suit = choice(cards.card_types)
            player_ranks.append(new_rank)
            player_suits.append(new_suit)

            new_card = cards.generate_card(new_rank, new_suit)
            color = [255, 0, 0] if new_suit in ['Heart', 'Diamond'] else [0, 0, 0]
            print("\nNew Card Drawn:")
            print(chromafy.format(new_card, foreground=color))

            player_points = calculate_points(player_ranks)
            print(f"\nPlayer now has {player_points} points.")

            if player_points > 21:
                print(chromafy.format("Player busted! Dealer wins!", foreground=[255, 0, 0]))
                return

        elif key == 's':
            print("\nPlayer stands.")
            break

        sleep(0.1)

    # --- Dealer's Turn ---
    print("\nDealer's Turn Begins...")
    dealer_ranks, dealer_suits, dealer_points = dealer_turn()

    # Draw dealer cards
    dealer_cards = [cards.generate_card(r, s) for r, s in zip(dealer_ranks, dealer_suits)]

    print("\nDealer's Full Cards:")
    for lines in zip(*[c.splitlines() for c in dealer_cards]):
        line_output = []
        for i, line in enumerate(lines):
            color = [255, 0, 0] if dealer_suits[i] in ['Heart', 'Diamond'] else [0, 0, 0]
            line_output.append(chromafy.format(line, foreground=color))
        print("   ".join(line_output))

    print(f"\nDealer has {dealer_points} points.")

    # --- Final Result ---
    if dealer_points > 21:
        print(chromafy.format("Dealer busted! Player wins!", foreground=[0, 255, 0]))
    elif player_points > dealer_points:
        print(chromafy.format("Player wins!", foreground=[0, 255, 0]))
    elif player_points < dealer_points:
        print(chromafy.format("Dealer wins!", foreground=[255, 0, 0]))
    else:
        print(chromafy.format("It's a tie!", foreground=[255, 255, 0]))

print(chromafy.format(title, 1, [255, 0, 0]))

while True:
    player_points = 0
    print(chromafy.format("Press 'H' for help, 'P' to play or 'Q' to quit.", foreground=[0, 255, 255]))

    key = keyboard.read_key()

    if key == 'q':
        break

    elif key == 'p':
        game()

    elif key == 'h':
        slow_print(instructions)

    else:
        sleep(0.5)
        pass

    if keyboard.is_pressed(key):
        sleep(0.1)
