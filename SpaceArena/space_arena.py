import turtle
import time
import random
import math

SCREEN_WIDTH=800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH+220,SCREEN_HEIGHT+20)
wn.title("Space Arean by amustafa")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()

class Game(object):
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.level = 1
		self.state = "splash"
	def start(self):
		self.state = "play"
	def start_level(self):
		sprites.clear()
		sprites.append(player)
		for missile in missiles:
			sprites.append(missile)
		for _ in range(self.level):
			x= random.randint(-self.width/2, self.width/2)
			y= random.randint(-self.height/2, self.height/2)
			dx = random.randint(-2, 2)/10
			dy = random.randint(-2, 2)/10
			sprites.append(Enemy(x,y,"square","red"))
			sprites[-1].dx=dx
			sprites[-1].dy = dy

		for _ in range(self.level):
			x= random.randint(-self.width/2,self.width/2)
			y= random.randint(-self.height/2,self.height/2)
			dx= random.randint(-2,2)/10
			dy= random.randint(-2,2)/10
			sprites.append(Powerup(x,y,"circle","blue"))
			sprites[-1].dx=dx
			sprites[-1].dy = dy

	def render_border(self,pen,x_offset,y_offset):
		pen.color("white")
		pen.width(3)
		pen.penup()
		left = -self.width/2.0 - x_offset
		right = self.width/2.0 - x_offset
		top = self.height/2.0 - y_offset
		bottom = -self.height/2.0 - y_offset
		pen.goto(left,top)
		pen.pendown()
		pen.goto(right,top)
		pen.goto(right,bottom)
		pen.goto(left,bottom)
		pen.goto(left,top)
		pen.penup()

	def render_info(self,pen,score,active_enemies=0):
		pen.color("blue")
		pen.penup()
		pen.goto(400,0)
		pen.shape("square")
		pen.setheading(90)
		pen.shapesize(10,32,None)
		pen.stamp()
		pen.color("white")
		pen.width(3)
		pen.goto(300,400)
		pen.pendown()
		pen.goto(300,-400)
		pen.penup()
		pen.color("white")
		char_pen.scale=1.0

		char_pen.draw_string(pen,"SPACE ARENA",400,270)
		char_pen.draw_string(pen,"SCORE {}".format(score),400,240)
		char_pen.draw_string(pen,"Enemies {}".format(active_enemies),400,210)
		char_pen.draw_string(pen,"Lives {}".format(player.lives),400,180)
		char_pen.draw_string(pen,"Level {}".format(game.level),400,150)

class Sprite(object):
	"""docstring for Sprite"""
	def __init__(self,x,y,shape,color):
		super(Sprite, self).__init__()
		self.x=x
		self.y=y
		self.shape=shape
		self.color= color
		self.dx = 0
		self.dy = 0
		self.heading = 0
		self.da = 0
		self.thrust = 0.0
		self.acceleration = 0.002
		self.health = 100
		self.max_health = 100
		self.width = 20
		self.height = 20
		self.state = "active"
		self.radar = 200
		self.max_dx = 5
		self.max_dy = 5
	def bounce(self,other):
		temp_dx = self.dx
		temp_dy = self.dy
		self.dx = other.dx
		self.dy = other.dy
		other.dx = temp_dx
		other.dy = temp_dy

	def is_collision(self,other):
		if self.x < other.x + other.width and\
			self.x + self.width > other.x and\
			self.y < other.y + other.height and\
			self.y + self.height > other.y:
			return True
		else:
			return False

	def border_check(self):
		if self.x > game.width/2-10:
			self.x = game.width/2-10
			self.dx *= -1

		elif self.x < -game.width/2+10:
			self.x = -game.width/2+10
			self.dx *= -1

		if self.y > game.height/2-10:
			self.y = game.height/2-10
			self.dy *= -1

		elif self.y < -game.height/2+10:
			self.y = -game.height/2+10
			self.dy *= -1

	def render(self, pen,x_offset,y_offset):
		if(self.state =="active"):
			pen.goto(self.x-x_offset,self.y-y_offset)
			pen.setheading(self.heading)
			pen.shape(self.shape)
			pen.color(self.color)
			pen.stamp()
			self.render_health_meter(pen,x_offset,y_offset)

	def render_health_meter(self,pen, x_offset,y_offset):
		pen.goto(self.x-10-x_offset,self.y+20-y_offset)
		pen.width(3)
		pen.pendown()
		pen.setheading(0)
		if(self.health/self.max_health < 0.3):
			pen.color("red")
		elif self.health/self.max_health < 0.7:
			pen.color("yellow")
		else:
			pen.color("green")
		pen.fd(20 * (self.health/self.max_health))
		if(self.health != self.max_health):
			pen.color("grey")
			pen.fd(20 * ((self.max_health - self.health)/self.max_health))
		pen.penup()

	def update(self):
		self.heading += self.da
		self.heading %= 360
		self.dx += math.cos(math.radians(self.heading))* self.thrust
		self.dy += math.sin(math.radians(self.heading))* self.thrust
		self.x += self.dx
		self.y += self.dy
		self.border_check()
class Player(Sprite):
	"""docstring for Player"""
	def __init__(self, x,y,shape,color):
		Sprite.__init__(self,x,y, shape,color)
		self.lives = 3
		self.score = 0
		self.heading = 0
		self.da = 1

	def rotate_left(self):
		self.da = 1

	def rotate_right(self):
		self.da = -1

	def stop_rotation(self):
		self.da = 0

	def render(self, pen, x_offset, y_offset):
		pen.shapesize(0.5,1.0,None)
		pen.goto(self.x-x_offset,self.y-y_offset)
		pen.setheading(self.heading)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.stamp()
		pen.shapesize(1.0,1.0,None)
		self.render_health_meter(pen,x_offset,y_offset)

	def accelerate(self):
		self.thrust += self.acceleration

	def decelerate(self):
		self.thrust = 0.0

	def fire(self):
		for missile in missiles:
			if missile.state == "ready":
				missile.fire(self.x,self.y,self.heading,self.dx,self.dy)
				break

	def update(self):
		if self.state =="active":
			self.heading += self.da
			self.heading %= 360
			self.dx += math.cos(math.radians(self.heading))* self.thrust
			self.dy += math.sin(math.radians(self.heading))* self.thrust
			self.x += self.dx
			self.y += self.dy
			self.border_check()
			if(self.health<=0):
				self.reset()
	def reset(self):
		self.x=0
		self.y=0 
		self.health = self.max_health
		self.dx = 0
		self.dy = 0
		self.lives -=1
class Missile(Sprite):
	"""docstring for Player"""
	def __init__(self, x,y,shape,color):
		Sprite.__init__(self,0,0, shape,color)
		self.state = "ready"
		self.thrust = 10
		self.max_fuel = 300
		self.fuel = self.max_fuel
		self.height = 4
		self.width= 4
	def fire(self,x,y,heading,dx,dy):
		if(self.state == "ready"):
			self.state= "active"
			self.x= x
			self.y= y
			self.heading=heading
			self.dx += math.cos(math.radians(self.heading))* self.thrust
			self.dy += math.sin(math.radians(self.heading))* self.thrust

	def update(self):
		if(self.state == "active"):
			self.fuel -= self.thrust
			if(self.fuel <= 0):
				self.reset()
			self.heading += self.da
			self.heading %= 360
			self.x += self.dx
			self.y += self.dy
			self.border_check()

	def reset(self):
		self.fuel = self.max_fuel
		self.dx = 0
		self.dy = 0
		self.state = "ready"

	def render(self, pen, x_offset, y_offset):
		if self.state == "active":
			pen.shapesize(0.2,0.2,None)
			pen.goto(self.x-x_offset,self.y-y_offset)
			pen.setheading(self.heading)
			pen.shape(self.shape)
			pen.color(self.color)
			pen.stamp()
			pen.shapesize(1,1,None)

class EnemyMissile(Sprite):
	"""docstring for Player"""
	def __init__(self, x,y,shape,color):
		Sprite.__init__(self,0,0, shape,color)
		self.state = "ready"
		self.thrust = 10
		self.max_fuel = 300
		self.fuel = self.max_fuel
		self.height = 4
		self.width= 4
	def fire(self,x,y,heading,dx,dy):
		if(self.state == "ready"):
			self.state= "active"
			self.x= x
			self.y= y
			self.heading=heading
			self.dx += math.cos(math.radians(self.heading))* self.thrust
			self.dy += math.sin(math.radians(self.heading))* self.thrust

	def update(self):
		if(self.state == "active"):
			self.fuel -= self.thrust
			if(self.fuel <= 0):
				self.reset()
			self.heading += self.da
			self.heading %= 360
			self.x += self.dx
			self.y += self.dy
			self.border_check()

	def reset(self):
		self.fuel = self.max_fuel
		self.dx = 0
		self.dy = 0
		self.state = "ready"

	def render(self, pen, x_offset, y_offset):
		if self.state == "active":
			pen.shapesize(0.2,0.2,None)
			pen.goto(self.x-x_offset,self.y-y_offset)
			pen.setheading(self.heading)
			pen.shape(self.shape)
			pen.color(self.color)
			pen.stamp()
			pen.shapesize(1,1,None)
class Enemy(Sprite):
	"""docstring for Player"""
	def __init__(self, x,y,shape,color):
		Sprite.__init__(self,0,0, shape,color)
		self.max_health = 20
		self.health = self.max_health
		self.type = random.choice(["hunter","mine","surv"])
		if self.type == "hunter":
			self.color ="red"
			self.shape = "square"
		elif self.type =="mine":
			self.color="orange"
			self.shape="square"
		elif self.type == "surv":
			self.color="pink"
			self.shape="square"
	def update(self):
		if self.state =="active":
			self.heading += self.da
			self.heading %= 360
			self.dx += math.cos(math.radians(self.heading))* self.thrust
			self.dy += math.sin(math.radians(self.heading))* self.thrust
			self.x += self.dx
			self.y += self.dy
			self.border_check()
			if(self.health<=0):
				self.reset()
			if self.type =="hunter":
				if self.x < player.x:
					self.dx += 0.01
				else:
					self.dx -= 0.01

				if self.y < player.y:
					self.dy += 0.01
				else:
					self.dy -= 0.01
			elif self.type == "mine":
				self.dx = 0
				self.dy = 0
			elif self.type == "surv":
				if self.x < player.x:
					self.dx += 0.01
				else:
					self.dx -= 0.01

				if self.y < player.y:
					self.dy += 0.01
				else:
					self.dy -= 0.01
			if self.dx > self.max_dx:
				self.dx = self.max_dx
			elif self.dx < - self.max_dx:
				self.dx = -self.max_dx

			if self.dy > self.max_dy:
				self.dy = self.max_dy
			elif self.dy < - self.max_dy:
				self.dy = -self.max_dy
	def reset(self):
		self.state = "inactive"

class Powerup(Sprite):
	"""docstring for Player"""
	def __init__(self, x,y,shape,color):
		Sprite.__init__(self,0,0, shape,color)

class Camera():
	def __init__(self,x,y):
		self.x= x
		self.y = y
	def update(self,x,y):
		self.x=x
		self.y=y

class Radar():
	def __init__(self,x,y,width,height):
		self.x= x
		self.y = y
		self.width = width
		self.height = height

	def render(self,pen, sprites):
		pen.setheading(90)
		pen.goto(self.x+self.width/2.0,self.y)
		pen.pendown()
		pen.color("white")
		pen.circle(self.width/2.0)
		pen.penup()

		for sprite in sprites:
			if sprite.state =="active":
				radar_x = self.x + (sprite.x-player.x)*(self.width/game.width)
				radar_y = self.y + (sprite.y-player.y)*(self.height/game.height)
				pen.goto(radar_x,radar_y)
				pen.shape(sprite.shape)
				pen.color(sprite.color)
				pen.setheading(sprite.heading)
				pen.shapesize(0.1,0.1,None)
				dist = ((player.x - sprite.x)**2 + (player.y-sprite.y)**2)**0.5
				if(dist < player.radar):
					pen.stamp()

class CharacterPen():
	def __init__(self,color="white",scale=1.0):
		self.color=color
		self.scale=scale
		self.chars={}
		self.chars["1"] = ((-5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
		self.chars["2"] = ((-5, 10),(5, 10),(5, 0), (-5, 0), (-5, -10), (5, -10))
		self.chars["3"] = ((-5, 10),(5, 10),(5, 0), (0, 0), (5, 0), (5,-10), (-5, -10))
		self.chars["4"] = ((-5, 10), (-5, 0), (5, 0), (2,0), (2, 5), (2, -10))
		self.chars["5"] = ((5, 10), (-5, 10), (-5, 0), (5,0), (5,-10), (-5, -10))
		self.chars["6"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (-5, 0))
		self.chars["7"] = ((-5, 10), (5, 10), (0, -10))
		self.chars["8"] = ((-5, 0), (5, 0), (5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0))
		self.chars["9"] = ((5, -10), (5, 10), (-5, 10), (-5, 0), (5, 0))
		self.chars["0"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
		self.chars["A"] = ((-5, -10), (-5, 10), (5, 10), (5, -10), (5, 0), (-5, 0))
		self.chars["B"] = ((-5, -10), (-5, 10), (3, 10), (3, 0), (-5, 0), (5,0), (5, -10), (-5, -10))
		self.chars["C"] = ((5, 10), (-5, 10), (-5, -10), (5, -10))
		self.chars["D"] = ((-5, 10), (-5, -10), (5, -8), (5, 8), (-5, 10))
		self.chars["E"] = ((5, 10), (-5, 10), (-5, 0), (0, 0), (-5, 0), (-5, -10), (5, -10))
		self.chars["F"] = ((5, 10), (-5, 10), (-5, 0), (5, 0), (-5, 0), (-5, -10))
		self.chars["G"] = ((5, 10), (-5, 10), (-5, -10), (5, -10), (5, 0), (0, 0))
		self.chars["H"] = ((-5, 10), (-5, -10), (-5, 0), (5, 0), (5, 10), (5, -10))
		self.chars["I"] = ((-5, 10), (5, 10), (0, 10), (0, -10), (-5, -10), (5, -10))
		self.chars["J"] = ((5, 10), (5, -10), (-5, -10), (-5, 0))   
		self.chars["K"] = ((-5, 10), (-5, -10), (-5, 0), (5, 10), (-5, 0), (5, -10))
		self.chars["L"] = ((-5, 10), (-5, -10), (5, -10))
		self.chars["M"] = ((-5, -10), (-3, 10), (0, 0), (3, 10), (5, -10))
		self.chars["N"] = ((-5, -10), (-5, 10), (5, -10), (5, 10))
		self.chars["O"] = ((-5, 10), (5, 10), (5, -10), (-5, -10), (-5, 10))
		self.chars["P"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0))
		self.chars["Q"] = ((5, -10), (-5, -10), (-5, 10), (5, 10), (5, -10), (2, -7), (6, -11))
		self.chars["R"] = ((-5, -10), (-5, 10), (5, 10), (5, 0), (-5, 0), (5, -10))
		self.chars["S"] = ((5, 8), (5, 10), (-5, 10), (-5, 0), (5, 0), (5, -10), (-5, -10), (-5, -8))
		self.chars["T"] = ((-5, 10), (5, 10), (0, 10), (0, -10)) 
		self.chars["V"] = ((-5, 10), (0, -10), (5, 10)) 
		self.chars["U"] = ((-5, 10), (-5, -10), (5, -10), (5, 10)) 
		self.chars["W"] = ((-5, 10), (-3, -10), (0, 0), (3, -10), (5, 10))   
		self.chars["X"] = ((-5, 10), (5, -10), (0, 0), (-5, -10), (5, 10))   
		self.chars["Y"] = ((-5, 10), (0, 0), (5, 10), (0,0), (0, -10))   
		self.chars["Z"] = ((-5, 10), (5, 10), (-5, -10), (5, -10))   
		self.chars["-"] = ((-3, 0), (3, 0)) 
	def draw_string(self,pen,str,x,y):
		pen.width(2)
		pen.color(self.color)

		x-= 15*self.scale * ((len(str)-1)/2)
		for char in str:
			self.draw_chars(pen,char,x,y)
			x += 15 * self.scale

	def draw_chars(self,pen,char,x,y):
		scale = self.scale
		char = char.upper()
		if char in self.chars:
			pen.penup()
			xy=self.chars[char][0]
			pen.goto(x+xy[0]*scale,y+xy[1]*scale)
			pen.pendown()
			for i in range(1,len(self.chars[char])):
				xy=self.chars[char][i]
				pen.goto(x+xy[0]*scale,y+xy[1]*scale)
			pen.penup()

char_pen = CharacterPen("red",3)
char_pen.draw_string(pen,"SPACE_ARENA",0,160)
char_pen.scale=1
char_pen.draw_string(pen,"BY AMUSTAFA", 0, 100)

char_pen.draw_string(pen,"Player", -150,-20)
#create sprites
game = Game(700,500)

player = Player(100,100,"triangle", "white")
player.dx =0.01

missiles= []
for _ in range (30):
	missiles.append(Missile(0,100,"circle","yellow"))

missiles.append(EnemyMissile(0,100,"circle","red"))

camera=Camera(player.x,player.y)
radar = Radar(400,-200,200,200)

# powerup = Powerup(0,-100,"circle", "blue")
# powerup.dy = 0.01

# powerup2 = Powerup(-100,-100,"circle", "blue")
# powerup2.dy = 0.01

#sprites list
sprites = []
game.start_level()

#kb binding
wn.listen()
wn.onkeypress(player.rotate_left,"Left")
wn.onkeypress(player.rotate_right,"Right")

wn.onkeyrelease(player.stop_rotation,"Left")
wn.onkeyrelease(player.stop_rotation,"Right")

wn.onkeypress(player.accelerate,"Up")
wn.onkeyrelease(player.decelerate,"Up")

wn.onkeypress(player.fire,"space")

wn.onkeypress(game.start,"s")

while True:
	if game.state == "splash":
		wn.update()
	else:
		pen.clear()
		for sprite in sprites:
			sprite.update()

		for sprite in sprites:
			if isinstance(sprite, Enemy) and sprite.state == "active":
				if player.is_collision(sprite):
					sprite.health -= 10
					player.health -= 10
					player.bounce(sprite)
				for missile in missiles:
					if missile.state =="active" and missile.is_collision(sprite):
						sprite.health -= 10
						missile.reset()

			if isinstance(sprite,Powerup):
				if player.is_collision(sprite):
					player.bounce(sprite)
				for missile in missiles:
					if missile.state =="active" and missile.is_collision(sprite):
						sprite.x = -100
						sprite.y = -100
						missile.reset()

		for sprite in sprites:
			sprite.render(pen,camera.x+100,camera.y)

		game.render_border(pen,camera.x+100,camera.y)

		end_level = True
		for sprite in sprites:
			if isinstance(sprite, Enemy) and sprite.state == "active":
				end_level= False
		if end_level:
			game.level += 1
			game.start_level ()

		camera.update(player.x,player.y)

		game.render_info(pen,0,0)
		radar.render(pen,sprites)
		wn.update()
