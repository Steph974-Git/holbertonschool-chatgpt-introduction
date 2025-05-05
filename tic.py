#!/usr/bin/python3

def print_board(board):
	print("\n")
	for i, row in enumerate(board):
		print(" | ".join(row))
		# Only print divider between rows, not after the last row
		if i < 2:
			print("-" * 9)
	print("\n")

def check_winner(board):
	# Check rows
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Check columns
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Check diagonals
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_board_full(board):
	"""Check if the board is full (tie condition)"""
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	current_player = "X"
	
	while True:
		print_board(board)
		print(f"Player {current_player}'s turn")
		
		# Get valid row and column input
		try:
			row = int(input("Enter row (0, 1, or 2): "))
			if row not in [0, 1, 2]:
				print("Invalid row! Please enter 0, 1, or 2.")
				continue
				
			col = int(input("Enter column (0, 1, or 2): "))
			if col not in [0, 1, 2]:
				print("Invalid column! Please enter 0, 1, or 2.")
				continue
		except ValueError:
			print("Invalid input! Please enter numbers only.")
			continue
			
		# Check if the cell is empty
		if board[row][col] != " ":
			print("That spot is already taken! Try again.")
			continue
			
		# Place the mark and check for win/tie
		board[row][col] = current_player
		
		if check_winner(board):
			print_board(board)
			print(f"Player {current_player} wins!")
			break
			
		if is_board_full(board):
			print_board(board)
			print("It's a tie!")
			break
			
		# Switch players
		current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
	print("Welcome to Tic-Tac-Toe!")
	tic_tac_toe()
