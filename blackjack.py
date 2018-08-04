import random

SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
         "Jack", "Queen", "King", "Ace")
VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
          "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
PLAYING = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck():
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        card_list = ""
        for card in self.deck:
            card_list += str(card) + "\n"
        return card_list

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop()
        return card


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet cannot exceed {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global PLAYING
    while True:
        hs = input("Would you like to hit or stand? Enter 'h' or 's': ")
        if hs[0].lower() == "h":
            hit(deck, hand)
        elif hs[0].lower() == "s":
            print("player_hand stands. dealer_hand is PLAYING.")
            PLAYING = False
        else:
            print("Please input 'h' or 's'")
            continue
        break

def show_some(player, dealer):
    print("Dealer's Hand:")
    print(" <card hidden>")
    print(f" {dealer.cards[1]}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Total = ", player.value)

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Total = ", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Total = ", player.value)

def player_busts(player, dealer, chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("\nDealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("\nDealer wins!")
    chips.lose_bet()

def push():
    print("\nPlayer and Dealer tie! It is a push.")


# BlackJack game
first_hand = True
while True:
    if first_hand:
        print("Welcome to BlackJack!")
        player_chips = Chips()
        first_hand = False
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)
    while PLAYING:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal())
        show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push()
    print(f"\nPlayer's new amount of chips is {player_chips.total}")
    if player_chips.total == 0:
        print("You are out of chips. Thanks for playing.")
        break
    play_again = input("Would you like to play again? Enter 'y' or 'n' ")
    if play_again[0].lower() == "y":
        PLAYING = True
        continue
    else:
        print("Thanks for playing.")
        break
