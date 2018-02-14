# Command-line Blackjack Game Simulator

*Author: Wonhee Park*

**Files**
* ```README.md```
* ```blackjack.py```

**Development Environment**
* python 3

**Time to Complete**: 2/13/18-2/14/18

**Running the Program**
* if you are running python3, run command: ```python blackjack.py``` 
* if env is set to python2, install python3, and run ```python3 blackjack.py```

**Requirements**
* Dealer must hit on soft 17.
* Single Deck. The deck is shuffled every 6 rounds.
* Player is not allowed to split cards.
* Keep track of win percentage for the player.

## Design Choice


## Implementation


## Testing


## Challenges


## Key Information
- dealer algorithm not complete
- not taking into account what happens when cards run out during draw process

## Sources
* Online Resources:
	* game rules:[link1](http://www.blackjackinfo.com/blackjack-rules.php)
	* shuffle algorithm: [link2](https://www.programiz.com/python-programming/examples/shuffle-card)
	* shuffle algorithm (Fisher Yates): [link3](http://code.activestate.com/recipes/360461-fisher-yates-shuffle/)
	* deck OOP: [link4](https://www.youtube.com/watch?v=t8YkjDH86Y4)
	* https://stackoverflow.com/questions/24719368/syntaxerror-non-default-argument-follows-default-argument


## To Do
* handle valid input for hit and stand, create error checking
* generate random card from deck via a class
* have 2 cards given to player, and 2 cards to dealer
* get player sum and dealer sum 
* run hit or stand logic for both palyers
* add attributes to player for winnings and current state
* when both players are at stop state, calculate winnings
* add logic for shuffling after 6 games, add logic to build deck when deck runs out
* add Header for Rules of Game: 21 is blackjack, > 21 is bust, both bust dealer wins, 
* do unit testing for ace of spades 
* add more intense algorithm for dealer to hit or stand
* do analytics on n number of games and see the winning average 

TMRW
- have all player's winning percentage show
- check percentages for 6 rounds. 
- create text box around header of game (formatting) and cite 
- logic to build deck when deck runs out
- clean up code 
- README.md 
- submit

- create unit tests

Bugs:
- fix Ace issue doesnt decrement if its less than 21
