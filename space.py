import turtle
import random
import os
import winsound

#setup screen 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

def draw_border():
	border_pen = turtle.Turtle()
	border_pen.speed(0)
	border_pen.penup()
	border_pen.color("white")
	border_pen.setposition(-300,-300)
	border_pen.pendown()
	border_pen.pensize(3)
	for side in range(4):
		border_pen.fd(600)
		border_pen.lt(90)
	border_pen.hideturtle()
def draw_player():
	global player
	player = turtle.Turtle()
	player.color("blue")
	player.shape("player.gif")
	player.penup()
	player.speed(0)
	player.setposition(0,-250)
	player.setheading(90)

def move_left():
	global player
	x = player.xcor()
	x -= player_speed
	if x > -280:
		player.setx(x)

def move_right():
	global player
	x = player.xcor()
	x += player_speed
	if x < 280:
		player.setx(x)

def draw_enemy():
	global enemies
	enemies = []
	#add enemies 
	for i in range(5):
		enemies.append(turtle.Turtle())
	for enemy in enemies:
		enemy.shape("invader.gif")
		enemy.color("red")
		enemy.penup()
		enemy.speed(0)
		x = random.randint(-200,200)
		y = random.randint(100,250)

		enemy.setposition(x,y)

def draw_bullet():
	global bullet,bullet_state
	bullet = turtle.Turtle()
	bullet.color("yellow")
	bullet.shape("triangle")
	bullet.penup()
	bullet.speed(0)
	bullet.setheading(90)
	bullet.shapesize(0.5,0.5)
	bullet.hideturtle()
	bullet_state = "ready"

def fire_bullet():
	global bullet_state
	#move the bullet
	if bullet_state == "ready":
		winsound.PlaySound("laser.wav",winsound.SND_ASYNC)
		os.system
		x = player.xcor()
		y = player.ycor()
		bullet.setposition(x,y+10)
		bullet.showturtle()
		bullet_state = "fire"

def is_collision(t1,t2):
	return t1.distance(t2) < 20

def draw_score():
	global score,score_pen
	score_pen = turtle.Turtle()
	score_pen.color("white")
	score_pen.speed(0)
	score_pen.penup()
	score_pen.setposition(-290,280)
	scorestring = "Score: %s" %score
	score_pen.write(scorestring,False,align="left")
	score_pen.hideturtle()

turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")
def main():
	draw_border()
	draw_player()
	draw_enemy()
	draw_bullet()
	global player_speed,enemy_speed,bullet_speed,bullet_state,score
	score=0
	draw_score()

	player_speed = 15
	enemy_speed = 2
	bullet_speed = 20

	while True:
		# move enemy 
		for enemy in enemies:
			x = enemy.xcor()
			x += enemy_speed
			enemy.setx(x)
			if(x > 280):
				enemy_speed *=-1
				for e in enemies:
					y =e.ycor()
					y -=40
					e.sety(y)

			if(x < -280):
				enemy_speed *= -1
				for e in enemies:
					y =e.ycor()
					y -=40
					e.sety(y)

			if is_collision(bullet,enemy):
				#reset bullet
				winsound.PlaySound("explosion.wav",winsound.SND_ASYNC)
				bullet.hideturtle()
				bullet_state = "ready"
				bullet.setposition(0,-400)
				#reset enemy
				enemy.setposition(-200,250)
				score += 10
				score_pen.clear()
				scorestring = "Score: %s" %score
				score_pen.write(scorestring,False,align="left")
			if is_collision(enemy,player):
				print("Game Over")
				break
		#FIRE
		if bullet_state == "fire":
			y =bullet.ycor()
			y+=bullet_speed
			bullet.sety(y)

		if bullet.ycor() > 275:
			bullet.hideturtle()
			bullet_state = "ready"

main()