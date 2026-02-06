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
# list of card values and suits
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',] 
suits = [ 'c', 'h', 's', 'd']  # clubs, diamonds, hearts, spades
#this code ask the user fo the number of card they want
num_cards = int(input("how many cards would you like to be dealt? "))
# this code generates and empty list to store the player's hand
hand = []
# this code generates random cards until the hand has the desired number of unique cards
while len(hand) < num_cards:
    value = random.choice(values) 
    suits = random.choice(suits)
    card = value + suits
    if card not in hand: 
        hand.append(card)
        # this code prints the player's hand
        print("\nYour hand of cards:")
        for card in hand:
            print(card)
    # output total number of cards
    print(f"\nTotal number of cards in hand: {len(hand)}")