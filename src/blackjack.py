# BLACKJACK GAME - SINGLE PLAYER
# AUTHOR: Wonhee Park

# LIBRARIES
import random
import sys

# GLOBALS
num_dealings = 0
num_games = 0
num_cards = 52
blackjack = 21

dealer_cards = []
player_cards = []

# STRUCTS
# CREATE card shuffling algorithm 

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

# SUMMARY: shuffle what remains of the deck 
def shuffle_cards(num_cards):
	return

def main():

	while (1):
		print("\nWelcome to a game of blackjack!")
		print("Type exit if you ever want to exit out of your game.\n")
		print("-----------------------------------------------------------")
		print("Here are your cards, player!\n")
		print("The dealer has his cards now too!\n")
		print("-----------------------------------------------------------")
		player_input = input("Would you like to hit or stand?\nType h to hit and s to stand: ")
		player_input = delete_whitespace(player_input)
		player_input = validate_input(player_input)

		
if __name__ == "__main__":
    main()