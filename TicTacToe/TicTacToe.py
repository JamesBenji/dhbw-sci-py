# TicTacToe Game

# reusables: ["", "", ""]
opponent_symbol = "X"
computer_symbol = "O"

diagonal_1 = ["1", "5", "9"]
diagonal_2 = ["3", "5", "7"]

row_1 = ["1", "2", "3"]
row_2 = ["4", "5", "6"]
row_3 = ["7", "8", "9"]

column_1 = ["1", "4", "7"]
column_2 = ["2", "5", "8"]
column_3 = ["3", "6", "9"]

diagonals = [diagonal_1, diagonal_2]
columns = [column_1, column_2, column_3]
rows = [row_1, row_2, row_3]

tic_tac_toe_grid = {
    "1": "-",
    "2": "-",
    "3": "-",
    "4": "-",
    "5": "-",
    "6": "-",
    "7": "-",
    "8": "-",
    "9": "-",
}

moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
available_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
played_moves = []

# UI options
welcome_screen_options = ["1", "2", "3", "4", "5"]
welcome_message = "\n<<<<<<<<<<<<<<<<<<<TICTACTOE>>>>>>>>>>>>>>>>>>> \n"
welcome_prompt = "Make a selection (Enter the selction number) \n"

welcome_options = """
    1. Start game
    2. Know the rules
    3. See previous scores
    4. Learn how the game works
    5. End program
    
    # Press Ctrl + C to end the program at any time \n
"""

print(welcome_message)
print(welcome_prompt)
print(welcome_options)

selected_welcome_screen_option = input()


while selected_welcome_screen_option not in welcome_screen_options:
    print("Invalid selection. \n")
    print("[TRY AGAIN] Make a selection. Valid options are 1, 2, 3, 4, 5 \n")

    selected_welcome_screen_option = input()

# Utility variables

#demo
demo_grid = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

# Utility methods

#demo
def display_tic_tac_toe_grid_demo(demo_grid_dictionary):
    print("\n\n\n[Demo Grid] The grid has 9 positions. Select the position you want to make a move on using its correcponding number\n\n\n")
    row_line_demo = ""
    for value in demo_grid_dictionary.values():
        row_line_demo += f"   {value}   "
        if value == "3" or value == "6" or value == "9":
            print(row_line_demo)
            print("\n")
            row_line_demo = ""

    print("[TL;DR] 9 positions from 1 to 9. Select your target position using the numbers \n\n\n")


def display_tic_tac_toe_grid(grid_dictionary):
    print("[TicTacToe Grid]\n\n\n")
    row_line_demo = ""
    for key, value in grid_dictionary.items():
        row_line_demo += f"   {value}   "
        if key == "3" or key == "6" or key == "9":
            print(row_line_demo)
            print("\n")
            row_line_demo = ""

def get_user_move():
    user_move_selection = input()

    while user_move_selection not in moves:
        print("Invalid selection. \n")
        print("[TRY AGAIN] Make a selection. Valid options are 1, 2, 3, 4, 5 \n")
        user_move_selection = input()

    while user_move_selection in played_moves:
        print("This move has already been played. Select another move position \n")
        user_move_selection = input()

    return user_move_selection

def update_grid_with_move(move, symbol, grid):
    grid[move] = symbol


def update_grid_with_opponent_move(move):
    update_grid_with_move(move, opponent_symbol, tic_tac_toe_grid)

def update_grid_with_computer_move(move):
    update_grid_with_move(move, computer_symbol, tic_tac_toe_grid)

def get_computer_move(grid):
    # calculate the next best move
    computed_move = "1"
    return computed_move


def start_game():
    display_tic_tac_toe_grid(tic_tac_toe_grid)
    opponent_move = get_user_move()
    update_grid_with_opponent_move(opponent_move)
    computer_move = get_computer_move(tic_tac_toe_grid)
    update_grid_with_computer_move(computer_move)
    

# Program core

display_tic_tac_toe_grid_demo(demo_grid)

while True:
    start_game()
