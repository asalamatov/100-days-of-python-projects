from turtle import Turtle, Screen, colormode
from runner import Runner
from cars import Cars
from scoreboard import Scoreboard
import time
from random import randint

colormode(255)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Passing Capstone')
screen.tracer(0)


pet = Runner()
cars = Cars()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(pet.move, 'Up')
screen.onkey(pet.move, 'w')
screen.onkey(pet.move, '8')
screen.onkey(pet.move, 'space')

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    screen.update()
    cars.create_car()
    cars.move_cars()
    
    # Detect collision with cars
    for car in cars.all_cars:
        if car.distance(pet) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    
    if pet.ycor() > 280:
        pet.come_back()
        cars.speed_up()
        scoreboard.level_up()
        



screen.exitonclick()