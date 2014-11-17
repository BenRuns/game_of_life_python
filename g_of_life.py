

def list_to_check(x,y):
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
	for item in list_to_check(x,y):		
		if item in cells:
			count += cells[item]
	return count 


def next_state(cells):
	next_state = {}
	for point in cells.keys():
		alive = cells[point] == 1
		neighbors = neighbors_count(point[0],point[1],cells)
		if not alive and neighbors == 3:
			next_state[point] = 1
		elif neighbors > 3 or neighbors < 2:
			next_state[point] = 0
	return next_state


def add_to_grid_alive(cells):
	to_check = []
	to_add = {}
	for item in cells.keys():
		checking = [ x for x in list_to_check(item[0],item[1]) if x not in to_check and x not in cells ]
		to_check += checking

	for item in to_check:
		if neighbors_count(item[0],item[1],cells) == 3:
			to_add[(item[0],item[1])] = 1
	return to_add


def tick(cells):
	changes = next_state(cells)
	expansions = add_to_grid_alive(cells)
	cells.update(changes)
	cells.update(expansions)



	

def print_grid( size, cells):
	grid = []
	for y in range(size):
		grid.append([])
		for x in range(size):
			grid[y].append(0)
	for point in cells.keys():
		if  0 <= point[0] < size and 0 <= point[1] < size:
			grid[point[1]][point[0]] = cells[point]  
	return grid






#testing

test_array_dict = {}


for x in range(6):
	for y in range(6):
		test_array_dict[(x,y)] = 0

test_array_dict[(1,2)] = 1
test_array_dict[(2,2)] = 1
test_array_dict[(3,2)] = 1
test_array_dict[(2,3)] = 1
test_array_dict[(3,3)] = 1
test_array_dict[(4,3)] = 1


for x in range(20):
	
	print '>>>>>>>>>>>>>>>>>>>>', x + 1


	for item in print_grid(6,test_array_dict)[::-1]:
		print item
	tick(test_array_dict)
	




