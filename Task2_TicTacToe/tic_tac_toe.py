import random

# Initialize empty board
game_board = ["-" for _ in range(9)]

def show_board():
    print()
    for i in range(0, 9, 3):
        print(game_board[i], "|", game_board[i+1], "|", game_board[i+2])
    print()

def is_winner(symbol):
    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for pos in winning_positions:
        if game_board[pos[0]] == symbol and game_board[pos[1]] == symbol and game_board[pos[2]] == symbol:
            return True
    return False

def board_full():
    return "-" not in game_board

def user_turn():
    while True:
        choice = input("Choose a position (1-9): ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < 9 and game_board[idx] == "-":
                game_board[idx] = "X"
                break
        print("Invalid choice, try again.")

def computer_turn():
    empty_cells = [i for i, val in enumerate(game_board) if val == "-"]
    move = random.choice(empty_cells)
    game_board[move] = "O"
    print("Computer played at position", move + 1)

print("=== TIC TAC TOE ===")
print("Player: X | Computer: O")

while True:
    show_board()
    user_turn()

    if is_winner("X"):
        show_board()
        print("🎉 Congratulations! You won.")
        break

    if board_full():
        show_board()
        print(" Match Draw.")
        break

    computer_turn()

    if is_winner("O"):
        show_board()
        print(" Computer wins.")
        break
