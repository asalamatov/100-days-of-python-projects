from turtle import Turtle
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class Cars():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.1
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(5)
        
        
    def speed_up(self):
        self.car_speed *= 0.7
        
    # def move(self):
    #     for car in self.all_cars:
    #         car.backward(5)

        
    # def create_car(self):
    #     new_car = Turtle()
    #     new_car.shape('square')
    #     new_car.shapesize(stretch_len=2, stretch_wid=1)
    #     new_car.penup()
    #     new_car.color(random.choice(COLORS))
    #     random_y = random.randint(-250, 250)
    #     new_car.goto(300, random_y)
    #     self.all_cars.append(new_car)
