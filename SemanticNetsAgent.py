import copy
import time

class AnimalsState:

	def __init__(self, wolves, sheep):
		self.wolves = wolves
		self.sheep = sheep

	def is_valid(self):
		if self.sheep >= 0 and self.wolves  >= 0 \
				   and (self.sheep == 0 or self.sheep >= self.wolves):
			return True
		else:
			return False

	def __hash__(self):
		return hash((self.wolves, self.sheep)) ### hash function

class BoatState:

	def __init__(self, boat):
		self.boat = boat
		self.parent = None

	# def __hash__(self):
	# 	return hash((self.boat, self.parent))

	def generate_neighbors(self):
		neighbors = []
		temp_state = copy.deepcopy(self.boat)


		if self.boat['position'] == 'L': ### define next states and current states for boat
			current_pos = 'L'
			across_current_pos = 'R'
		elif self.boat['position'] == 'R':
			current_pos = 'R'
			across_current_pos = 'L'

			## move two wolves, then two sheep, etc
			## then 

		if temp_state[current_pos].wolves >= 2:   
			temp_state[current_pos].wolves = temp_state[current_pos].wolves - 2
			temp_state[across_current_pos].wolves = temp_state[across_current_pos].wolves + 2
			temp_state['position'] = across_current_pos
			if temp_state[current_pos].is_valid() and temp_state[across_current_pos].is_valid():  ### check if it's illegal
				boat_state = BoatState(temp_state) ## create a new state using the temp state if it is legal
				boat_state.parent = self ## parent inherets current
				neighbors.append(boat_state) ### save in list

		temp_state = copy.deepcopy(self.boat)
		if temp_state[current_pos].sheep >= 2:
			temp_state[current_pos].sheep = temp_state[current_pos].sheep - 2
			temp_state[across_current_pos].sheep = temp_state[across_current_pos].sheep + 2
			temp_state['position'] = across_current_pos
			if temp_state[current_pos].is_valid() and temp_state[across_current_pos].is_valid():
				boat_state = BoatState(temp_state)
				boat_state.parent = self
				neighbors.append(boat_state)

		temp_state = copy.deepcopy(self.boat)
		if temp_state[current_pos].wolves >= 1:
			temp_state[current_pos].wolves = temp_state[current_pos].wolves - 1
			temp_state[across_current_pos].wolves = temp_state[across_current_pos].wolves + 1
			temp_state['position'] = across_current_pos
			if temp_state[current_pos].is_valid() and temp_state[across_current_pos].is_valid():
				boat_state = BoatState(temp_state)
				boat_state.parent = self
				neighbors.append(boat_state)

		temp_state = copy.deepcopy(self.boat)
		if temp_state[current_pos].sheep >= 1:
			temp_state[current_pos].sheep = temp_state[current_pos].sheep - 1
			temp_state[across_current_pos].sheep = temp_state[across_current_pos].sheep + 1
			temp_state['position'] = across_current_pos
			if temp_state[current_pos].is_valid() and temp_state[across_current_pos].is_valid():
				boat_state = BoatState(temp_state)
				boat_state.parent = self
				neighbors.append(boat_state)

		temp_state = copy.deepcopy(self.boat)
		if temp_state[current_pos].sheep >= 1 and temp_state[current_pos].wolves >= 1:
			temp_state[current_pos].sheep = temp_state[current_pos].sheep - 1
			temp_state[across_current_pos].sheep = temp_state[across_current_pos].sheep + 1
			temp_state[current_pos].wolves = temp_state[current_pos].wolves - 1
			temp_state[across_current_pos].wolves = temp_state[across_current_pos].wolves + 1
			temp_state['position'] = across_current_pos
			if temp_state[current_pos].is_valid() and temp_state[across_current_pos].is_valid():
				boat_state = BoatState(temp_state)
				boat_state.parent = self
				neighbors.append(boat_state)
		return neighbors  ## returns potential neighbors to be searched through


def goal(state):
	if state.boat['L'].sheep == 0 and state.boat['L'].wolves == 0 and state.boat['position'] == 'R':
		return True
	else:
		return False




def bfs(current): 
	end = AnimalsState(0, 0)
	root = {'L': current, 'R': end, 'position': 'L'}
	seen = set()
	q = list()
	queue = [BoatState(root)]
	path = []
	count = 0
	for state in queue:
		count+=1
		if goal(state):
			path = [state]
			return state
			while state.parent:
				path.insert(0, state.parent)
				state = state.parent
			break
		if(count > 15000):
			return []
		queue.extend(state.generate_neighbors())
	return []



def is_valid_state(state):
	if state != None:
			if state.sheep >= state.wolves \
			and (state.sheep + state.wolves) > 0:
				return True

	else:
		return False

class SemanticNetsAgent:
	def __init__(self):
		#If you want to do any initial processing, add it here.
		pass

	def solve(self, initial_sheep, initial_wolves):
		#Add your code here! Your solve method should receive
		#the initial number of sheep and wolves as integers,
		#and return a list of 2-tuples that represent the moves
		#required to get all sheep and wolves from the left
		# start = time.time()

		moves = list()
		initial_state = AnimalsState(initial_wolves,initial_sheep)
		if is_valid_state(initial_state):
			print('Solving...')
			state = bfs(initial_state)
			if(state == []):
				return []
			list1 = list()
			list2=list()
			path = [state]
			if(type(state) is tuple):
				return (0,0)
			else:		
				while state.parent:
					state = state.parent
					path.append(state)
				for p in reversed(path):

						left = (p.boat['L'].sheep,p.boat['L'].wolves)
						right = (p.boat['R'].sheep,p.boat['R'].wolves)
		

						sheep = p.boat['L'].sheep
						wolves = p.boat['L'].wolves

						list1.append(sheep)
						list2.append(wolves)

						sheep_change =  [abs(x - list1[i - 1]) for i, x in enumerate(list1)][1:]
						wolves_change =  [abs(x - list2[i - 1]) for i, x in enumerate(list2)][1:]

				moves = list(zip(sheep_change,wolves_change))

		else:
				moves = []
		
		return moves


t = SemanticNetsAgent()
# print(t.solve(4,4))

 