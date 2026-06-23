from settings import *
import pygame
import math

class Player():
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS 
        self.angle = PLAYER_ANGLE
    
    def movement(self): # There is a diagram explaining the logic behind the trig
                        # functions in this folder (player_coordinate_formulas.png)
        sin_a = math.sin(self.angle) # sin_a is sin(alpha) 
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed() # List of keys that are currently getting
                                        # pressed.
        if keys[pygame.K_w]: 
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_cos
            dy += -speed_sin
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.x += dx
        self.y += dy

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time


    def update(self):
        self.movement()
    
    @property # This is called a decorator and modifies function behavior.
    def pos(self): # "@property" is a built in decorator that comes with Python
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
