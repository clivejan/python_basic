def turn_90_degree(grid):
	for x in range(len(grid[0])):
		for y in range(len(grid)):
			print(grid[y][x], end='')
		print()

grid = [['.', '.', '.', '.', '.', '.', ],
        ['.', 'O', 'O', '.', '.', '.', ],
        ['O', 'O', 'O', 'O', '.', '.', ],
        ['O', 'O', 'O', 'O', 'O', '.', ],
        ['.', 'O', 'O', 'O', 'O', 'O', ],
        ['O', 'O', 'O', 'O', 'O', '.', ],
        ['O', 'O', 'O', 'O', '.', '.', ],
        ['.', 'O', 'O', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', '.', ]]

turn_90_degree(grid)
