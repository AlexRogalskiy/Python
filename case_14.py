import pygame
import math
import numpy
import random

from pygame.locals import *

pygame.init()
width = 800
height = 640

size = width, height
background = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
fullBar = pygame.image.load("./full.jpg")
emptyBar = pygame.image.load("./empty.jpg")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
mainloop = True

barHeight = 36
barWidth = 80
barGraphHeight = 327
barPos = [55, 130]

def fftCalculations(data):
	data2 = numpy.array(data) / 4
	fourier = numpy.fft.rfft(data2)
	ffty = numpy.abs(fourier)
	ffty = ffty / 256.0
	return ffty

while mainloop:
	buff = [ random.random() for _ in range(1024) ]
	barData = fftCalculations(buff)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False
		if (event.type == KEYUP) or (event.type == KEYDOWN):
			if event.key == K_ESCAPE:
				mainloop = False
	screen.fill(background)

	for i in range(8):
		bars = barData[i]
		bars = int(math.floor(bars * 10))
		if bars > 10:
			bars = 10
		bars -= 1
		screen.blit(emptyBar, (barPos[0] + i * (barWidth + 10), barPos[1]), (0, 0, barWidth, barHeight * (10 - bars)))
		if bars >= 0:
			barStartPos = (barPos[0] + i * (barWidth + 10), barPos[1] + barGraphHeight - barHeight * bars + 6)
			barSourceBlit = (0, barGraphHeight - barHeight * bars + 6, barWidth, barHeight * bars)
			screen.blit(fullBar, barStartPos, barSourceBlit)

	pygame.display.update()