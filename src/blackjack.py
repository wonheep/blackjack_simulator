# BLACKJACK GAME - SINGLE PLAYER
# AUTHOR: Wonhee Park

# LIBRARIES
from cards import Card
from cards import Deck
from cards import Player
import random
import sys

# GLOBALS
num_games = 0

winnings = 0
state = ["start", "continue", "stop"]
start_state = "start"
blackjack = 21

all_done = False

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

def main():

	while (1):
		print("\nWelcome to a game of blackjack!")
		print("Type exit if you ever want to exit out of your game.\n")
		deck = Deck()
		deck.build()
		deck.shuffle()
		#deck.show()
		print("-----------------------------------------------------------")
		
		print("Here are your cards, player!\n")
		player = Player("Player", start_state, winnings)
		player.draw(deck).draw(deck)
		player.show()
		player_cards = player.hand

		print("\nThe dealer has his cards now too!\n")
		dealer = Player("Dealer", start_state, winnings)
		dealer.draw(deck).draw(deck)
		dealer_cards = dealer.hand
		print("-----------------------------------------------------------")
		
		player_input = input("Would you like to hit or stand?\nType h to hit and s to stand: ")
		player_input = delete_whitespace(player_input)
		player_input = validate_input(player_input)
		print("-----------------------------------------------------------")

		* Dealer must hit on soft 17.
		* Single Deck. The deck is shuffled every 6 rounds.
		* Keep track of win percentage for the player.

		if num_games % 6 == 0:
			deck.shuffle()
		if deck.empty() == True:
			deck.build()

		player_sum = 
		dealer_sum = 

		if player_input == "h":
			player.draw(deck)
			player.show()
			player.state("continue")
		else:
			player.state("stop")
			print("Your cards are:\n")
			player.show()
			print("Total: %d" %player_sum)
			print("-----------------------------------------------------------")


		if player.state = "stop" and dealer.state = "stop":
			num_games++
			if player_sum == blackjack and dealer_sum == blackjack:
				# dealer wins
			else if (player_sum <= blackjack && player_sum > dealer_sum):
				#player wins
			else if (dealer_sum <= blackjack && dealer_sum > player_sum):
				#dealer wins
			else if (player_sum > blackjack && dealer_sum > blackjack):
				#dealer wins






		
if __name__ == "__main__":
    main()