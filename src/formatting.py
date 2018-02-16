### Functions for print statement formatting ###


class color:
   DARKCYAN = '\033[36m'
   RED = '\033[31m'
   BLUE = '\033[34m'
   GREEN = '\033[92m'
   REDBRIGHT = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   END = '\033[0m'


def box_lines(lines, width):
    topBottomRow = "+" + "-" * width + "+"
    middle = "\n".join("|" + x.ljust(width) + "|" for x in lines)
    return "\n" + color.BOLD + color.RED + "{0}\n{1}\n{0}".format(topBottomRow, middle) + color.END + color.END


def box_lines2(lines, width):
    topBottomRow = "+" + "-" * width + "+"
    middle = "\n".join("|" + x.ljust(width) + "|" for x in lines)
    return "\n" + color.BOLD + color.GREEN + "{0}\n{1}\n{0}".format(topBottomRow, middle) + color.END + color.END


def split_line(line, width):
    return [line[i:i+width] for i in range(0, len(line), width)]


def split_msg(msg, width):
    lines = msg.split("\n")
    split_lines = [split_line(line, width) for line in lines]
    return [item for sublist in split_lines for item in sublist] # flatten


def border_msg(msg, width):
    return(box_lines(split_msg(msg, width), width))


def winner_msg(msg, width):
    return(box_lines2(split_msg(msg, width), width))


def dotted_line():
    print(color.BOLD + "-------------------------------------------------------" + color.END)

def dotted_line2():
    print(color.BOLD + "-------------------DEALER PLAYS------------------------" + color.END)

def end_line():
	 print(color.BOLD + color.REDBRIGHT + "\n-----------------------END GAME-------------------------\n" + color.END + color.END)


def shuffle_statement():
	print(color.BOLD + color.BLUE + "Reshuffling Deck!" + color.END + color.END)


def player_statement():
	print(color.BOLD + "Here are your cards, player!\n" + color.END)


def dealer_statement():
	print(color.BOLD + "\nThe dealer has his cards now too!\n" + color.END)
	print(color.DARKCYAN + "HIDDEN: Card 1" + color.END)

def beginning_msg():
	print(border_msg("""    Welcome to a game of Blackjack!   """, 40))
	print("Type" + color.BOLD + " exit " + color.END + "if you ever want to exit out of your game.\n")


def dealer_wins():
	print(winner_msg(("    DEALER WINS!   "), 20))
	print("\n")


def player_wins():
	print(winner_msg(("   YOU WIN!   "), 15))
	print("\n")

def push():
	print(winner_msg(("     TIE! NOBODY WON!     "), 25))
	print("\n")


def input_msg():
	print(color.BOLD + color.BLUE + "Would you like to hit or stand?" + color.END + color.END)
	player_input = input(color.BLUE + "Type h to hit and s to stand: " + color.END)
	return player_input

def summarygame():
	 print(color.BOLD + "\n-------------------SUMMARY OF GAME---------------------\n" + color.END)


