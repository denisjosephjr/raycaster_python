import pygame # Looking forward to using this module
import sys # This module is still a mystery to me. It is for system specific parameters and function/ interpreter interaction.

from settings import * # What the hell is the pound symbol supposed to be?
# The pound symbol allows the import of all objects in the module without using dot notation. Risky..
from map import *

class Game():
    def __init__(self):
        pygame.init() # Strange, to have to call init() in another module. We'll see..
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock() # This line concerns me, i think it should be a function call, but it isn't
        self.dela_time = 1 # delta time is the amount of time that has passed since the last frame
        self.new_game()

    def new_game(self): # Assuming, that I will use this later.
        self.map = Map(self) # from the map module, creates map

    def update(self):
        pygame.display.flip() # Not sure what this function does yet.
        self.delta_time = self.clock.tick(FPS)    # Assuming that this function sets the frame rate, Not exactly..
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}') # This would display the current frame rate rounded to 1 decimal place

    def draw(self):
        self.screen.fill('black') # blacks out the screen, probably when loading.
        self.map.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                pygame.quit() # condition statement that exits the game if detected. Although, I wish I were more familiar with this
                sys.exit()

    def run(self):
        while True: # So this function calls 3 of the other functions only if it is true that the game is running
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__': # I struggled to understand this in the past. Basically __name__ is variable that holds the module name.
    game = Game()
    game.run()  # but... the interpreter assigns the name '__main__' if it is the primary module running (not the actual file name)
