# Classes for Card, Deck, Player 

# LIBRARIES
import random


# GLOBALS
suits = ["clubs", "diamonds", "hearts", "spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


# SUMMARY: Each card has a suit and value
# FUNCTIONS: show card 
class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
		print("{} of {}".format(self.value, self.suit))


# SUMMARY: Each deck has 52 cards
# FUNCTIONS: Build the deck, show each card in the deck, shuffle the deck
class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in suits:
			for v in values:
				self.cards.append(Card(s,v))

	# Fisher-Yates Shuffle Algorithm (source in README.md)
	def shuffle(self):
		length = len(self.cards) - 1
		for i in range(length, 0, -1):
			rand_num = random.randint(0, i)
			if rand_num == i:
				continue
			self.cards[i], self.cards[rand_num] = self.cards[rand_num], self.cards[i]

	def draw(self):
		return self.cards.pop()

	def empty():
		if len(self.cards) == 0:
			return True


# SUMMARY: Player can draw card from deck
# FUNCTIONS: draw a card from deck, show the card
class Player(object):
	def __init__(self, name, state, winnings):
		self.name = name
		self.state = state
		self.winnings = winnings
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.draw())
		return self

	def show(self):
		for c in self.hand:
			c.show();
