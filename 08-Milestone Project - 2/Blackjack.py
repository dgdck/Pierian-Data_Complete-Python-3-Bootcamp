from random import shuffle


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    # Create the cards
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        # Create the deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_cards(self, x):
        # Shuffle deck
        i = 0
        while i <= x:
            shuffle(self.all_cards)
            i += 1

    def deal_one(self):
        # pop card from deck
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name.capitalize()
        self.all_cards = []
        if name.lower() != 'dealer':
            self.balance = 100

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) is list:
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a sinle Card object
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return self.name


if __name__ == '__main__':
    print("Welcome to Blackjack!")
    print(
        """

    The rules are:
    Get as close to 21 without going over it.
    This game uses a standard 52-card deck.
    You start with 100 chips.

        """
    )

    # Create and shuffle deck
    play_deck = Deck()
    play_deck.shuffle_cards(10)

    # Create dealer and player
    dealer = Player('dealer')
    player = ''

    while player == '':
        try:
            player = Player(input("What is your name? "))
            player.balance

        except AttributeError:
            print("Sorry, you can't be the dealer")
            player = ''

        else:
            print(f"Welcome {player}! Here are your {player.balance} chips.")

    game_on = True
    while game_on:

        pass
