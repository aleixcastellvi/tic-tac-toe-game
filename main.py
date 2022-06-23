import random

from utils import *


# Game structure variable (dictionary of 9 keys and keys)
dic = initial_dict()
# Number of games counter
game_number = 0


# A starting order of the game is assigned.
# In a random way it is decided which player starts playing
players = []

if random.randint(0, 1) == 0:
    players.append('X')
    players.append('O')

else:
    players.append('O')
    players.append('X')


print("Let's start! :-D")
# Starting game board
grid_3x3(dic)


while True:

    # First player's turn to choose a position
    print(f'Player {players[0]} turn. Enter position: ')
    player_turn(dic, players[0])

    # After choice position, a game is added to the counter
    game_number += 1

    # The updated board is displayed
    grid_3x3(dic)

    # Check if after end of the turn, there is a winner
    if game_winner(dic) == True:
        print(f'PLAYER {players[0]} HAS WON!!!')
        break

    # If after 9 turns there is no winner, there is a tie
    elif game_number == 9:
        print(f'TIE BETWEEN PLAYER {players[0]} AND PLAYER {players[1]}')
        break

    # Second player's turn to choose a position
    print(f'Player {players[1]} turn. Enter position: ')
    player_turn(dic, players[1])

    # After choice position, a game is added to the counter
    game_number += 1

    # The updated board is displayed
    grid_3x3(dic)

    # Check if after end of the turn, there is a winner
    if game_winner(dic) == True:
        print(f'PLAYER {players[1]} HAS WON!!!')
        break
