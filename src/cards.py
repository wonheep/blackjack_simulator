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

	def empty(self):
		if len(self.cards) ß== 0:
			self.build()


# SUMMARY: Player can draw card from deck
# FUNCTIONS: draw a card from deck, show the card
class Player(object):
	def __init__(self, name, state):
		self.name = name
		self.state = state
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.draw())
		return self

	def total(self):
		sum_hand = 0
		for c in self.hand:
			if sum_hand > 21 and c.value == "Ace":
				sum_hand -= 10
			elif c.value == "Jack" or c.value == "Queen" or c.value == "King":
				sum_hand += 10;
			elif c.value == "Ace":
				sum_hand += 11
			else:
				sum_hand += int(c.value)

		return sum_hand

	def winnings(self, wins, num_games):
		if wins == 0:
			print("{} winning percentage = 0%".format(self.name))
		else:
			print("{} winning percentage = {}%".format(self.name, round(100*float(wins)/float(num_games), 2)))

	def show(self):
		for c in self.hand:
			c.show();
