 
import math
import random
import pygame
class cube(object):
	def __init__(self,pos,dirx=0,diry=1,color=(255,0,0)):
		self.color=color
		self.pos=pos
		self.dirx=dirx
		self.diry=diry
	def draw(self,surface,eyes=False):
		step = width//rows
		i=self.pos[0]
		j=self.pos[1]
		pygame.draw.rect(surface,self.color,(i*step,j*step,step,step))
		if eyes:
			centre = step//2
			radius = 3
			circleMiddle = (i*step+centre-radius,j*step+8)
			circleMiddle2 = (i*step + step -radius*2, j*step+8)
			pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
			pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
	def move(self,dx,dy):
		self.dirx=dx
		self.diry=dy
		self.pos = (self.pos[0]+self.dirx,self.pos[1]+self.diry)

class snake(object):
	body = []
	turns = {}
	def __init__(self,color,pos):
		self.color=color
		self.head = cube(pos)
		self.body.append(self.head)
		self.dirx=0
		self.diry=1
	def draw(self,surface):
		for i,c in enumerate(self.body):
			if i == 0:
				c.draw(surface,True)
			else:
				c.draw(surface)
	def addCube(self):
		tail = self.body[-1]
		dx,dy = tail.dirx,tail.diry
		if dx == 1 and dy == 0:
			self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
		elif dx == -1 and dy == 0:
			self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
		elif dx == 0 and dy == 1:
			self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
		self.body[-1].dirx=dx
		self.body[-1].diry=dy

	def move(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			keys = pygame.key.get_pressed()
			for key in keys:
				if keys[pygame.K_LEFT]:
					self.dirx=-1
					self.diry=0
					self.turns[self.head.pos[:]] = [self.dirx,self.diry]
				elif keys[pygame.K_RIGHT]:
					self.dirx=1
					self.diry=0
					self.turns[self.head.pos[:]] = [self.dirx,self.diry]
				elif keys[pygame.K_UP]:
					self.dirx=0
					self.diry=-1
					self.turns[self.head.pos[:]] = [self.dirx,self.diry]
				elif keys[pygame.K_DOWN]:
					self.dirx=0
					self.diry=1
					self.turns[self.head.pos[:]] = [self.dirx,self.diry]

		for i,c in enumerate(self.body):
			p = c.pos[:]
			if p in self.turns:
				turn = self.turns[p]
				c.move(turn[0],turn[1])
				if(i == len(self.body)-1):
					self.turns.pop(p)
			else:
				if(c.dirx == -1 and c.pos[0]<=0): 
					c.pos=(rows-1,c.pos[1])
				elif(c.dirx==1 and c.pos[0]>=rows-1):
					c.pos=(0,c.pos[1])
				elif(c.diry == 1 and c.pos[1]>=rows-1):
					c.pos = (c.pos[0],0)
				elif(c.diry==-1 and c.pos[1] <= 0):
					c.pos = (c.pos[0],rows-1)
				else:
					c.move(c.dirx,c.diry)

def drawGrid(surface):
	global width,rows
	step = width//rows
	x=0
	y=0
	for i in range(rows):
		x = x+step
		y=y+step
		pygame.draw.line(surface,(255,255,255),(x,0),(x,width))
		pygame.draw.line(surface,(255,255,255),(0,y),(width,y))

def redrawWindow(surface):
	surface.fill((0,0,0))
	drawGrid(surface)
	snake.draw(surface)
	snack.draw(surface)
	pygame.display.update()

def randomSnack():
	positions = snake.body
	while True:
		x = random.randrange(rows)
		y = random.randrange(rows)
		if len(list(filter(lambda z:z.pos == (x,y),positions))) > 0:
			continue
		else:
			break
	return (x,y)

def main():
	global rows,width,snake,snack
	rows = 20
	width= 500
	win = pygame.display.set_mode((width,width))
	snake = snake((255,0,0),(10,10))
	snack = cube(randomSnack(),color=(0,255,0))
	clock = pygame.time.Clock()
	while True:
		pygame.time.delay(50)
		clock.tick(10)
		snake.move()
		if(snake.body[0].pos == snack.pos):
			snake.addCube()
			snack = cube(randomSnack(),color=(0,255,0))
		redrawWindow(win)
	pass

main()