import numpy as np
class NeuralNetwork:

	#initilization
	def __init__(self,numI,numH,numO):

		self.input_nodes = numI
		self.hidden_nodes = numH
		self.output_nodes = numO
		self.weights_ih = np.random.rand(numH,numI) * 2 - 1
		self.weights_ho = np.random.rand(numO,numH) * 2 - 1
		self.bias_h = np.random.rand(numH,1) * 2 - 1
		self.bias_o = np.random.rand(numO,1) * 2 - 1

	# guess data
	def guess(self,input):

		hidden = NeuralNetwork.sigmoid(np.add(np.matmul(self.weights_ih,input),self.bias_h))

		output = NeuralNetwork.sigmoid(np.add(np.matmul(self.weights_ho,hidden),self.bias_o))

		return output

	def copy(self):
		return self 

	def mutate(self, mutationRate):
		for i in range(self.hidden_nodes):
			for j in range(self.input_nodes):
				if (np.random.rand()<mutationRate):
					self.weights_ih[i][j] = np.random.rand() * 2 - 1 
		for i in range(self.output_nodes):
			for j in range(self.hidden_nodes):
				if (np.random.rand()<mutationRate):
					self.weights_ho[i][j] = np.random.rand() * 2 - 1
		for i in range(self.hidden_nodes):
			if (np.random.rand()<mutationRate):
				self.bias_h[i][0] = np.random.rand() * 2 - 1
		for i in range(self.output_nodes):
			if (np.random.rand()<mutationRate):
				self.bias_o[i][0] = np.random.rand() * 2 - 1

	# activation function!
	def sigmoid(x):
		return 1/ (1 + np.exp(-x))

	def dsigmoid(x):
		return x * (1-x)