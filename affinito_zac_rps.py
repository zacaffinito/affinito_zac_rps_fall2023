# This file was created by: Zac Affinito

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image
Create CPU function that defines a computer choice
Compare computer choice with player choice and determine a winner
'''


# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = game_folder

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

RPS_choices = ("rock", "paper", "scissors")

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
# instantiate (create an instance of) the Turtle class for the rock
rock_instance = turtle.Turtle()
# add the rock image as a shape
screen.addshape(rock_image)
# attach the rock_image to the rock_instance
rock_instance.shape(rock_image)
# remove the pen option from the rock_instance so it doesn't draw lines when moved
rock_instance.penup()
# assign vars for rock position
rock_pos_x = -300
rock_pos_y = 0
# set the position of the rock_instance
rock_instance.setpos(rock_pos_x,rock_pos_y)


# setup the paper image using the os module as paper_image
paper_image = os.path.join(images_folder, 'paper.gif')
# instantiate (create an instance of) the Turtle class for the paper
paper_instance = turtle.Turtle()
# add the paper image as a shape
screen.addshape(paper_image)
# attach the paper_image to the paper_instance
paper_instance.shape(paper_image)
# remove the pen option from the paper_instance so it doesn't draw lines when moved
paper_instance.penup()
# assign vars for paper position
paper_pos_x = 0
paper_pos_y = 0
# set the position of the paper_instance
paper_instance.setpos(paper_pos_x,paper_pos_y)

# setup the scissors image using the os module as scissors_image
scissors_image = os.path.join(images_folder, 'scissors.gif')
# instantiate (create an instance of) the Turtle class for the scissors
scissors_instance = turtle.Turtle()
# add the scissors image as a shape
screen.addshape(scissors_image)
# attach the scissors_image to the scissors_instance
scissors_instance.shape(scissors_image)
# remove the pen option from the scissors_instance so it doesn't draw lines when moved
scissors_instance.penup()
# assign vars for scissors position
scissors_pos_x = 300
scissors_pos_y = 0
# set the position of the scissors_instance
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

# instantiate a generic turtle
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('deep pink')
text.hideturtle()

# hide that turtle
t.hideturtle()



# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    
    if x and y:

        if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
            return True
        else:
            return False

# function that passes through wn onlick - uses elif statements to create a trapdoor to find which image is clicked on
def mouse_pos(x, y):
    if collide(x, y, rock_instance, rock_w, rock_h):
        return 'rock'

    elif collide(x, y, paper_instance, paper_w, paper_h):
        return 'paper'

    elif collide(x, y, scissors_instance, scissors_w, scissors_h):
        return 'scissors'

"""
Make the game -
Define number of rounds
Assign computer choices to a random integer
allow computer to return option
allow player to pick
Compare computer's choice with player choice
decide a winner
"""
def gamerps(x, y):
    global rounds
    
    while rounds > 0:
        if rounds == 0:
            exitonclick()
        computer = RPS_choices[randint(0,2)]
        player = mouse_pos(x,y)
        if player == "rock" and computer == "scissors":
            print("player has won")
            break
        elif player == "rock" and computer == "paper":
            print("computer has won")
            break
        elif player == "rock" and computer == "rock":
            print("the game is a tie")
            break
        elif player == "paper" and computer == "rock":
            print("player has won")
            break
        elif player == "paper" and computer == "scissors":
            print("computer has won")
            break
        elif player == "paper" and computer == "paper":
            print("the game is a tie")
            break
        elif player == "scissors" and computer == "paper":
            print("player has won")
            break
        elif player == "scissors" and computer == "rock":
            print("computer has won")
            break
        elif player == "scissors" and computer == "scissors":
            print("the game is a tie")
            break


rounds = int(screen.textinput("Rounds", "How many rounds would you like to play?"))

screen.onclick(gamerps)

# runs mainloop for Turtle - required to be last
screen.mainloop()