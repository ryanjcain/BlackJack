import random
class Card(object):
    """Represents a standard playing card.
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.
        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    """Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


class Player(Deck):
    """Represents a player in the blackjack game"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

class Dealer(Deck):

    """Represents the dealer's hand and the house's
    restrictions for playing the game"""

    def __init__(self, label=''):
        self.cards = []
        self.label = label

class Shoe(Deck):
    """ The shoe object is a collection of 6 decks """

    def __init__(
        self, deck1=Deck(), deck2=Deck(), deck3=Deck(),
        deck4=Deck(), deck5=Deck(), deck6=Deck()
        ):

        deck_list = [deck1,deck2,deck3,deck4]

        self.cards = []
        for deck in deck_list:
            for card in deck.cards:
                self.cards.append(card)


    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


class Game(object):
    def __init__(
    self, player = Player(), shoe = Shoe(), dealer = Dealer(), hand = Hand()
    ):
        print '''
        Welcome to Casino!
        '''

    def play(self):
        shoe = Shoe()
        hand = Hand()
        card = Card()
        score = 0 #determine how close to 21
        if raw_input("Do you want to play? (Y) or (N) ") == 'Y':
            shoe.shuffle()
            shoe.move_cards(hand, 2)
            print "Here's your starting hand: %s" % (', '.join(map(str, hand.cards)))
            #making hand.cards list into string to print

            #Initialize player's score
            for card in hand.cards:
                if card.rank > 10:
                    card.rank = 10
                score += card.rank
            print "Your score is %d" % (score) #too high, indices of face cards wrong

            #Player plays until they either call or bust.
            while score < 21:
                if raw_input("Would you like to hit? (Y) or (N) ") == 'Y':
                    shoe.move_cards(hand, 1)
                    print "Now here's your hand: %s" % (', '.join(map(str, hand.cards)))
                else:
                    break

                #Recalculate the score with the new card in hand
                score = 0
                for card in hand.cards:
                    if card.rank > 10:
                        card.rank = 10
                    score += card.rank
                print "Your score is %d" % (score) #too high, indices of face cards wrong



            print "Sorry you busted!"



        else:
            print "Guess you won't play with us :("

game = Game()
game.play()

def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.
    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


"""
git add <file name> or -A or .
git commit -m "Message"
git commit (Creates a multi-line comment, use esc :wq to finish)
git push
git pull
git status
git branch
git branch <new branch name>
git checkout <branch name>
git merge <origin repository>
"""
