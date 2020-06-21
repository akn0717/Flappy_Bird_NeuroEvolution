import pygame
from bird import FBird
from pipe import pipes
import numpy as np
import random

chim = []
ong = []
total = 200
last = 300
max_score = -1
gen = 0
pygame.init()
screen = pygame.display.set_mode((400,708))
#screen.blit(screeb,(0,0))
clock = pygame.time.Clock()
textsurface = pygame.font.SysFont('Comic Sans MS', 30).render('Score', False,(0,0,0))

def round(x):
	if (float(x-int(x))>=0.5): return int(x)+1
	return int(x)

def pickone(savedchim):
	#index = random.choice(savedchim)
	index = 0
	r = np.random.rand()
	while (r>0):
		r -= savedchim[index].fitness;
		index+=1
	index-=1
	print(savedchim[index].fitness)
	child = FBird(screen, savedchim[index].brain)	
	return child

def mix(a,b):
	temp = FBird(screen)
	for i in range(a.brain.hidden_nodes):
		for j in range(a.brain.input_nodes):
			if (np.random.rand()<=0.5): temp.brain.weights_ih[i][j] = a.brain.weights_ih[i][j]
			else : temp.brain.weights_ih[i][j] = b.brain.weights_ih[i][j]
	for i in range(a.brain.output_nodes):
		for j in range(a.brain.hidden_nodes):
			if (np.random.rand()<=0.5): temp.brain.weights_ho[i][j] = a.brain.weights_ho[i][j]
			else : temp.brain.weights_ho[i][j] = b.brain.weights_ho[i][j]
	for i in range(a.brain.hidden_nodes):
		if (np.random.rand()<=0.5): temp.brain.bias_h[i][0] = a.brain.bias_h[i][0]
		else: temp.brain.bias_h[i][0] = b.brain.bias_h[i][0]
	for i in range(a.brain.output_nodes):
		if (np.random.rand()<=0.5): temp.brain.bias_o[i][0] = a.brain.bias_o[i][0]
		else: temp.brain.bias_o[i][0] = b.brain.bias_o[i][0]
	return temp

def generate():
	calculateFitness()
	fit = []
	savedchim = []
	global chim
	for i in range(total):
		parent_1 = pickone(chim)
		parent_2 = pickone(chim)
		child = mix(parent_1,parent_2)
		savedchim.append(child)
	chim = savedchim
	for i in range(total):
		chim[i].mutate(0.1)

def calculateFitness():
	s = 0
	global chim
	for i in chim:
		s += i.score
	for i in range(len(chim)):
		if s != 0:
			chim[i].fitness = chim[i].score / s
		else: chim[i].fitness = 0

def display(text, text_x, text_y, size):
	textsurface = pygame.font.SysFont('Comic Sans MS', size).render(text, False,(0,0,0))
	screen.blit(textsurface,(text_x,text_y))


def draw():
	screen.fill((255,255,255))
	cur = 0
	next_pipe = 0
	gen_score = 0
	for i in range(len(ong)):
		if ong[i].get_x()<=-100:
			cur = i
			if cur<len(ong):
				next_pipe = cur + 1
			else: next_pipe = cur
	for i in range(cur,len(ong)):
		for j in chim:
			j.hit(ong[i])
		ong[i].update()
		ong[i].show()
	for i in chim:
		if i.isdead==0:
			i.think(ong[next_pipe])
			if gen_score<i.score: gen_score = i.score
			i.update()
			i.show()
	global max_score
	if gen_score>max_score: max_score = gen_score
	display('Generation: ',0,0,20)
	display(str(gen), 120,0,20)
	display('Best score: ',0,30,20)
	display(str(max_score),120,30,20)
	display('This Generation Best Score: ',0,60,20)
	display(str(gen_score),280,60,20)
	pygame.display.update()

def setup():
	ong.clear()
	last = 300

	for i in range(100):
		ong.append(pipes(screen,last))
		last = ong[len(ong)-1].get_x()

	global gen
	if gen>=1: generate()
	gen+=1
	crashed = False
	while not crashed:
		clock.tick(60)
		crashed = True
		for i in chim:
			if i.isdead == 0: crashed = False
		draw()

end = True
for i in range(total):
	chim.append(FBird(screen))
while end:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = False
	setup()

pygame.quit()
quit
