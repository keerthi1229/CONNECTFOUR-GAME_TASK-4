import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """Create an empty Connect Four board."""
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    """Drop a piece into the board."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Check if the column is valid for a new piece."""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """Get the next open row in the column."""
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    """Print the board in a readable format."""
    print(np.flip(board, 0))

def winning_move(board, piece):
    """Check if the current move is a winning move."""
    
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (board[r][c] == piece and board[r][c+1] == piece and
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True

    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and board[r+1][c] == piece and
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True

    
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (board[r][c] == piece and board[r+1][c+1] == piece and
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True

    
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (board[r][c] == piece and board[r-1][c+1] == piece and
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True

def play_connect_four():
    """Main function to play Connect Four."""
    board = create_board()
    game_over = False
    turn = 0

    print_board(board)

    while not game_over:
        
        if turn == 0:
            col = int(input("Player 1, make your selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print_board(board)
                    print("Player 1 wins!")
                    game_over = True

        
        else:
            col = int(input("Player 2, make your selection (0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print_board(board)
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)

        
        turn += 1
        turn %= 2


if __name__ == "__main__":
    play_connect_four()