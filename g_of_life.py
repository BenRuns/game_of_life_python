

def neighbors(x,y):
	return	[(x + 1, y),
			 (x - 1, y),
			 (x +1, y +1 ),
			 (x -1, y -1 ),
			 (x +1, y -1 ),
			 (x -1, y +1 ),
			 (x, y+1),
			 (x, y-1)]

def neighbors_count(x,y,cells):
	count = 0
	for item in neighbors(x,y):		
		if item in cells:
			count += 1
	return count 


def next_state(cells):
	next_state = []
	for point in cells:
		count = neighbors_count(point[0],point[1], cells)
		if 2 <= count <= 3:
			next_state.append(point)
		for xy in neighbors(point[0],point[1]):
			if neighbors_count(xy[0],xy[1], cells) == 3 and xy not in next_state:
				next_state.append(xy)

	return set(next_state)


def grid( size, cells):
	grid = []
	for y in range(size):
		grid.append([])
		for x in range(size):
			grid[y].append(".")
	for point in cells:
		if  0 <= point[0] < size and 0 <= point[1] < size:
			shape = "#"
			grid[point[1]][point[0]] = shape
	return grid



def print_life_cycle( cycles, cells ,size ):
	inputs = set(cells)
	for cycle in range(cycles):

		for item in grid( size, inputs )[::-1]:
			print item 
		print "*******"
		inputs = next_state(inputs)
	return inputs
	





inputs = [(2,15),(2,14),(2,13),(1,13),(0,14)]


print print_life_cycle( 600, inputs , 20 )







