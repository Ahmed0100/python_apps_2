import turtle
import time
import random
block_size = 20
delay = .1
wn = turtle.Screen()
wn.title("Snake by amustafa")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #turns of screen update
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("score: 0 high score: 0",align="center", font=("Courier",24,"normal"))

score = 0
high_score = 0

def go_up():
	if head.direction != "down":
		head.direction = "up"
def go_down():
	if head.direction != "up":
		head.direction = "down"
def go_left():
	if head.direction != "right":
		head.direction = "left"
def go_right():
	if head.direction != "left":
		head.direction = "right"

def move():
	y = head.ycor()
	x = head.xcor()
	if head.direction == "up":
		head.sety(y + block_size)
	elif head.direction == "down":
		head.sety(y - block_size)
	elif head.direction == "left":
		head.setx(x - block_size)
	elif head.direction == "right":
		head.setx(x + block_size)

def main():

	wn.listen()
	wn.onkeypress(go_up, "w")
	wn.onkeypress(go_down, "s")
	wn.onkeypress(go_left, "a")
	wn.onkeypress(go_right, "d")
	global score,high_score

	while True:
		wn.update()
		#check for borders
		if head.xcor() > 290 or head.xcor() <-290 or head.ycor() <-290 or head.ycor()>290:
			time.sleep(0.1)
			head.goto(0,0)
			# head.direction="stop"
			for segment in segments:
				segment.goto(1000,1000)
			segments.clear()
			score = 0
			pen.clear()
			pen.write("score: {} high score: {}".format(score,high_score), align="center", font=("Courier",24,"normal"))

		#Eat food 
		if head.distance(food) < 20:
			x= random.randint(-290,290)
			y= random.randint(-290,290)
			food.goto(x,y)
			score +=10
			if score > high_score:
				high_score = score
			pen.clear()
			pen.write("score: {} high score: {}".format(score,high_score), align="center", font=("Courier",24,"normal"))
			#add a segment 
			new_segment = turtle.Turtle()
			new_segment.speed(0)
			new_segment.shape("square")
			new_segment.color("gray")
			new_segment.penup()
			segments.append(new_segment)
		#Move the end segments first
		for index in range(len(segments)-1,0,-1):
			x = segments[index-1].xcor()
			y = segments[index-1].ycor()
			segments[index].goto(x,y)
		#move segment 0 to the head
		if(len(segments)>0):
			x = head.xcor()
			y=head.ycor()
			segments[0].goto(x,y)

		move()
		#check for self eat
		for segment in segments:
			if segment.distance(head)<20:
				time.sleep(.1)
				head.goto(0,0)
				# head.direction="stop"
				for segment in segments:
					segment.goto(1000,1000)
				segments.clear()
				score = 0
				pen.clear()
				pen.write("score: {} high score: {}".format(score,high_score), align="center", font=("Courier",24,"normal"))

		time.sleep(delay)

main()
wn.mainloop()