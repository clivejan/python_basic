def print_board(board):
	print(f" {board['top_l']} | {board['top_m']} | {board['top_r']}\n"
		  f"---+---+---\n"
		  f" {board['mid_l']} | {board['mid_m']} | {board['mid_r']}\n"
		  f"---+---+---\n"
		  f" {board['low_l']} | {board['low_m']} | {board['low_r']} ")

the_board = {'top_l': ' ', 'top_m': ' ', 'top_r': ' ',
	         'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
             'low_l': ' ', 'low_m': ' ', 'low_r': ' '}

turn = 'X'

for i in range(9):
	print_board(the_board)

	move = input(f"Turn for {turn}. Move on which space: ")
	the_board[move] = turn

	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

print_board(the_board)
