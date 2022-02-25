# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
import random

def setup():
    global vehicle
    global food
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    global d
    d = 25
    global x 
    x = random.randint(0, width)
    global y 
    y = random.randint(0, height)
    food = Food(x, y, 0)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display()
    food.display()
    # vehicle.seek(PVector(x, y))
    vehicle.boundaries(d)
    vehicle.arrive(PVector(x, y))
    vectorFood = food.getFoodPosition()
    vectorVehicle = vehicle.getVehiclePosition()
    if ((vectorFood.x == vectorVehicle.x) and (vectorFood.y == vectorVehicle.y)):
        newX = random.randint(0, width)
        newY = random.randint(0, height)
        food.spawn(PVector(newX, newY))
