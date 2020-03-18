import random
#function for getting user input
def input_val():
    name = input('Enter you name')
    return name
#Class defining deck features
class Deck:
    def __init__(self):
        card_face = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
        cards = list(zip(card_face, values))
        self.suit = cards*4

    def shuffle_card(self):
        random.shuffle(self.suit)

    def draw_card(self):
        self.shuffle_card()
        card = self.suit.pop()
        # print('card drawn is {} of value {}'.format(card[0],card[1]))
        return card

class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_card(self):
        for c in self.hand:
            print('card drawn is {} of value {}'.format(c[0], c[1]))

    def calculate_score(self):
        _score = 0
        for c in self.hand:
            _score += c[1]
        # print('{} score is : {}'.format(self.name, _score))
        return _score


class Player(Dealer):
    def __init__(self, name):
        super().__init__(name)

    def hit_or_stick(self):
        while True:
            choice = input("Do you want another card (Y/N)? ")
            if choice.lower().startswith('y'):
                return True
            elif choice.lower().startswith('n'):
                return False
            else:
                print("invalid entry")
                continue

class Game:
    def __init__(self, player, dealer='Jarvis'):
        self.deck = Deck()
        self.dealer = Dealer(dealer)
        self.player = Player(player)

    def draw_from_deck(self, person):
        card_drawn = self.deck.draw_card()
        person.hand.append(card_drawn)

    def play_game(self):
        # game start by giving two cards alternatively to player and dealer
        self.draw_from_deck(self.player)
        print('below is the hand of ', self.player.name)
        self.player.show_card()
        self.draw_from_deck(self.dealer)
        print('below is the hand of ', self.dealer.name)
        self.dealer.show_card()
        self.draw_from_deck(self.player)
        print('below is the hand of ', self.player.name)
        self.player.show_card()
        self.draw_from_deck(self.dealer)

        print('{} has a score of {}'.format(self.player.name, self.player.calculate_score()))
        hit = False
        if self.player.calculate_score() == 21 and self.dealer.calculate_score() == 21:
            print('The match is tied')
        elif self.player.calculate_score() == 21 and self.dealer.calculate_score() < 21:
            print(self.player.name, ' is the winner')
        else:
            hit = self.player.hit_or_stick()
            while hit is True:
                self.draw_from_deck(self.player)
                print('{} has a score of {}'.format(self.player.name, self.player.calculate_score()))
                if self.player.calculate_score() < 21:
                    hit = self.player.hit_or_stick()
                else:
                    hit = False
            print('{} has a score of {}'.format(self.player.name, self.player.calculate_score()))

            if self.player.calculate_score() == 21:
                print(self.player.name, 'is the winner')
            elif self.player.calculate_score() > 21:
                print(self.dealer.name, 'is the winner')
            else:
                print(self.player.name, ' has called a stand now its ', self.dealer.name, ' turn to pick card')
                self.dealer.show_card()
                print('{} has a score of {}'.format(self.dealer.name, self.dealer.calculate_score()))
                while self.dealer.calculate_score() < 17:
                    self.draw_from_deck(self.dealer)
                    print('{} has a score of {}'.format(self.dealer.name, self.dealer.calculate_score()))
                if self.dealer.calculate_score() > 21:
                    print(self.player.name, 'is the winner')
                elif self.player.calculate_score() > self.dealer.calculate_score():
                    print(self.player.name, 'is the winner')
                elif self.dealer.calculate_score() > self.player.calculate_score():
                    print(self.dealer.name, 'is the winner')
                else:
                    print('The match is tied')









