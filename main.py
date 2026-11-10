class Robot:
    def __init__(self):
        self.name = "Neon"
        self.x = 0
        self.y = 0
        self.direction = "north"
        self.energy = 100
import random
Neon = Robot()
obstacles = [(random.randint(-5,5),random.randint(-5,5)),(random.randint(-5,5),random.randint(-5,5)),(random.randint(-5,5),random.randint(-5,5))]
charge = [(-3,-4),(-2,3),(3,-2)]
import pygame
def move_east(self):
    if self.x >= 5:
        print()
        print("Boundary Reached")
        return False
    if not energy_check(self):
        return False
    if not obstacle_detect(self.x + 1,self.y):
        return False
    self.x = self.x + 1 
    self.direction = "east"
    self.energy = self.energy - 5
    energy_charge(self)
    return True
def move_west(self):
    if self.x <= -5:
        print()
        print('Boundary Reached')
        return False
    if not energy_check(self):
        return False
    if not obstacle_detect(self.x - 1,self.y):
        return False
    self.x = self.x - 1
    self.direction = "west"
    self.energy = self.energy - 5
    energy_charge(self)
    return True
def move_north(self):
    if self.y >= 5:
        print()
        print('Boundary Reached')
        return False
    if not energy_check(self):
        return False
    if not obstacle_detect(self.x,self.y + 1):
        return False
    self.y = self.y + 1
    self.direction = "north"
    self.energy = self.energy -5
    energy_charge(self)
    return True
def move_south(self):
    if self.y <= -5:
        print()
        print('Boundary Reached')
        return False
    if not energy_check(self):
        return False
    if not obstacle_detect(self.x,self.y - 1):
        return False
    self.y = self.y - 1
    self.direction = "south"
    self.energy = self.energy - 5
    energy_charge(self)
    return True
def energy_check(self):
    if self.energy < 5:
        print()
        print('Not enough energy!')
        return False
    if self.energy < 20:
        print()
        print('Warning: Low energy!')
    return True
def map(self):
    for y in range(5,-6,-1):
        for x in range(-5,6):
            if x == self.x and y == self.y:
                print('O', end=' ')
            elif (x,y) in obstacles:
                print('#', end=' ')
            elif (x,y) in charge:
                print('C', end=' ')
            else:
                print('.', end=' ') 
        print()
def obstacle_detect(next_x,next_y):
    if (next_x,next_y) in obstacles:
        print('Obstacle ahead, please try again')
        return False
    return True
def neon_status(self):
    print('Robot: ' + self.name)
    print('Position: (' + str(self.x) + ',' + str(self.y) + ')')
    print('Direction: ' + self.direction)
    print('Energy: ' + str(self.energy))
def energy_charge(self):
    if (self.x,self.y) in charge:
        self.energy = 100
        print('Energy have been recharged to 100')
    return True
def move_command():
    while True:
        command = input('Direction(North, West, South, East) to move Neon \nStop to quit \nStatus to view Neon Status \nMap to view map \nEnter your pick here: ').strip().lower()
        if command == 'east':
            move_east(Neon)
            print()
        elif command == 'north':
            move_north(Neon)
            print()
        elif command == 'south':
            move_south(Neon)
            print()
        elif command == 'west':
            move_west(Neon)
            print()
        elif command == 'stop':
            break
        elif command == 'status':
            print()
            neon_status(Neon)
            print()
        elif command == 'map':
            print()
            map(Neon)
            print()
        else:
            print('Invalid command! Try again')
move_command()
