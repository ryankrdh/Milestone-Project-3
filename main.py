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
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
ranks_list = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# BOOLEAN VALUES THAT CONTROL WHILE LOOPS
game_on = True
hide_dealer_card = True

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
        return f"There are {len(self.all_cards)} cards in the deck."


# CREATING THE HAND, THIS DEALS WITH HOLDING THE CARDS DEALT FROM THE DECK AND CALCULATING THE VALUES.
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        if self.value > 21:
            self.aces == 1
        else:
            self.aces = 11


# CREATING THE CHIPS CLASS THAT WILL HANDLE PLAYER'S CHIPS, BETS, AND ONGOING WINNINGS.
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self, bet):
        self.total += self.bet
        print(f"You just win {self.bet} chips!")

    def lose_bet(self):
        self.total -= self.bet
        print(f"You just lost {self.bet} chips!")


# TAKING BETS
def take_bet():
    bet_amount = 0

    bet_amount = (int(input("How much would you like to bet?")))
    if bet_amount > chips_in_hand.total:
        print(int(input("You don't have that many chips, how much would you like to bet?")))
    else:
        print(f"You've bet {bet_amount} chips!")


# HIT
def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


# PROMPTS PLAYER TO HIT OR STAND
def hit_or_stand(deck,hand):
    answer = ''
    while answer != 'hit' or answer != 'stand':
        input("Would you like to 'hit' or 'stand'?").lower()
    if answer == 'hit':
        hit()
        print("You've decided to 'hit'")
    else:
        game_on = false
        print("You've decided to 'stand'")


# FUNCTION TO DISPLAY CARDS
def show_some(player,dealer):
    print(player.hand)
    while hide_dealer_card:
        print(dealer.hand[:-1])
def show_all(player,dealer):
    print(player.hand)
    print(dealer.hand)


cards_in_hand = Hand()
chips_in_hand = Chips()
new_deck = Deck()
new_deck.shuffle_deck()