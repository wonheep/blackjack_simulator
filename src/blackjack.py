# BLACKJACK GAME - SINGLE PLAYER
# AUTHOR: Wonhee Park

# LIBRARIES
from cards import Card
from cards import Deck
from cards import Player
import random
import sys

# GLOBALS
dealer_winnings = 0
player_winnings = 0
blackjack = 21
#all_done = False

# SUMMARY: deletes whitespace before, between and after text
def delete_whitespace(player_input):
	player_input = ''.join(player_input.split()) 
	return player_input.lower()

# SUMMARY: error checking from user input
def validate_input(player_input):
	if player_input == "exit":
		sys.exit()
	if player_input == "s" or player_input == "h":
		return player_input
	else:
		player_input = input("--------Invalide input!--------\nPlease type h for hit or s for stand: ")
		delete_whitespace(player_input)
		validate_input(player_input)
		return player_input


def show_stats(person, state):
	print("%s cards are:\n" %person)
	person.show()
	person.state = state
	person_sum = person.total()
	print("sum: %d\n" %person_sum) 
	print("-----------------------------------------------------------")


def game_round(player_input, player, dealer, deck):

	# Player's request
	if player_input == "h":
		player.draw(deck)
		show_stats(player, "continue")
	else:
		show_stats(player, "stop")

	# Dealer's Algorithm
	if dealer.total() <= 17:
		dealer.draw(deck)
		show_stats(dealer, "continue")
	elif dealer.total() == blackjack:
		show_stats(dealer, "stop")
	# BAD ALGORITHM
	#elif dealer.total() > 17 and dealer.total() < blackjack:
	#	dealer.draw(deck)
	#	show_stats(dealer, "stop")
	else:
		show_stats(dealer, "stop")

def calculate_winning(person, winnings, num_games):
	
	if person == "dealer":
		print("DEALER WINS!\n")
	else:
		print("YOU WIN!\n")
	print("-----------------------------------------------------------")
	winnings = winnings + 1
	person.winnings(winnings, num_games)
	break

def main():

	num_games = 0

	while (1):
		print("\nWelcome to a game of blackjack!")
		print("Type exit if you ever want to exit out of your game.\n")
		deck = Deck()
		deck.build()
		deck.shuffle()
		#deck.show()
		print("-----------------------------------------------------------")
		
		print("Here are your cards, player!\n")
		player = Player("Player", "start")#, start_state, player_winnings)
		player.draw(deck).draw(deck)
		player.show()

		print("\nThe dealer has his cards now too!\n")
		dealer = Player("Dealer", "start")#, start_state, dealer_winnings)
		dealer.draw(deck).draw(deck)
		dealer.show()
		print("-----------------------------------------------------------")
		
		#DEBUG
		player_sum = player.total()
		dealer_sum = dealer.total()
		print("player sum: %d\n" %player_sum) 
		print("dealer sum: %d\n" %dealer_sum) 
		print("-----------------------------------------------------------")

		while (1):
			if player.state == "stop" and dealer.state == "stop":
				break
			else:
				player_input = input("Would you like to hit or stand?\nType h to hit and s to stand: ")
				player_input = delete_whitespace(player_input)
				player_input = validate_input(player_input)
				print("-----------------------------------------------------------")
				game_round(player_input, player, dealer, deck)

		num_games = num_games + 1
		print("num_games: %d" %num_games)

		# * Dealer must hit on soft 17.
		# * Single Deck. The deck is shuffled every 6 rounds.
		# * Keep track of win percentage for the player.

		# if num_games % 6 == 0:
		# deck.shuffle()
		# if deck.empty() == True:
		# deck.build()

		if player_sum == blackjack and dealer_sum == blackjack:
			# dealer wins
			calculate_winning(dealer, dealer_winnings, num_games)
		elif (player_sum <= blackjack && player_sum > dealer_sum):
			#player wins
			calculate_winning(player, player_winnings, num_games)
		elif (dealer_sum <= blackjack && dealer_sum > player_sum):
			#dealer wins
			calculate_winning(dealer, dealer_winnings, num_games)
		elif (player_sum > blackjack && dealer_sum > blackjack):
			#dealer wins
			calculate_winning(dealer, dealer_winnings, num_games)
		elif (player_sum <= blackjack && dealer_sum > blackjack):
			#player wins
			calculate_winning(player, player_winnings, num_games)
		elif (dealer_sum <= blackjack && player_sum > blackjack):
			#dealer wins
			calculate_winning(dealer, dealer_winnings, num_games)
			

if __name__ == "__main__":
    main()