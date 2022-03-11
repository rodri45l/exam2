
Pig Dice Game
==========================
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


The Pig Dice game is a fun exciting game which you can play and enjoy. The game of Pig is a very simple jeopardy dice game in which two players race to reach 100 points. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player holds and scores the sum of the rolls (i.e. the turn total).


## Table of Contents
* General Info
* Technologies Used
* Usage
* Setup
* Features
* Project requirements
* Acknowledgements


## General Information
To start the game the user can use the command `make play` or simply run the cmd_game.py file.

### Commands
- `play`: Play vs the computer, the user must pass the game mode (easy, hard) as an argument. 
- `play2`: Two player game.
- `rules`: Show the rules.
- `scoreboard`: Print the scoreboard.
- `bye` : exit the game.
- `help` : Prints all the commands , if another command is passed as an argument instructions for this command will be printed.

## Test/Cheat
In order to be able to test the different features we added some cheat codes, when asked for the user name use HIVA, YANA OR RODRI45Z . This will allow the user to start with a score of 100 and will instantly win the game.
There is a 4th name that can be used, if the player name is "test" the computer will instantly win the game.

## Technologies Used
- Python - version 3.9 [![Language used: Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/python)
- Git - version 2.25.1 


## Run testsuit
TO run the full testsuit use the following command `make test`
## Documentation
Original documentation can be found in the doc folder. To regenerate documentation simply run `make doc`
## Game Intelligence

Our game has 2 modes of intelligence.
First one is the "easy" mode , where the computer just chooses a random option (roll or hold).
There is one more mode available to play , the "hard" mode.


The hard mode was developed using data and equations from [Optimal Play of the Dice Game Pig](http://cs.gettysburg.edu/~tneller/papers/pig.zip)
The module should_roll contains the source code. Using the data the function should_roll() calculates the choice with more chances of winning. These probabilities were calculated using [value iteration](https://en.wikipedia.org/wiki/Markov_decision_process#Value_iteration). 

Using data with the probabilities to win if the user turn total is 0 we can calculate the probabilities for the rest of scores and then calculate the choice with more probabilities.




## Setup
First step would be to set the python name used. Makefile uses `PYTHON=python` as default.
create a virtual enviroment using the command `make venv`, once created the user should initiate this virtual enviroment using:

- . .venv/Scripts/activate (Windows)

- . .venv/bin/activate (linux/MacOS)

Then once inside the virtual enviroment the user should install the required packages using `make install`

After this the user can simply run `make play` to play the game or run the cmd_game.py file in the diceGame folder.


## Features
- Play an awesome amusing game with rolling your DICE!
- Keep track of your score


## Project requirements
1.Functionality
2.Structure
3.Unittesting
4.Document by comments
5.Generate documentation from comments
6.Generate UML diagrams from code
7.Use semantic versioning
8.Code style
9.README.md
10.Presentation video
(https://hkr.instructure.com/courses/4708/pages/assignment-2-test-driven-development)



## Acknowledgements
- This project was based on [Assignment 2 - Test driven development](https://en.wikipedia.org/wiki/Pig_(dice_game)).
- Thanks to our teacher Mikael Roos


Created by: Rodri, Yana, Hiva