"""*****************************************************************
Title: Tic-Tac-Toe Game
Author: Dan Page

Description: This program is a simple Tic Tac Toe game where each
player will take their turn placing an X or O on the board until
someone wins or they tie (when all board spots are full).  The
players have the option of playing as many games as they'd like.

Date Created: 02/10/2018
Date Updated: 02/11/2018
*****************************************************************"""


# PROGRAM START


# FUNCTIONS FOR THE GAME

# Start Game Function
def start_game():
    """
    INPUT: Void
    OUTPUT: Text for game start as well as gathering user inputs
    """
    print("Welcome to Tic-Tac-Toe!")

    input("\nPress any key to continue...")

    print("""
    This game has a few rules:
        1 - There are 9 spots on a 3x3 board with two players in the game
        2 - One user will be X's, the other will be O's
        3 - Each player will take their turn placing their mark (X or O) on the board
        4 - The first player to get 3 in a row of their mark WINS
    """)

    input("Press any key to continue...\n")

    # Create user info
    global user1, user2, mark1, mark2
    user1 = input("Who is going first? ")
    print("Welcome {user}!".format(user=user1))
    mark1 = input("Would you like to be X or O? ")
    print("\n")

    user2 = input("Who is going second? ")
    print("Welcome {user}!".format(user=user2))
    if mark1.upper() == "X":
        print("You are O's!")
        mark2 = "O"
    else:
        print("You are X's!")
        mark2 = "X"

    # Creating User Choice lists to track their spot choices
    global spots1, spots2
    spots1 = []
    spots2 = []

    input("\nPress any key to begin the game!\n")


# Game Board Function
def game_board():
    """
    INPUT: VOID
    OUTPUT: The current state of the Tic Tac Toe Board
    """

    print("Here is the current Game Board:")

    # Print Format with the spots list in order to dynamically insert X's/O's based on user input
    print("""

     {} | {} | {} 
    ---|---|---
     {} | {} | {} 
    ---|---|---
     {} | {} | {} 
     

    """.format(board_spots[0],
               board_spots[1],
               board_spots[2],
               board_spots[3],
               board_spots[4],
               board_spots[5],
               board_spots[6],
               board_spots[7],
               board_spots[8]))


# Player Input Function
def player_input(player):
    """
    INPUT: Name of the player
    OUTPUT: Gathers their choice on the board
    """
    while True:
        spot_choice = int(input("{play}, please choose a spot: ".format(play=player)))

        if spot_choice in board_spots:
            if player == user1:
                spots1.append(spot_choice)
                board_spots[spot_choice - 1] = mark1
                break
            else:
                spots2.append(spot_choice)
                board_spots[spot_choice - 1] = mark2
                break
        else:
            print("That spot is already taken!")
            continue


# Check Win Function
def win_check(player_spots):
    """
    INPUT: list of user spaces
    OUTPUT: Boolean of whether or not the user has won, based on their spaces
    """

    # Check for every winning combination
    if (1 in player_spots) and (2 in player_spots) and (3 in player_spots):
        return True
    elif (4 in player_spots) and (5 in player_spots) and (6 in player_spots):
        return True
    elif (7 in player_spots) and (8 in player_spots) and (9 in player_spots):
        return True
    elif (1 in player_spots) and (4 in player_spots) and (7 in player_spots):
        return True
    elif (2 in player_spots) and (5 in player_spots) and (8 in player_spots):
        return True
    elif (3 in player_spots) and (6 in player_spots) and (9 in player_spots):
        return True
    elif (1 in player_spots) and (5 in player_spots) and (9 in player_spots):
        return True
    elif (3 in player_spots) and (5 in player_spots) and (7 in player_spots):
        return True
    else:
        return False


# End Game Function
def end_game():
    """
    INPUT: Void
    OUTPUT: Displays the end game text with the winner and losoer
    """
    print("Congratulations {won}, you've won the game!".format(won=winner))
    print("Sorry {los}, better luck next time!".format(los=loser))
    print("\n")


# THE GAME
while True:

    # Start Game
    start_game()

    # Show Board
    board_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # Spots on the board
    available_spots = 9     # Track number of spots in case of tie game
    game_board()

    # Single Game Loop
    while True:

        # Player 1's Turn
        player_input(user1)
        available_spots -= 1
        game_board()

        # Player 1 Win Check
        if win_check(spots1):
            # Assign Winner and Loser
            winner = user1
            loser = user2
            end_game()
            break

        # Run out of board spots with no winner yet
        if available_spots <= 0:
            print("It's a Tie!")
            break

        # Player 2's Turn
        player_input(user2)
        available_spots -= 1
        game_board()

        # Player 2 Win Check
        if win_check(spots2):
            # Assign Winner and Loser
            winner = user2
            loser = user1
            end_game()
            break

    # Checks if players want to play again
    repeat = input("\nWould you like to play again?(y/n): ")
    if repeat.lower() == "y":
        continue
    else:
        print("\nHave a great rest of your day!!!!")
        break

# PROGRAM END