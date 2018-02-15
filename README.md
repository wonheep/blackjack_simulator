# Command-line Blackjack Game Simulator

*Author: Wonhee Park*

**Files**
* ```README.md```
* ```blackjack.py```
* ```cards.py```
* ```formatting.py```

**Development Environment**
* python3

**Time to Complete**: 2/13/18-2/14/18 (in GitHub commit history)

**Running the Program**
* if you are running python3, run command: ```python blackjack.py``` 
* if environment is set to python2, install python3, and run ```python3 blackjack.py```

**Requirements**
* 1 player and 1 dealer
* Dealer must hit on soft 17.
* Single Deck. The deck is shuffled every 6 rounds.
* Player is not allowed to split cards.
* Keep track of win percentage for the player.

## Design Choice
* created classes to define a card object, deck object, and player object in ```card.py```. It was best to implement this aspect of the program as object-oriented because each had many attributes and functions that would be tedious to track via array, dictionary, and global variable implementation.
* separated formatting print statements to a different file, ```formatting.py``` in order to divide functionality and aesthetic purposes of the program.
* Used the Fisher-Yates shuffle algorithm to shuffle the deck. source below.  
* focused on modular code to avoid redundant operations
* Dealer information is private, player only knows that dealer is continuing to hit but not their hand sum. 

## Implementation Steps
* each card has suit and value, value goes from 2-10,J, Q, K, A defined via globals. 
```Python
class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
```
* each deck can build a full 52 from the globals, can shuffle using the Fisher-Yates algorithm, draw a card from the deck (decrements deck), rebuild the deck if empty
```Python
class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		
	def shuffle(self):

	def draw(self):

	def empty(self):
```
* each Player is given a name, in this case it only happense once (Player, Dealer). State: start, continue, stop. Initially given start status, the status is set to stop once both players decide to stand. Number of wins is cumulative, and number of games player played cumulative.
```Python
class Player(object):
	def __init__(self, name, state, wins, num_games):
		self.name = name
		self.state = state
		self.wins = wins
		self.num_games = num_games
		self.hand = []

	def draw(self, deck):
		
	def total(self):
		
	def winnings(self, wins, num_games):
		
	def show(self):
		
```
* ```formatting.py``` colors and text decorations used for print statements. Also includes program to draw box around text when printing to console. Below are the ANSI codes used. 
```Python
class color:
   DARKCYAN = '\033[36m'
   RED = '\033[31m'
   BLUE = '\033[34m'
   GREEN = '\033[92m'
   REDBRIGHT = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   END = '\033[0m'
```
* ```blackjack.py```
	* ```def main()``` game runs in an infinite while loop unless user gives exit input, then exits. Build beginning messages, initialize dealer and player and their attributes. Draw 2 cards for each player consecutively. Set statuses to continue and enter another infinite while loop that runs until both players have chosen to stand (state = stop). Increment game count and calculate winner based on their hand sums by calling player.winnings to calculate winning percentage. Reshuffle deck every 6 games, and check at end of each game if deck has run out of cards. 
	* ```def delete_whitespace()``` remove trailing, leading, and in-between white spaces, and convert input to lower case.
	* ```def validate_input()``` exit out of program if input is exit, continue if valid input, poll user for valid input if invalid one given. 
	* ```def game_round()``` hit/stand logic for dealer, cumulate hand sum. Update player's hand according to their input. Return both player's hand sum.
	* ```def show_stats_<dealer or player>()``` Mainly for debugging purposes, wanted to check state and sum of both player's while each round of a game is occurring. 
	* ```def determine_winner()``` logic to determine winner based on player_sum and dealer_sum. 6 scenarios mapped out. Dealer usually given biased win because if both players bust or both hit blackjack, dealer is given precedence. 
	* ```def calculate_win()``` prints winner message to console and returns increment win_count of winner to be used for calculting percentages. 

## Initial Thought Process
* handle valid input for hit and stand + error handling
* create deck, card, player struct
* generate random card from deck 
* have 2 cards given to player, and 2 cards to dealer
* calculate player sum and dealer sum 
* create hit or stand logic for dealer
* add attributes to player for winnings and current state (break condition for end of game)
* when both players are at stop state, calculate winnings
* add logic for shuffling after 6 games, add logic to build deck when deck runs out
* format print statements
* separate code to be modular
* do unit testing (esp. for ace of spades calculation)
* add more intense algorithm for dealer to hit or stand
* do analytics on n number of games and see the winning average 


## Testing
* method: iteratively check functionality and edge cases, instead of debugging at the end
* debug: used print statements through each modular function that returned dependent variables
* manually ran 6 games and tested that deck was reshuffled
* verified that winning percentage calculated cumulatively 
* input can handle spaces and tabs between text, and polls user for valid input until given so


## Key Information
* I did not get to implement automated unit tests to handle large edge cases. (Ex: check deck is rebuilt after 52 games, use of Ace's 1 or 11 value logic, skew of hit and stand algorithm of dealer)
* I did not get to implement a stronger dealer hit/stand algorithm. Currently, using a simple 3-case scenario for dealer. 
	* initially included this logic, but later deleted since it skewed the favor towards player wins.
```Python 
		elif dealer.total() > 17 and dealer.total() < blackjack:
			dealer.draw(deck)
		    show_stats(dealer, "stop")
```


## Sources
* Online Resources:
	* game rules:[link1](http://www.blackjackinfo.com/blackjack-rules.php)
	* shuffle algorithm (Fisher Yates): [link3](http://code.activestate.com/recipes/360461-fisher-yates-shuffle/)
	* deck OOP: [link4](https://www.youtube.com/watch?v=t8YkjDH86Y4)
	* default arguments: [link5](https://stackoverflow.com/questions/24719368/syntaxerror-non-default-argument-follows-default-argument)
	* ANSI code for colors: [link6](https://en.wikipedia.org/wiki/ANSI_escape_code)
	* drawing boxes around text: [link7](https://stackoverflow.com/questions/39969256/draw-a-box-around-message-line)

