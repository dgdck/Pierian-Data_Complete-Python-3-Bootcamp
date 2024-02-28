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
        return self.all_cards.pop(0)


class Player:

    def __init__(self, name):
        self.name = name.capitalize()
        self.all_cards = []
        self.placed_bet = 0
        self.total_value = 0
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
    
    def bet(self, amount=5):
        self.balance -= amount
        self.placed_bet = amount
        return f"You have placed a bet of {self.placed_bet}. You have {self.balance} of chips left."
    
    def calculate_cards(self):
        total_value = 0
        ace_card = False
        for card in self.all_cards:
            if card.rank == 'Ace':
                ace_card = True
            total_value += card.value
        if total_value > 21 and ace_card is True:
            total_value -= 10
        return total_value

    def __str__(self) -> str:
        return self.name


'''
newplayer = Player('Test')
print(newplayer.bet())
print(newplayer.balance)
'''


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
        # Reset cards in hands
        dealer.all_cards = []
        player.all_cards = []

        print("\n" * 2)

        place_bet = True
        while place_bet:
            try:
                x = int(input("Place your bet. Minimum is 5. "))
                
            except ValueError:
                print("Please enter a number")
            
            else:
                if x < 5:
                    print("The minimum bet is 5 chips.")
                else:
                    print(player.bet(x))
                    place_bet = False

        dealer.add_cards(play_deck.deal_one())
        player.add_cards(play_deck.deal_one())
        dealer.add_cards(play_deck.deal_one())
        player.add_cards(play_deck.deal_one())

        print(f"You have a {player.all_cards[0]} and {player.all_cards[1]}")
        print(f"Your total value is: {player.calculate_cards()}\n")
        print(f"The dealer has {dealer.all_cards[-1]} and a card face down.\n")

        dealer_cardvalue = dealer.calculate_cards()
        player_cardvalue = player.calculate_cards()

        if player_cardvalue == 21:
            player.balance += player.placed_bet * 2
            print("You have BLACKJACK")
            print(f"Your new balance is: {player.balance} chips.\n")

        action = True
        while action:
            action = input("Choose the following: stand, hit, double or surrender ").lower()
            dealer_cardvalue = dealer.calculate_cards()
            player_cardvalue = player.calculate_cards()

            if action == 'stand':
                # Keep your cards and dealer reveals his second card.
                # Check who won.
                print(f"The dealer has {dealer.all_cards[-1]} and {dealer.all_cards[0]}.")
                print(f"The dealer's cardvalue is: {dealer.calculate_cards()}\n")

                if dealer_cardvalue > player_cardvalue:
                    print("Dealer has won\n")
                    break

                elif dealer_cardvalue == player_cardvalue:
                    print("The cards have equal value\n")
                    break

                elif dealer_cardvalue < player_cardvalue:
                    player.balance += player.placed_bet * 2
                    print("You have won this round")
                    print(f"You now have {player.balance} chips.\n")
                    break            

            if action == 'hit':
                # Player gets an additional card
                # Can be repeated untill bust
                pass
            
            if action == 'double':
                # Double wager and get 1 additional card
                # Check who won
                pass

            if action == 'surrender':
                # Give up and lose half your bet
                # Start new round
                pass

            place_bet = True

       # game_on = False
