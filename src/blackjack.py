### BLACKJACK GAME - SINGLE PLAYER ###
# AUTHOR: Wonhee Park


# LIBRARIES
from cards import *
from formatting import *
import random
import sys


# GLOBALS
#blackjack = ["Jack", "Queen", "King"]
tens = ["Jack", "Queen", "King"]

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
def show_stats(person, state):
	print(color.BOLD + "%s cards are:" %person.name + color.END)
	person.show()
	person.state = state
	person_sum = person.total()
	print(color.BOLD + "sum: %d\n" %person_sum + color.END) 
	dotted_line()


# SUMMARY: Player logic for hit/stand 
def player_round(player, deck, player_input=None):
	if player_input == "h":
		player.draw(deck)
		if player.total() > 21:
			show_stats(player, "stop")
		else:
			show_stats(player, "continue") 
	else:
		show_stats(player, "stop")

	player_sum = player.total()
	player_state = player.state

	# DEBUG 
	# print("player: %d" %player_sum)
	# print("player state %s" %player_state)

	return player_sum

# SUMMARY: Dealer logic for hit/stand
def dealer_round(dealer, deck, known, unknown):
	if dealer.total() <= 16:
		dealer.draw(deck)
		show_stats(dealer, "continue")
	elif dealer.total() == 17:
		for c in dealer.hand:
			if c.value == "Ace":
				dealer.draw(deck)
				show_stats(dealer, "continue")
		else:
			show_stats(dealer, "stop")
	elif dealer.total() == 21:
		show_stats(dealer, "stop")
	else:
		show_stats(dealer, "stop")

	dealer_sum = dealer.total()
	dealer_state = dealer.state

	# DEBUG 
	# print("dealer: %d" %dealer_sum)
	# print("dealer state %s" %dealer_state)

	return dealer_sum

# SUMMARY: game goes on infinitely, unless user types exit when requesting input
# DEBUG: Uncomment to see dealer stats as well
def main():
	num_games = 0
	d_wins = 0
	p_wins = 0

	while (1):
		beginning_msg()
		deck = Deck()
		deck.build()
		deck.shuffle()
		dotted_line()
		
		player_statement()
		player = Player("Player", "start", player_wins, num_games)
		player_card1 = player.draw(deck)
		player_card2 = player.draw(deck)
		player.show()
		dotted_line()

		dealer_statement()
		dealer = Player("Dealer", "start", dealer_wins, num_games)
		known = dealer.draw(deck)
		unknown = dealer.draw(deck)
		dealer.show_one()

		player_sum = player.total()
		dealer_sum = dealer.total()
		# DEBUG
		# print("player sum: %d\n" %player_sum) 
		# print("dealer sum: %d\n" %dealer_sum) 
		dotted_line()

		player.state = "continue"
		dealer.state = "continue"

		# player gets blackjack
		if player_sum == 21 and dealer_sum != 21:
			player_wins()
			p_wins += 1
		# both player and dealer are blackjack, tie
		elif player_sum == 21 and dealer_sum == 21:
			push()
		else: 
			while(1):
				if player.state == "stop":
					break
				player_input = validate_input(delete_whitespace(input_msg()))
				dotted_line()
				player_sum = player_round(player, deck, player_input)

			# player busts 
			if player_sum > 21:
				print(color.BOLD + "YOU BUSTED" + color.END)
				dealer_wins()
				d_wins += 1
			# player has 21 (non blackjack) or less than 21 
			else:
				while(1):
					if dealer.state == "stop":
						break
					dotted_line2()
					dealer_sum = dealer_round(dealer, deck, known, unknown)

				# dealer has blackjack 
				if dealer_sum == 21 and len(dealer.hand)==2:
					dealer_wins()
					d_wins += 1
				# dealer busts
				elif dealer_sum > 21:
					player_wins()
					p_wins += 1
				elif dealer_sum > player_sum:
					dealer_wins()
					d_wins += 1
				elif player_sum > dealer_sum:
					player_wins()
					p_wins += 1 
				else:
					push()

		# summarizing information 
		num_games += 1
		summarygame()
		print(color.BOLD + "dealer hand" + color.END)
		dealer.show()
		print("dealer sum: %d\n" %dealer_sum) 
		print(" ")
		print(color.BOLD + "player hand" + color.END)
		player.show()
		print("player sum: %d\n" %player_sum) 
		print("\nNumber of games: %d" %num_games)
		print("Dealer wins: %d" %d_wins)
		print("Player wins: %d\n" %p_wins)
		dealer.winnings(d_wins, num_games)
		player.winnings(p_wins, num_games)

		# SUMMARY: requirement met, checked manually after 6 rounds 
		if num_games % 6 == 0:
			shuffle_statement()
			deck.shuffle()

		# SUMMARY: rebuild deck if deck runs out 
		deck.empty()

		end_line()
		

if __name__ == "__main__":
    main()

