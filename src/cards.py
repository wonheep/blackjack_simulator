### Classes for Card, Deck, Player objects ###


# LIBRARIES
import random
from formatting import *


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
		print(color.DARKCYAN + "{} of {}".format(self.value, self.suit) + color.END)


# SUMMARY: Each deck has 52 cards
# FUNCTIONS: Build the deck, shuffle the deck, draw from the deck, rebuild if deck is empty
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
		if len(self.cards) == 0:
			self.build()


# SUMMARY: Player attributes and capabilities
# FUNCTIONS: draw a card from deck, calculate hand total, winnings percentage, show cards in hand
class Player(object):
	def __init__(self, name, state, wins, num_games):
		self.name = name
		self.state = state
		self.wins = wins
		self.num_games = num_games
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.draw())
		return self

	def total(self):
		sum_hand = 0
		for c in self.hand:
			if c.value == "Jack" or c.value == "Queen" or c.value == "King":
				sum_hand += 10;
			elif c.value == "Ace":
				temp = sum_hand + 11
				if temp > 21:
					sum_hand += 1
				else:
					sum_hand +=11
			else:
				sum_hand += int(c.value)
		return sum_hand

	def winnings(self, wins, num_games):
		if wins == 0:
			print(color.BOLD + color.GREEN + "{} winning percentage = 0%".format(self.name) + color.END + color.END)
		else:
			print(color.BOLD + color.GREEN + "{} winning percentage = {}%".format(self.name, round(100*float(wins)/float(num_games), 2))+ color.END + color.END)

	def show(self):
		for c in self.hand:
			c.show();

	def show_one(self):
		 c = self.hand[0]
		 c.show()
