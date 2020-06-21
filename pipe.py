import random
import pygame
class pipes:
	def __init__(self,screen,last):
		self.x = random.randint(last+200,last+300)
		self.top = random.randint(-370,-30)
		self.gap = random.randint(100,300)
		self.bottom = self.top + self.gap + 500
		self.speed = 3

		self.img = [pygame.image.load('assets/top.png').convert_alpha(),
					pygame.image.load('assets/bottom.png').convert_alpha()]

		self.screen = screen

	def show(self):
		self.screen.blit(self.img[0],(self.x,self.top))
		self.screen.blit(self.img[1],(self.x,self.bottom))

	def update(self):
		self.x -= self.speed

	def get_x(self):
		return self.x