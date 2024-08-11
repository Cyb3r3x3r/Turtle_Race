import random
from turtle import Turtle,Screen

color_list = ["red","yellow","green","purple","olive","cyan","blue","violet","orange","magenta"]
WIDTH,HEIGHT = 600,600
count = 0
def get_no_of_turtles():
    while True:
        count = input("Enter how many turtles you want to race(2-10): ")
        if count.isdigit():
            count = int(count)
            if 2<=count<=10:
                print("You have chosen to race " + str(count) + " turtles.")
                return count
            else:
                print("Try again and give the number in the given range.")
        else:
            print("Enter a numeric value.")

def race():                           #Function to start the race
    is_race_on = True
    while is_race_on:
        for t in turtle_list:
            distance = random.randrange(1,20)   #Get a random distance value for turtle to move
            t.forward(distance)             #Move the turtle
            x,y = t.pos()               #Check the position of the turtle
            if y>=HEIGHT//2-25:            #See if it has reached or crossed the finish line.
                print("The winner is " + t.pencolor() + " turtle.")
                if str(check_bet)==str(t.pencolor):
                    print("You predicted the right result. GREAT!!!")
                else:
                    print("Your prediction was wrong")
                is_race_on = False
        
def bet():
    print("----------TIME TO BET----------------")
    i = 1;
    race_color_list = []
    for t in turtle_list:
        print(str(i) + ". " + t.pencolor())
        i += 1
        race_color_list.append(t.pencolor())
    flag = True
    while flag:
        bet_choice =input(print("Which turtle you want to bet on? : "))
        if bet_choice in race_color_list:
            return bet_choice
            flag = False
        else:
            print("Please enter a valid color name.")  


turtles = get_no_of_turtles()
s1 = Screen()
s1.setup(WIDTH,HEIGHT)          #Setting the height and width of the screen
s1.title("Python Turtle Race")
x_space = WIDTH//(turtles+1)        #Dividing the screen to give equal spacing to turtles
turtle_list = []

for i in range(1,turtles+1):            #Creating the turtles
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2 + (i*x_space),-HEIGHT//2+10)
    turtle_list.append(new_turtle)

check_bet = bet()
race()    
   
s1.exitonclick()
