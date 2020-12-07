# Import libraries/modules for the program
import pygame #Use "pygame" library to create GUI, game loop, draw shapes/images on screen
import random #Use "random" library to select randomly the guess word to display
#-----------------------------------------------------------------
# Initialize pygame
pygame.init()
# Create a GUI window
winHeight = 480
winWidth = 700
GREEN = (0,255,0)
win = pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("Hangman - by Daniel")

#-----------------------------------------------------------------
# Main program here
inPlay = True
while inPlay:
	# Use loop to draw window	
	win.fill(GREEN);
	pygame.display.update()
	pygame.time.delay(100)

#-----------------------------------------------------------------
pygame.quit() # always quit pygame when done!
