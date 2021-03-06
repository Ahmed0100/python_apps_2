import turtle 
import time
import random
wn = turtle.Screen()
wn.title("TETRIS by amustafa")
wn.bgcolor("white")
wn.setup(width=600,height=800)
wn.tracer(0)
delay = .05
block_size=20
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")

grid = [

	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

class Shape(object):
	def __init__(self):
		self.x = 5
		self.y = 0
		self.color = random.randint(1,7)
		square = [	[1,1],
				[1,1]]

		hor_line = [[1,1,1,1]]

		ver_line = [[1],
				[1],
				[1],
				[1]]

		left_l = [	[1,0,0,0],
				[1,1,1,1]]

		right_l = [	[0,0,0,1],
				[1,1,1,1]]

		left_s = [	[1,1,0],
				[0,1,1]]

		right_s = [	[0,1,1],
				[1,1,0]]

		t = 	[	[0,1,0],
				[1,1,1]]

		shapes = [square, hor_line, ver_line, left_l, right_l,left_s,right_s,t]

		self.shape = random.choice(shapes)

		self.height= len(self.shape)
		self.width = len(self.shape[0])

	def rotate(self,grid):
		self.erase_shape(grid)
		rotated_shape = []
		for x in range(len(self.shape[0])):
			new_row = []
			for y in range(len(self.shape) -1,-1,-1):
				new_row.append(self.shape[y][x])
			rotated_shape.append(new_row)
		right_side = self.x + len(rotated_shape[0])
		if(right_side < len(grid[0])):
			self.shape= rotated_shape
			self.height= len(self.shape)
			self.width = len(self.shape[0])

	def move_left(self, grid):
		if self.x >0 and grid[self.y][self.x-1]==0:
			self.erase_shape(grid)
			self.x -= 1

	def move_right(self, grid):
		if self.x < 12 - self.width and grid[self.y][self.x+self.width]==0:
			self.erase_shape(grid)
			self.x += 1

	def erase_shape(self,grid):
		for y in range(self.height):
			for x in range(self.width):
				if self.shape[y][x] == 1:
					grid[self.y+y][self.x + x] = 0

	def draw_shape(self,grid):
		for y in range(self.height):
			for x in range(self.width):
				if self.shape[y][x] == 1:
					grid[self.y+y][self.x + x] = self.color

	def can_move(self,grid):
		result = True
		for x in range(self.width):
			if self.y + self.height > 23:
				result = False
			elif grid[self.y + self.height][self.x + x]!=0:
				result = False
		return result

def draw_grid(pen, grid):
	pen.clear()
	top_left_x = -110
	top_left_y = 230
	colors = ["black", "lightblue", "blue", "orange", "green", "purple","yellow", "red"]
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			screen_x = top_left_x + (j*block_size)
			screen_y = top_left_y - (i*block_size)
			color_num = colors[grid[i][j]]
			pen.color(color_num)
			pen.goto(screen_x,screen_y)
			pen.stamp()

def draw_score(pen,score):
	pen.goto(-50,300)
	pen.write("Score: {}".format(score), move=False, align="left", font=("Arial",20,"normal"))


def check_grid(grid):
	global score
	y = 23
	while y>0:
		is_full = True
		for x in range(0,12):
			if grid[y][x] == 0:
				is_full =False
				y-=1
				break
		if is_full:
			score += 10
			for copy_y in range(y,0,-1):
				for copy_x in range(0,12):
					grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

#Main game loop
def main():
	global shape, score
	score = 0
	shape = 0

	draw_grid(pen,grid)

	wn.listen()
	wn.onkey( lambda: shape.move_left(grid),"a")
	wn.onkey( lambda: shape.move_right(grid),"d")
	wn.onkey( lambda: shape.rotate(grid),"space")

	shape = Shape()
	grid[shape.y][shape.x] = shape.color

	while True:
		wn.update()
		if shape.can_move(grid):
			#erase current shape
			shape.erase_shape(grid)
			#move shape
			shape.y += 1
			#draw shape
			shape.draw_shape(grid)
		else:
			shape = Shape()
			check_grid(grid)		#check is bottom row is full
		draw_score(pen,score)
		draw_grid(pen,grid)
		time.sleep(delay)
main()
wn.mainloop()