#!/usr/bin/env python
import libSBTCVM
import time
import os
import array
import math
import libbaltcalc


#poor man's wave generator :p
def sqblksnd(reptimes, multit):
	ex="!"
	til="^"
	sampl=(((ex * reptimes) + (til * reptimes)) * multit)
	return sampl
#wavsp=(sqblksnd(220, 20))
	
	
def mk1buzz(code):
	timechar=code[0]
	#print timechar
	if timechar=="+":
		timemag=60
	elif timechar=="-":
		timemag=20
	else:
		timemag=40
	freqcode=((code[1]) + (code[2]) + (code[3]) + (code[4]) +(code[5]))
	#print freqcode
	baserep=160
	repjump=2
	magn=libSBTCVM.buzznumstruct5(libbaltcalc.BTINVERT(freqcode))
	magn=(243 - magn + 20)
	
	repadd=(repjump * magn)
	#samplmag=sqblksnd((baserep + repadd), (20))
	#sampltnk=samplmag[:6480]
	if timechar=="+":
		#sampltnk=(sampltnk + sampltnk + sampltnk + sampltnk + sampltnk)
		sampltnk=autosquare(repadd, 0.31)
	elif timechar=="-":
		sampltnk=autosquare(repadd, 0.11)
		#sampltnk=(sampltnk)
		
	else:
		#sampltnk=(sampltnk + sampltnk + sampltnk)
		sampltnk=autosquare(repadd, 0.21)
	#print sampltnk
	return sampltnk

def foobsin(num):
	#return math.sin(math.sin(math.sin(num)))
	#return math.sin(math.sin(num))
	return (math.floor(math.sin(num)) * 4500)


def autosquare(freq, lenth):
	temparray=array.array('f', [(foobsin(2.0 * math.pi * freq * t / 22050)) for t in xrange(0, int(lenth * 22050))])
	return temparray


