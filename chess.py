import random

# Initialize the board with ASCII pieces
def initialize_board():
    board = [
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
    ]
    return board

# Display the board in the console
def display_board(board):
    print("  a b c d e f g h")
    print(" +-----------------+")
    for i, row in enumerate(board):
        print(f"{8-i}| {' '.join(row)} |")
    print(" +-----------------+")

# Translate board position to array indices
def pos_to_index(pos):
    col, row = pos
    return 8 - int(row), ord(col) - ord('a')

# Move a piece on the board
def move_piece(board, start_pos, end_pos):
    start_row, start_col = pos_to_index(start_pos)
    end_row, end_col = pos_to_index(end_pos)
    piece = board[start_row][start_col]
    board[start_row][start_col] = ' '  # Empty the start position
    board[end_row][end_col] = piece    # Place the piece at the end position

# Get random move for the computer
def get_random_move(board, is_white_turn):
    while True:
        start_row = random.randint(0, 7)
        start_col = random.randint(0, 7)
        end_row = random.randint(0, 7)
        end_col = random.randint(0, 7)
        piece = board[start_row][start_col]
        # Select only white or black pieces for respective turns
        if (is_white_turn and piece in '♙♖♘♗♕♔') or (not is_white_turn and piece in '♟♜♞♝♛♚'):
            if board[end_row][end_col] == ' ' or board[end_row][end_col].islower() != piece.islower():
                return (start_row, start_col), (end_row, end_col)

# Main game loop
def play_game():
    board = initialize_board()
    is_white_turn = True

    while True:
        display_board(board)
        if is_white_turn:
            print("Player's turn (white)")
            try:
                start_pos = input("Enter the start position (e.g., e2): ")
                end_pos = input("Enter the end position (e.g., e4): ")
                move_piece(board, start_pos, end_pos)
            except Exception as e:
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn (black)")
            start, end = get_random_move(board, is_white_turn)
            start_pos = chr(start[1] + ord('a')) + str(8 - start[0])
            end_pos = chr(end[1] + ord('a')) + str(8 - end[0])
            move_piece(board, start_pos, end_pos)
            print(f"Computer moved from {start_pos} to {end_pos}")

        # Toggle turn
        is_white_turn = not is_white_turn

# Run the game
play_game()
