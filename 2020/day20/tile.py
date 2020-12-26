class Tile:
	def __init__(self,_id,input_ary):
		self.id = _id
		self.orientation = 0
		self.edge_length = len(input_ary[0])

		self.edges = dict()
		edge0 = ""
		edge2 = ""
		for i in range(self.edge_length):
			edge0 += input_ary[i][-1]
			edge2 += input_ary[i][0]
		self.edges[0] = edge0
		self.edges[2] = edge2
		self.edges[1] = input_ary[-1]
		self.edges[3] = input_ary[0]

		self.neighbors = dict()
		self.permutations = set()
		for side in range(4):
			self.neighbors[side] = 0
			self.permutations.add(self.edges[side])
			self.permutations.add(self.edges[side][::-1])

	def rotate(self):
		new_edges = dict()
		new_edges[0] = self.edges[3]
		new_edges[1] = self.edges[0][::-1]
		new_edges[2] = self.edges[1]
		new_edges[3] = self.edges[2][::-1]
		self.edges = new_edges

	def flip(self):
		new_edges = dict()
		new_edges[0] = self.edges[0][::-1]
		new_edges[1] = self.edges[3]
		new_edges[2] = self.edges[2][::-1]
		new_edges[3] = self.edges[1]
		self.edges = new_edges

	def mirror(self):
		new_edges = dict()
		new_edges[0] = self.edges[2]
		new_edges[1] = self.edges[1][::-1]
		new_edges[2] = self.edges[0]
		new_edges[3] = self.edges[3][::-1]
		self.edges = new_edges

	def __str__(self):
		result = "Tile {}:\n".format(self.id)
		for i in range(self.edge_length):
			if i == 0:
				result += self.edges[3] + "\n"
			elif i == self.edge_length - 1:
				result += self.edges[1] + "\n"
			else:
				result += self.edges[2][i] + (" " * (self.edge_length - 2)) + self.edges[0][i] + "\n"
		result += "\n"
		return result