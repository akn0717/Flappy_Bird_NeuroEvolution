import pygame
from NN import NeuralNetwork
import numpy as np

class FBird:
	def __init__(self, screen, brain = None):
		self.bird = pygame.Rect(65, 50, 50, 50)
		self.y = 708/2
		self.x = 64
		self.score = 0
		self.fitness = 0
		if brain!=None : self.brain = brain.copy()
		else: 
			self.brain = NeuralNetwork(4,4,1)

		self.frame = [pygame.image.load("assets/0.png").convert_alpha()]

		self.gravity = 1
		self.velocity = 0
		self.isdead = 0
		self.screen = screen

	def show(self):
		self.screen.blit(self.frame[0],(self.x,self.y))

	def update(self):
		self.score += 1
		self.velocity += self.gravity;
		self.y += self.velocity;

		if (self.y >= 708 or self.y<10):
			self.isdead = 1

	def hit(self, pip):
		if (pip.x-40 <= self.x) and (self.x<=pip.x+40):
			if (pip.top+500>=self.y or pip.bottom<=self.y):
				self.isdead = 1

	def mutate(self, MutationRate):
		self.brain.mutate(MutationRate)

	def up(self):
		self.velocity = -10

	def think(self, pip):
		inputs = np.array([[self.y],[(pip.top+500)],[pip.bottom],[(pip.x-40-self.x)]])
		outputs = self.brain.guess(inputs)
		if (outputs[0][0]>0.5): self.up()
		return outputs[0][0]






