'''
Game will have only have one player against a dealer.

Card rank are as follows:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(10), Queen(10), King(10), Ace(1 or 11)

Player can either STAND or HIT. You are also able to determine the betting amount.
'''
'''
Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
'''


import random
import pdb


# LIST THAT MAKES UP A FULL DECK OF CARDS
# PYTHON SUIT SYMBOLS: CLUBS = \u2663, SPADES = \u2660, DIAMONDS = \u2666, HEARTS = \u2665
suits_list = ("\u2663, \u2660, \u2666, \u2665")
values_list = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
ranks_list = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# BOOLEAN VALUES THAT CONTROL WHILE LOOPS
game_on = True


# CREATING A SINGLE CARD TYPE
class CardType:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values_list[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# CREATING THE DECK, SHUFFLE, AND DEALING ONE CARD.
class Deck:

    def __init__(self):
        # Creates a new deck of cards at the beginning of the game.
        self.all_cards = []
        for suit in suits_list:
            for rank in ranks_list:
                self.all_cards.append(CardType(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        return f"self.all_cards"


