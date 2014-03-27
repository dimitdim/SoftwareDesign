# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:34:24 2014

@author: pruvolo
"""

import pygame
from pygame.locals import *
import random
import math
import time

class BrickBreakerModel:
    """encodes gamestate of brickbreaker"""
    def __init__(self):
        self.number_of_lives = 3
        self.bricks=list()
        for col in range(640/110):
            for row in range(240/30):
                new_brick=Brick(10+110*col,10+30*row,100,20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                self.bricks.append(new_brick)

class Brick:
    """encodes state of brick"""
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color

class BrickBreakerView:
    def __init__(self,model,screen):
        self.model=model
        self.screen=screen

    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for brick in self.model.bricks:
            pygame.draw.rect(self.screen, pygame.Color(brick.color[0],brick.color[1],brick.color[2]), pygame.Rect(brick.x,brick.y,brick.width,brick.height))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = BrickBreakerModel()
    view=BrickBreakerView(model,screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        view.draw()
        time.sleep(.001)

    pygame.quit()
