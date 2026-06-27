import pygame # Looking forward to using this module

import sys # This module is still a mystery to me. It is for system specific 
           # parameters and function/ interpreter interaction.

from settings import * # The pound symbol allows the import of all objects in the
                       # module without using dot notation. Risky..

from map import *

from player import *


class Game():

    def __init__(self):
    
        pygame.init()                               # Read Pygame Documentation

        self.screen = pygame.display.set_mode(RES)  # Sets resolution to value
                                                    # specified in settings.py

        self.clock = pygame.time.Clock()            # Read Pygame Documentation

        self.dela_time = 1 # Delta Time: The amount of time that has passed since
                           # the last frame. What unit?
        self.new_game()


    def new_game(self): 
        self.map = Map(self) # Creates instance of a map.


    def update(self):
        pygame.display.flip() # Read Pygame Documentation

        self.delta_time = self.clock.tick(FPS)    # Read Pygame Documentation 
                                                  
        # This would display the current frame rate rounded to 1 decimal place.
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}') 


    def draw(self):
        self.screen.fill('black') # blacks out the screen, probably when loading.
        self.map.draw()


    def check_events(self):
        # Read Pygame Documentation
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                pygame.quit() # Conditional statement that exits the game if detected. 
                sys.exit()

    def run(self):
        while True: # The 3 methods that effectively run the game.
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__': # __name__ is a variable that holds the module name.
    game = Game()
    game.run()  # but... the interpreter assigns the name '__main__' if it is the primary module running (not the actual file name)
