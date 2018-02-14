### BLACKJACK GAME - SINGLE PLAYER ###
# AUTHOR: Wonhee Park


# LIBRARIES
from cards import *
from formatting import *
import random
import sys


# GLOBALS
blackjack = 21


# SUMMARY: Remove spaces from user input
def delete_whitespace(player_input):
	player_input = ''.join(player_input.split()) 
	return player_input.lower()


# SUMMARY: Validate that user input is h or s
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

# SUMMARY: Set state and total of player and show it's sum to console
def show_stats_player(person, state):
	print(color.BOLD + "%s cards are:" %person.name + color.END)
	person.show()
	person.state = state
	person_sum = person.total()
	print(color.BOLD + "sum: %d\n" %person_sum + color.END) 
	dotted_line()


# SUMMARY: Set state and total of dealer
# DEBUG: uncomment if you want to see dealer stats
def show_stats_dealer(person, state):
	# print("%s cards are:" %person.name)
	# person.show()
	person.state = state
	person_sum = person.total()
	# print("sum: %d\n" %person_sum) 
	# dotted_line()


# SUMMARY: Dealer logic to hit or stand, resetting player stats after input
# DEBUG: uncomment if you want to see values iteratively
def game_round(player, dealer, deck, player_input=None):
	if dealer.total() <= 17:
		dealer.draw(deck)
		show_stats_dealer(dealer, "continue")
	elif dealer.total() == blackjack:
		show_stats_dealer(dealer, "stop")
	# BAD ALGORITHM
	# elif dealer.total() > 17 and dealer.total() < blackjack:
	#	dealer.draw(deck)
	#	show_stats(dealer, "stop")
	else:
		show_stats_dealer(dealer, "stop")

	if player_input == "h":
		player.draw(deck)
		show_stats_player(player, "continue")
	else:
		show_stats_player(player, "stop")

	player_sum = player.total()
	dealer_sum = dealer.total()
	player_state = player.state
	dealer_state = dealer.state

	# DEBUG 
	# print("player: %d" %player_sum)
	# print("player state %s" %player_state)
	# print("dealer: %d" %dealer_sum)
	# print("dealer state %s" %dealer_state)
	return player_sum, dealer_sum


# SUMMARY: Print winner message box to console based on person (dealer or player)
def calculate_win(person, wins, num_games):
	# DEBUG
	# print("person: %s" %person.name)

	wins += 1
	if person.name == "Dealer":
		dealer_wins()
	else:
		player_wins()
	return wins


# SUMMARY: Determine winner of game round after both players are at "stop" state
# DEBUG: Uncomment to see which case of winning logic was used to determine winner. Already verified
def determine_winner(player_sum, dealer_sum, dealer, player, num_games, dealer_wins, player_wins):
	if player_sum == blackjack and dealer_sum == blackjack:
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		# DEBUG - dealer wins
		# print("case1")
		# print("HELP: %d", wins)
	elif (player_sum <= blackjack and player_sum > dealer_sum):
		wins = calculate_win(player, player_wins, num_games)
		player_wins = wins
		# DEBUG - player wins
		# print("case2")
		# print("HELP: %d", wins)
	elif (dealer_sum <= blackjack and dealer_sum > player_sum):
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		# DEBUG - dealer wins
		# print("case3")
		# print("HELP: %d", wins)
	elif (player_sum > blackjack and dealer_sum > blackjack):
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		# DEBUG - dealer wins
		# print("case4")
		# print("HELP: %d", wins)
	elif (player_sum <= blackjack and dealer_sum > blackjack):
		wins = calculate_win(player, player_wins, num_games)
		player_wins = wins
		# DEBUG - player wins
		# print("case5")
		# print("HELP: %d", wins)
	elif (dealer_sum <= blackjack and player_sum > blackjack):
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		# DEBUG - dealer wins
		# print("case6")
		# print("HELP: %d", wins)
	return dealer_wins, player_wins
	

# SUMMARY: game goes on infinitely, unless user types exit when requesting input
# DEBUG: Uncomment to see dealer stats as well
def main():
	num_games = 0
	dealer_wins = 0
	player_wins = 0

	while (1):
		beginning_msg()
		deck = Deck()
		deck.build()
		deck.shuffle()
		#deck.show()
		dotted_line()
		
		player_statement()
		player = Player("Player", "start", player_wins, num_games)
		player.draw(deck).draw(deck)
		player.show()
		dotted_line()

		dealer_statement()
		dealer = Player("Dealer", "start", dealer_wins, num_games)
		dealer.draw(deck).draw(deck)
		# dealer.show()
		
		player_sum = player.total()
		dealer_sum = dealer.total()
		# DEBUG
		# print("player sum: %d\n" %player_sum) 
		# print("dealer sum: %d\n" %dealer_sum) 
		dotted_line()

		player.state = "continue"
		dealer.state = "continue"
		while (1):
			if player.state == "stop" and dealer.state == "stop":
				break
			elif player.state == "continue":
				player_input = input_msg()
				player_input = delete_whitespace(player_input)
				player_input = validate_input(player_input)
				dotted_line()
				player_sum, dealer_sum = game_round(player, dealer, deck, player_input)
			else:
				print("dealer is still playing.\n")
				dotted_line()
				player_sum, dealer_sum = game_round(player, dealer, deck, None)

		num_games = num_games + 1

		# DEBUG
		# print("num_games: %d" %num_games)
		# print("Before cases\n")
		# print("player_sum = %d" %player_sum)
		# print("dealer_sum = %d" %dealer_sum)

		dealer_wins, player_wins = determine_winner(player_sum, dealer_sum, dealer, player, num_games, dealer_wins, player_wins)
		print("Number of games: %d" %num_games)
		print("Dealer wins: %d" %dealer_wins)
		print("Player wins: %d\n" %player_wins)
		dealer.winnings(dealer_wins, num_games)
		player.winnings(player_wins, num_games)

		# SUMMARY: requirement met, checked manually after 6 rounds 
		if num_games % 6 == 0:
			shuffle_statement()
			deck.shuffle()

		# SUMMARY: rebuild deck if deck runs out 
		deck.empty()

		end_line()
		

if __name__ == "__main__":
    main()

