#!/usr/bin/env python
import os
import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
from pygame.locals import *
import time
import libttext
pygame.font.init()
simplefont = pygame.font.SysFont(None, 16)


fondir="FONT0"


def abtslackline(receveabt, linetext):
	interx=[(receveabt[1]), (receveabt[2]),(receveabt[3]), (receveabt[4]), (receveabt[5]), (receveabt[6]), (receveabt[7]), (receveabt[8]), (receveabt[9]), (receveabt[10]), (receveabt[11]), (receveabt[12]), (receveabt[13]), (receveabt[14]), (receveabt[15]), (receveabt[16]), (receveabt[17]), (receveabt[18]), (receveabt[19]), (receveabt[20]), (receveabt[21]), (receveabt[22]), (receveabt[23]), (receveabt[24]), (receveabt[25]),(receveabt[26]), (linetext)]
	return interx

def abtcharblit(receveabtb, charblit):
	if charblit=="\n":
		receveabtb=abtslackline(receveabtb, "")
	else:
		charnum=0
		curr=receveabtb[26]
		for f in curr:
			if charnum==36:
				receveabtb=abtslackline(receveabtb, "")
			charnum += 1
		receveabtb[26]=((receveabtb[26]) + charblit)
	return(receveabtb)

def charblit(chsurface, colx, liney, charcode):
	colx=(colx*9)
	liney=(liney*9)
	glifcode=libttext.charcodedict.get(charcode)
	#print glifcode
	gliffile=(libttext.chargliph.get(glifcode))
	#print gliffile
	glif=pygame.image.load(os.path.join(fondir, (libttext.chargliph.get(glifcode))))
	chsurface.blit(glif, (colx, liney))
	return chsurface

