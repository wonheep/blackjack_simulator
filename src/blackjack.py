# BLACKJACK GAME - SINGLE PLAYER
# AUTHOR: Wonhee Park

# LIBRARIES
from cards import Card, Deck, Player
from formatting import border_msg, dotted_line, end_line, color
import random
import sys

# GLOBALS
blackjack = 21

def delete_whitespace(player_input):
	player_input = ''.join(player_input.split()) 
	return player_input.lower()

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
	print("%s cards are:" %person.name)
	person.show()
	person.state = state
	person_sum = person.total()
	print("sum: %d\n" %person_sum) 
	dotted_line()
	#return person_sum, person.state


def game_round(player, dealer, deck, player_input=None):
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

	if player_input == "h":
		player.draw(deck)
		show_stats(player, "continue")
	else:
		show_stats(player, "stop")

	# DEBUG 
	player_sum = player.total()
	dealer_sum = dealer.total()
	player_state = player.state
	dealer_state = dealer.state
	print("player: %d" %player_sum)
	print("player state %s" %player_state)
	print("dealer: %d" %dealer_sum)
	print("dealer state %s" %dealer_state)

	return player_sum, dealer_sum


def calculate_win(person, wins, num_games):
	wins += 1
	print("person: %s" %person.name)
	if person.name == "Dealer":
		print(color.BOLD + color.RED + "DEALER WINS!\n" + color.END + color.END)
	else:
		print(color.BOLD + color.DARKCYAN + "YOU WIN!\n" + color.END + color.END)
	#print("{} winning percentage = {}%".format(person.name, round(100*float(wins)/float(num_games),2)))
	dotted_line()
	return wins


def determine_winner(player_sum, dealer_sum, dealer, player, num_games, dealer_wins, player_wins):
	if player_sum == blackjack and dealer_sum == blackjack:
		# dealer wins
		print("case1")
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		print("HELP: %d", wins)
	elif (player_sum <= blackjack and player_sum > dealer_sum):
		#player wins
		print("case2")
		wins = calculate_win(player, player_wins, num_games)
		player_wins = wins
		print("HELP: %d", wins)
	elif (dealer_sum <= blackjack and dealer_sum > player_sum):
		#dealer wins
		print("case3")
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		print("HELP: %d", wins)
	elif (player_sum > blackjack and dealer_sum > blackjack):
		#dealer wins
		print("case4")
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		print("HELP: %d", wins)
	elif (player_sum <= blackjack and dealer_sum > blackjack):
		#player wins
		print("case5")
		wins = calculate_win(player, player_wins, num_games)
		player_wins = wins
		print("HELP: %d", wins)
	elif (dealer_sum <= blackjack and player_sum > blackjack):
		#dealer wins
		print("case6")
		wins = calculate_win(dealer, dealer_wins, num_games)
		dealer_wins = wins
		print("HELP: %d", wins)
	return dealer_wins, player_wins
	

def main():
	num_games = 0
	dealer_wins = 0
	player_wins = 0

	while (1):
		print(border_msg("""    Welcome to a game of Blackjack!   """, 40))
		print("Type" + color.BOLD + " exit " + color.END + "if you ever want to exit out of your game.\n")
		deck = Deck()
		deck.build()
		deck.shuffle()
		#deck.show()
		dotted_line()
		
		print("Here are your cards, player!")
		player = Player("Player", "start", player_wins, num_games)
		player.draw(deck).draw(deck)
		player.show()

		print("\nThe dealer has his cards now too!")
		dealer = Player("Dealer", "start", dealer_wins, num_games)
		dealer.draw(deck).draw(deck)
		dealer.show()
		dotted_line()
		
		#DEBUG
		player_sum = player.total()
		dealer_sum = dealer.total()
		print("player sum: %d\n" %player_sum) 
		print("dealer sum: %d\n" %dealer_sum) 
		dotted_line()

		player.state = "continue"
		dealer.state = "continue"
		while (1):
			if player.state == "stop" and dealer.state == "stop":
				break
			elif player.state == "continue":
				player_input = input("Would you like to hit or stand?\nType h to hit and s to stand: ")
				player_input = delete_whitespace(player_input)
				player_input = validate_input(player_input)
				dotted_line()
				player_sum, dealer_sum = game_round(player, dealer, deck, player_input)
			else:
				print("dealer is still playing.\n")
				dotted_line()
				player_sum, dealer_sum = game_round(player, dealer, deck, None)

		num_games = num_games + 1
		print("num_games: %d" %num_games)

		# DEBUG
		print("Before cases\n")
		print("player_sum = %d" %player_sum)
		print("dealer_sum = %d" %dealer_sum)

		dealer_wins, player_wins = determine_winner(player_sum, dealer_sum, dealer, player, num_games, dealer_wins, player_wins)
		print("dealer wins: %d" %dealer_wins)
		print("player wins: %d" %player_wins)
		dealer.winnings(dealer_wins, num_games)
		player.winnings(player_wins, num_games)

		if num_games % 6 == 0:
		 	print("Reshuffling Deck!")
		 	deck.shuffle()
		deck.empty()
		end_line()
		

if __name__ == "__main__":
    main()