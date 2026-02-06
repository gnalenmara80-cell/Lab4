"""
Program Name: Lab4_Deal Cards
Author: Gnalen Mara
Purpose: This program simulates dealing a hand of cards. The user chooses how many
cards they want, and the program randomly generates that many unique cards from
standard card values and suits. Cards do not repeat in the hand.
Starter Code: No starter code used.
Date: 02/06/2026
"""

import random

# List of card values and suits
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["c", "h", "s", "d"]  # clubs, hearts, spades, diamonds

# Ask the user for the number of cards they want
num_cards = int(input("How many cards would you like to be dealt? "))

# Create an empty list to store the player's hand
hand = []

# Generate random unique cards
while len(hand) < num_cards:
    value = random.choice(values)
    suit = random.choice(suits)
    card = value + suit

    if card not in hand:
        hand.append(card)

# Print the player's hand
print("\nYour hand of cards:")
for card in hand:
    print(card)

# Print total number of cards
print("\nTotal number of cards in hand:", len(hand))