# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

color_list=["red","yellow"]
count = 0

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("arrow")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for number in range(START_LENGTH) :
    x_pos=snake.pos()[0]#Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    yasa_food = snake.stamp()
    stamp_list.append(yasa_food)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!          
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 1
DOWN = 0
LEFT = 2
RIGHT = 3
direction = None
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

b=turtle.clone()
b.pensize(6)
b.pencolor('purple')
b.penup()
b.goto(300,300)
b.pendown()
b.goto(300,-300)
b.goto(-300,-300)
b.goto(-300,300)
b.goto(300,300)
def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
   
    print("You pressed the up key!")

direction = UP
    
def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
   
    print("You pressed the down key!")

direction = RIGHT    

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
   
    print("You pressed the right key!")
    
direction = UP

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    
    print("You pressed the left key!")


#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=(LEFT_EDGE/SQUARE_SIZE)+1
    max_x=(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=(DOWN_EDGE/SQUARE_SIZE)+1
    max_y=(UP_EDGE/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food.goto(food_x, food_y)
    food_pos.append((food_x, food_y))
    stamp_id = food.stamp()
    food_stamps.append(stamp_id)
snake.color("red")
turtle.bgcolor("black")
def move_snake():
    global count
    count+=1

    
    snake.color(color_list[count%2])
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos- SQUARE_SIZE)
        print('you moved down')
    elif direction==UP:
        snake.goto(x_pos, y_pos+ SQUARE_SIZE)
        print('you moved up')
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    
    if snake.pos() in pos_list[0:-1] :
        print('you ate yourself game over!')
        quit()
    #if snake.pos() in food_pos
    
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
     
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")

       
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
        
        
    #HINT: This if statement may be useful for Part 8

    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
  

    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_x_pos<= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    elif new_y_pos>= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()

    elif new_y_pos<= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()
#starter_code.py
#Displaying starter_code.py.
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos :
    
    food.goto(this_food_pos)
    food_id=food.stamp()
    food_stamps.append(food_id)
