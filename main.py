'''
Game will have only one player against a dealer.

Card rank are as follows:

2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(10), Queen(10), King(10), Ace(1 or 11)

Player can either STAND or HIT. You are also able to determine the betting amount.
'''

import random
import pdb

# LIST THAT MAKES UP A FULL DECK OF CARDS
# PYTHON SUIT SYMBOLS: CLUBS = \u2663, SPADES = \u2660, DIAMONDS = \u2666, HEARTS = \u2665
suits_list = ('\u2663', '\u2660', '\u2666', '\u2665')
values_list = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
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
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp


# # Debugging
# test_deck = Deck()
# print(test_deck)

# CREATING THE HAND, THIS DEALS WITH HOLDING THE CARDS DEALT FROM THE DECK AND CALCULATING THE VALUES.
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values_list[card.rank]

        # Track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# # Debugging
# test_deck = Deck()
# test_deck.shuffle_deck()
#
# # PLAYER
# test_player = Hand()
# # deal 1 card from the deck CardType(suit, rank)
# pulled_card = test_deck.deal_one()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)


# CREATING THE CHIPS CLASS THAT WILL HANDLE PLAYER'S CHIPS, BETS, AND ONGOING WINNINGS.
class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        print(f"You just won {self.bet} chips!")

    def lose_bet(self):
        self.total -= self.bet
        print(f"You just lost {self.bet} chips!")


# TAKING BETS
def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?"))

        except:
            print("Please input numbers only")

        else:
            if chips.bet > chips.total:
                print(
                    f"You don't have that many chips, how much would you like to bet? You currently have {chips.total} chips.")
            else:
                print(f"You've bet {chips.bet} chips!")
                break


# # Debugging
# chips_in_hand = Chips()
# print(chips_in_hand.total)
# take_bet(chips_in_hand)

# HIT
def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


# PROMPTS PLAYER TO HIT OR STAND
def hit_or_stand(deck,hand):
    global game_on
    answer = ''
    while (answer != 'hit' and answer != 'stand'):
        answer = input("Would you like to 'hit' or 'stand'?").lower()
    if answer == 'hit':
        hit(deck,hand)
        print("You've decided to 'hit'.")
        print("\n" * 3)
    else:
        print("You've decided to 'stand'.")
        print("\n" * 3)
        print("\nNow it's Dealer's turn.")
        game_on = False


# FUNCTION TO DISPLAY SOME CARDS
def show_some(player, dealer):
    # Shows only ONE of the dealer's cards and all of player's cards.
    print("\n Dealer's Hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])
    print("\n Player's Hand: ", *player.cards, sep='\n')


# FUNCTION TO DISPLAY ALL CARDS
def show_all(player, dealer):
    # Shows all of both dealer and player's cards.
    # sums up the values.
    print("\n Dealer's Hand: ", *dealer.cards, sep='\n')
    print(f"Value of Dealer's hand is: {dealer.value}")
    print("\n Player's Hand: ", *player.cards, sep='\n')
    print(f"Value of Player's hand is: {player.value}")


# END GAME SCENARIO HANDLERS
def player_busts(player, dealer, chips):
    print("PLAYER BUST!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUST! PLAYER WINS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Both the dealer and player tie! PUSH")


# ASKING THE PLAYER TO PLAY ANOTHER HAND
def play_again():
    answer = ''
    while (answer != 'yes' and answer != 'no'):
        answer = input("Would you like to play another hand? 'yes' or 'no'?").lower()
    if answer == 'yes':
        return True
        print("You've decided to play another hand!")
    else:
        print("You've decided to stop playing!")
        return False



# GAMEPLAY
start_new_game = True

# Print an opening statement
print(
    "WELCOME TO BLACKJACK! \nGame will have only ONE PLAYER aginst the DEALER. \nCard rank are as follows: \n2, 3, 4, 5, 6, 7, 8, 9, 10, Jack(10), Queen(10), King(10), Ace(1 or 11) \nThe player will start out with 100 chips. Good luck!")

# Set up the Player's chips
player_chips = Chips()

# Create & shuffle the deck, deal two cards to each player
deck = Deck()
deck.shuffle_deck()

while start_new_game:

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while game_on:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        else:
            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)

                # Show all cards
                show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)

                elif player_hand.value > dealer_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)

                elif player_hand.value < dealer_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)

                else:
                    push(player_hand, dealer_hand)

            # Inform Player of their chips total
            print(f"\nPlayer has {player_chips.total} chips total.")
            game_on = False
    # Ask to play again
    if not play_again():
        break
    else:
        start_new_game = True
        game_on = True