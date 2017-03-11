#!/usr/bin/env python
import libtfont0
import libtrom
import pygame.event
import pygame.key
import pygame.display
import pygame.image
import pygame.mixer
import pygame
from pygame.locals import *
import time
import os
import libTDAcommon
import libbaltcalc
import libttext
import libtbuzz
import libtstcg1 as stcg
pygame.display.init()

print "SBTCVM Mark 1.1 Starting up..."

windowicon=pygame.image.load(os.path.join('GFX', 'icon64.png'))
pygame.display.set_icon(windowicon)

screensurf=pygame.display.set_mode((800, 600))
pygame.display.set_caption("SBTCVM Mark 1.1", "SBTCVM Mark 1.1")
pygame.font.init()
#used for TTY
simplefont = pygame.font.SysFont(None, 16)
#used for smaller data displays (inst. data etc.)
smldispfont = pygame.font.SysFont(None, 16)
#used in larger data displays (register displays, etc.)
lgdispfont = pygame.font.SysFont(None, 20)
pixcnt1=40
pixjmp=14
USRYN=0
USRWAIT=0
#graphics:
#background pixmap
vmbg=pygame.image.load(os.path.join('GFX', 'VMBG.png'))
#indicator lamps
#GREEN
LEDGREENON=pygame.image.load(os.path.join('GFX', 'LAMP-GREEN.png'))
LEDGREENOFF=pygame.image.load(os.path.join('GFX', 'LAMP-GREEN-OFF.png'))
#CPU
CPULEDACT=pygame.image.load(os.path.join('GFX', 'LAMP-BLUE.png'))
CPULEDSTANDBY=pygame.image.load(os.path.join('GFX', 'LAMP-ORANGE.png'))

COLORDISP=pygame.image.load(os.path.join('GFX', 'COLORDISP-DEF.png'))
MONODISP=pygame.image.load(os.path.join('GFX', 'MONODISP-DEF.png'))
#this list is what is displayed on the TTY on VM boot.

abt=["SBTCVM", "Mark 1.1", "v1.0.0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "ready", ""]

pygame.mixer.init(frequency=22050 , size=-16)

extradraw=0

wavsp=libtbuzz.mk1buzz("0-----")
snf=pygame.mixer.Sound(wavsp)
snf.play()

#config defaults
TROMA="BOOTUP.TROM"
#these are dud roms full of soft stops
TROMB=("DEFAULTdud.TROM")
TROMC=("DEFAULTdud.TROM")
TROMD=("DEFAULTdud.TROM")
TROME=("DEFAULTdud.TROM")
TROMF=("DEFAULTdud.TROM")
CPUWAIT=(0.01)
stepbystep=0
scconf=open('BOOTUP.CFG', 'r')
exconf=compile(scconf.read(), 'BOOTUP.CFG', 'exec')

tuibig=1
logromexit=0
logIOexit=0
exec(exconf)
#print BOOTUPFILE

#4 trit instruct
#6 trit data.
#as such:
#iiiidddddd

colvectorreg="000000"
monovectorreg="000000"

if stepbystep==1:
	STEPLED=LEDGREENON
else:
	STEPLED=LEDGREENOFF



stcgsurf=pygame.Surface((324, 243))
stcgsurf.fill((127, 127, 127))
#RAMBANK startup begin
RAMbank = {}

#calmlst = open("ORDEREDLIST6.txt")
screensurf.fill((0,127,255))
screensurf.blit(vmbg, (0, 0))
pygame.display.update()

#ramstart
for ramadr in libTDAcommon.calmlst:
	#print "foobar"
	ramadr=ramadr.replace("\n", "")
	RAMbank[ramadr] = "000000"
	#
tromready=0
print "waiting for libtrom"
while tromready==0:
	tromready=libtrom.initwait()
	time.sleep(0.1)
print "libtrom ready."	

MONODISPBIG=pygame.transform.scale(MONODISP, (144, 144))
COLORDISPBIG=pygame.transform.scale(COLORDISP, (148, 148))
#RAMBANK startup end
colorreg="++++++"
ROMFILE=TROMA
ROMLAMPFLG="A"
stopflag=0
EXECCHANGE=0
#ROMFILE=open(BOOTUPFILE)
EXECADDR="------"
REG1="000000"
REG2="000000"
print "SBTCVM Mark 1.1 Ready. the VM will now begin."
while stopflag==0:
	curinst=(libtrom.tromreadinst(EXECADDR,ROMFILE))
	curdata=(libtrom.tromreaddata(EXECADDR,ROMFILE))
	#some screen display stuff & general blitting
	#screensurf.fill((0,127,255))
	#draw Background
	screensurf.blit(vmbg, (0, 0))
	#these show the instruction and data in the instruction/data box :)
	insttext=smldispfont.render(curinst, True, (0, 255, 255), (0, 0, 0))
	datatext=smldispfont.render(curdata, True, (0, 255, 127), (0, 0, 0))
	screensurf.blit(insttext, (6, 495))
	screensurf.blit(datatext, (44, 495))
	#these draw the register displays :)
	reg1text=lgdispfont.render(REG1, True, (255, 0, 127), (0, 0, 0))
	reg2text=lgdispfont.render(REG2, True, (255, 127, 0), (0, 0, 0))
	screensurf.blit(reg1text, (98, 491))
	screensurf.blit(reg2text, (189, 491))
	#and here is what draws the ROM address display :)
	reg2text=lgdispfont.render(EXECADDR, True, (0, 127, 255), (0, 0, 0))
	screensurf.blit(reg2text, (280, 491))
	#and the current rom display :)
	CURROMTEXT=("ROM " + ROMLAMPFLG)
	reg2text=lgdispfont.render(CURROMTEXT, True, (255, 0, 255), (0, 0, 0))
	screensurf.blit(reg2text, (371, 491))
	#LED LAMPS
	#CPU
	screensurf.blit(CPULEDACT, (514, 493))
	#STEP
	screensurf.blit(STEPLED, (514, 500))
	screensurf.blit(COLORDISPBIG, (649, 1))
	screensurf.blit(MONODISPBIG, (649, 150))
	#TTY drawer :)
	#for fnx in abt:
	#	fnx=fnx.replace('\n', '')
	#	abttext=simplefont.render(fnx, True, (0, 127, 255), (0, 0, 0))
	#	screensurf.blit(abttext, (45, pixcnt1))
	#	pixcnt1 += pixjmp
	#pixcnt1=40
	lineq=0
	stcgsurf.fill((127, 127, 127))
	for fnx in abt:
		fnx=fnx.replace('\n', '')
		colq=0
		for qlin in fnx:
			#print qlin
			charq=libttext.charlookupdict.get(qlin)
			#print charq
			stcg.charblit(stcgsurf, colq, lineq, charq)
			colq +=1
		lineq +=1
	#screensurf.blit(stcgsurf, (45, 40))
	if tuibig==0:
		screensurf.blit(stcgsurf, (45, 40))
	else:
		bigstcg=pygame.transform.scale(stcgsurf, (648, 486))
		screensurf.blit(bigstcg, (0, 0))
	#aaaaannnnddd update display! :D
	pygame.display.update()
	
	#ROM READ (first register)
	if curinst=="----":
		REG1=(libtrom.tromreaddata(EXECADDR,ROMFILE))
		#print("----")
	#ROM READ (second register)
	elif curinst=="---0":
		REG2=(libtrom.tromreaddata(EXECADDR,ROMFILE))
		#print("---0")
	#IO READ REG1
	elif curinst=="---+":
		REG1=RAMbank[curdata]
		#print("---+")
	#IO READ REG2
	elif curinst=="--0-":
		REG2=RAMbank[curdata]
		#print("--0-")
	#IO WRITE REG1
	elif curinst=="--00":
		RAMbank[curdata] = REG1	
	#IO WRITE REG2
	elif curinst=="--0+":
		RAMbank[curdata] = REG2
	#swap primary Registers
	elif curinst=="--+-":
		REGTEMP = REG1
		REG1 = REG2
		REG2 = REGTEMP 
	#copy Register 1 to register 2
	elif curinst=="--+0":
		REG2 = REG1
	#copy Register 2 to register 1
	elif curinst=="--++":
		REG1 = REG2
	#invert register 1
	elif curinst=="-0--":
		REG1 = (libbaltcalc.BTINVERT(REG1))
	#invert register 2
	elif curinst=="-0-0":
		REG2 = (libbaltcalc.BTINVERT(REG2))
	#add both registers, load awnser into REG1
	elif curinst=="-0-+":
		#print REG1
		#print REG2
		#print "bla"
		REG1 = (libTDAcommon.trunkto6(libbaltcalc.btadd(REG1, REG2)))
	#sub both registers, load awnser into REG1
	elif curinst=="-00-":
		REG1 = (libTDAcommon.trunkto6(libbaltcalc.btsub(REG1, REG2)))
	#mul both registers, load awnser into REG1
	elif curinst=="-000":
		REG1 = (libTDAcommon.trunkto6(libbaltcalc.btmul(REG1, REG2)))
	#dev both registers, load awnser into REG1
	elif curinst=="-00+":
		REG1 = (libTDAcommon.trunkto6(libbaltcalc.btdev(REG1, REG2)))
	#set REG1
	elif curinst=="-0+-":
		REG1 = curdata
	#set REG1
	elif curinst=="-0+0":
		REG2 = curdata
	#set inst
	elif curinst=="-0++":
		instsetto=(REG1[0] + REG1[1] + REG1[2] + REG1[3])
		libtrom.tromsetinst(curdata, instsetto, ROMFILE)
	#set data
	elif curinst=="-+--":
		libtrom.tromsetdata(curdata, REG1, ROMFILE)
	#color draw
	elif curinst=="0---":
		jx=libTDAcommon.drawnumstruct3((curdata[0] + curdata[1] + curdata[2]))
		jy=libTDAcommon.drawnumstruct3((curdata[3] + curdata[4] + curdata[5]))
		RGBcol=libTDAcommon.colorfind(colorreg)
		#print monocol
		pygame.draw.line(COLORDISP, RGBcol, [jx, jy], [jx, jy], 1)
		COLORDISPBIG=pygame.transform.scale(COLORDISP, (148, 148))
	#set PPU color Register
	elif curinst=="0--0":
		colorreg=curdata
	elif curinst=="0--+":
		RGBcol=libTDAcommon.colorfind(curdata)
		#print monocol
		COLORDISP.fill(RGBcol)
		COLORDISPBIG=pygame.transform.scale(COLORDISP, (148, 148))
	#set PPU color vector Register
	elif curinst=="0-0-":
		colvectorreg=curdata
	elif curinst=="0-00":
		jx=libTDAcommon.drawnumstruct3((curdata[0] + curdata[1] + curdata[2]))
		jy=libTDAcommon.drawnumstruct3((curdata[3] + curdata[4] + curdata[5]))
		kx=libTDAcommon.drawnumstruct3((colvectorreg[0] + colvectorreg[1] + colvectorreg[2]))
		ky=libTDAcommon.drawnumstruct3((colvectorreg[3] + colvectorreg[4] + colvectorreg[5]))
		RGBcol=libTDAcommon.colorfind(colorreg)
		#print monocol
		pygame.draw.line(COLORDISP, RGBcol, [jx, jy], [kx, ky], 1)
		COLORDISPBIG=pygame.transform.scale(COLORDISP, (148, 148))
	#color draw rect
	elif curinst=="0-0+":
		jx=libTDAcommon.drawnumstruct3((curdata[0] + curdata[1] + curdata[2]))
		jy=libTDAcommon.drawnumstruct3((curdata[3] + curdata[4] + curdata[5]))
		kx=libTDAcommon.drawnumstruct3((colvectorreg[0] + colvectorreg[1] + colvectorreg[2]))
		ky=libTDAcommon.drawnumstruct3((colvectorreg[3] + colvectorreg[4] + colvectorreg[5]))
		RGBcol=libTDAcommon.colorfind(colorreg)
		#print monocol
		#pygame.draw.line(COLORDISP, RGBcol, [jx, jy], [kx, ky], 1)
		COLORDISP.fill(RGBcol, (libTDAcommon.makerectbipoint(jx, jy, kx, ky)))
		COLORDISPBIG=pygame.transform.scale(COLORDISP, (148, 148))
	
	#mono draw
	#mono draw pixel
	elif curinst=="0-+-":
		jx=libTDAcommon.drawnumstruct2((curdata[0] + curdata[1]))
		jy=libTDAcommon.drawnumstruct2((curdata[2] + curdata[3]))
		monocol=(int(libTDAcommon.dollytell((curdata[4] + curdata[5]))))
		#print monocol
		pygame.draw.line(MONODISP, (monocol, monocol, monocol), [jx, jy], [jx, jy], 1)
		MONODISPBIG=pygame.transform.scale(MONODISP, (144, 144))
	#mono fill
	elif curinst=="0-+0":
		monocol=(int(libTDAcommon.dollytell((curdata[4] + curdata[5]))))
		#print monocol
		MONODISP.fill((monocol, monocol, monocol))
		MONODISPBIG=pygame.transform.scale(MONODISP, (144, 144))
	#set PPU mono vector Register
	elif curinst=="0-++":
		monovectorreg=curdata
	#draw mono line
	elif curinst=="00--":
		jx=libTDAcommon.drawnumstruct2((curdata[0] + curdata[1]))
		jy=libTDAcommon.drawnumstruct2((curdata[2] + curdata[3]))
		kx=libTDAcommon.drawnumstruct2((monovectorreg[0] + monovectorreg[1]))
		ky=libTDAcommon.drawnumstruct2((monovectorreg[2] + monovectorreg[3]))
		monocol=(int(libTDAcommon.dollytell((curdata[4] + curdata[5]))))
		#print monocol
		pygame.draw.line(MONODISP, (monocol, monocol, monocol), [jx, jy], [kx, ky], 1)
		MONODISPBIG=pygame.transform.scale(MONODISP, (144, 144))
	#mono draw rect
	elif curinst=="00-0":
		jx=libTDAcommon.drawnumstruct2((curdata[0] + curdata[1]))
		jy=libTDAcommon.drawnumstruct2((curdata[2] + curdata[3]))
		kx=libTDAcommon.drawnumstruct2((monovectorreg[0] + monovectorreg[1]))
		ky=libTDAcommon.drawnumstruct2((monovectorreg[2] + monovectorreg[3]))
		monocol=(int(libTDAcommon.dollytell((curdata[4] + curdata[5]))))
		#print monocol
		#pygame.draw.line(MONODISP, (monocol, monocol, monocol), [jx, jy], [kx, ky], 1)
		MONODISP.fill((monocol, monocol, monocol), (libTDAcommon.makerectbipoint(jx, jy, kx, ky)))
		MONODISPBIG=pygame.transform.scale(MONODISP, (144, 144))
	#SHUTDOWN VM
	elif curinst=="000-":
		stopflag=1
		abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
		abt=libTDAcommon.abtslackline(abt, "soft stop.")
	#NULL INSTRUCTION (DOES NOTHING) USE WHEN YOU WISH TO DO NOTHING :p
	elif curinst=="0000":
		print("NULLinstruction")
	#goto rom adress specified by CURRENT DATA
	elif curinst=="000+":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
	#goto rom adress specified by Register 1
	elif curinst=="00+-":
		EXECADDRNEXT=REG1
		EXECCHANGE=1
	
	elif curinst=="00+0":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
	elif curinst=="00++":
		waitchop=curdata[5]
		if waitchop=="+":
			waitmagn=0.3
		elif waitchop=="-":
			waitmagn=0.1
		else:
			waitmagn=0.2
		time.sleep(( waitmagn))
	#asks user if goto to adress is desired
	elif curinst=="0+--":
		abt=libTDAcommon.abtslackline(abt, ("GOTO: (" + curdata + ") Y or N?"))
		USRYN=1
		extradraw=1	
	#user wait
	elif curinst=="0+-0":
		abt=libTDAcommon.abtslackline(abt, ("Press enter to continue."))
		USRWAIT=1
		extradraw=1	
	#TTY clear
	elif curinst=="0+-+":
		abt=["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
	#note these swap TROMS
	#TROMA: goto rom adress on TROMA specified by CURRENT DATA
	elif curinst=="+---":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROMA
		ROMLAMPFLG="A"
	#conditional GOTO
	elif curinst=="+--0":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROMA
			ROMLAMPFLG="A"
	#TROMB: goto rom adress on TROMB specified by CURRENT DATA
	elif curinst=="+--+":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROMB
		ROMLAMPFLG="B"
	elif curinst=="+-0-":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROMB
			ROMLAMPFLG="B"
	#TROMC: goto rom adress on TROMC specified by CURRENT DATA
	elif curinst=="+-00":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROMC
		ROMLAMPFLG="C"
	#conditional GOTO
	elif curinst=="+-0+":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROMC
			ROMLAMPFLG="C"
	#TROMD: goto rom adress on TROMD specified by CURRENT DATA
	elif curinst=="+-+-":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROMD
		ROMLAMPFLG="D"
	#conditional GOTO
	elif curinst=="+-+0":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROMD
			ROMLAMPFLG="D"
	#TROME: goto rom adress on TROME specified by CURRENT DATA
	elif curinst=="+-++":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROME
		ROMLAMPFLG="E"
	#conditional GOTO
	elif curinst=="+0--":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROME
			ROMLAMPFLG="E"
	#TROMF: goto rom adress on TROMF specified by CURRENT DATA
	elif curinst=="+0-0":
		EXECADDRNEXT=curdata
		EXECCHANGE=1
		ROMFILE=TROMF
		ROMLAMPFLG="F"
	#conditional GOTO
	elif curinst=="+0-+":
		if REG1==REG2:
			EXECADDRNEXT=curdata
			EXECCHANGE=1
			ROMFILE=TROMF
			ROMLAMPFLG="F"
	
	
	#dump register 1 to TTY
	elif curinst=="++0+":
		print ("REG1 DUMP:" + REG1)
		abt=libTDAcommon.abtslackline(abt, ("REG1 DUMP:" + REG1))
	#dump Register 2 to TTY
	elif curinst=="+++-":
		print ("REG2 DUMP:" + REG2)
		abt=libTDAcommon.abtslackline(abt, ("REG2 DUMP:" + REG2))
	#tty write port (direct)
	elif curinst=="+++0":
		abt=libTDAcommon.abtcharblit(abt, (libttext.charcodelook(curdata)))
	#Buzzer (direct)
	elif curinst=="++++":
		snf.stop()
		#print "derp"
		wavsp=libtbuzz.mk1buzz(curdata)
		snf=pygame.mixer.Sound(wavsp)
		snf.play()
		timechop=curdata[0]
		if timechop=="+":
			time.sleep(0.3)
		elif timechop=="-":
			time.sleep(0.1)
		else:
			time.sleep(0.2)
	#needed by user quering opcodes such as 0+--	
	if extradraw==1:
		screensurf.blit(vmbg, (0, 0))
		#these show the instruction and data in the instruction/data box :)
		insttext=smldispfont.render(curinst, True, (0, 255, 255), (0, 0, 0))
		datatext=smldispfont.render(curdata, True, (0, 255, 127), (0, 0, 0))
		screensurf.blit(insttext, (6, 495))
		screensurf.blit(datatext, (44, 495))
		#these draw the register displays :)
		reg1text=lgdispfont.render(REG1, True, (255, 0, 127), (0, 0, 0))
		reg2text=lgdispfont.render(REG2, True, (255, 127, 0), (0, 0, 0))
		screensurf.blit(reg1text, (98, 491))
		screensurf.blit(reg2text, (189, 491))
		#and here is what draws the ROM address display :)
		reg2text=lgdispfont.render(EXECADDR, True, (0, 127, 255), (0, 0, 0))
		screensurf.blit(reg2text, (280, 491))
		#and the current rom display :)
		CURROMTEXT=("ROM " + ROMLAMPFLG)
		reg2text=lgdispfont.render(CURROMTEXT, True, (255, 0, 255), (0, 0, 0))
		screensurf.blit(reg2text, (371, 491))
		#LED LAMPS
		#CPU
		screensurf.blit(CPULEDACT, (514, 493))
		#STEP
		screensurf.blit(STEPLED, (514, 500))
		screensurf.blit(COLORDISPBIG, (649, 1))
		screensurf.blit(MONODISPBIG, (649, 150))
		#TTY drawer :)
		#for fnx in abt:
		#	fnx=fnx.replace('\n', '')
		#	abttext=simplefont.render(fnx, True, (0, 127, 255), (0, 0, 0))
		#	screensurf.blit(abttext, (45, pixcnt1))
		#	pixcnt1 += pixjmp
		#pixcnt1=40
		lineq=0
		stcgsurf.fill((127, 127, 127))
		for fnx in abt:
			fnx=fnx.replace('\n', '')
			colq=0
			for qlin in fnx:
				#print qlin
				charq=libttext.charlookupdict.get(qlin)
				#print charq
				stcg.charblit(stcgsurf, colq, lineq, charq)
				colq +=1
			lineq +=1
		if tuibig==0:
			screensurf.blit(stcgsurf, (45, 40))
		else:
			bigstcg=pygame.transform.scale(stcgsurf, (648, 486))
			screensurf.blit(bigstcg, (0, 0))
		pygame.display.update()
		#abt=stcg.abtslackline(abt, jline)
		extradraw=0
	if USRWAIT==1:
		evhappenflg2=0
		while evhappenflg2==0:
			time.sleep(.1)
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_RETURN:
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					evhappenflg2=1
					stopflag=1
					abt=libTDAcommon.abtslackline(abt, "")
					abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
					abt=libTDAcommon.abtslackline(abt, "User stop.")
					break
				if event.type == KEYDOWN and event.key == K_F7:
					pygame.image.save(COLORDISP, (os.path.join('CAP', 'COLORDISP-OUT.png')))
					pygame.image.save(MONODISP, (os.path.join('CAP', 'MONODISP-OUT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F8:
					pygame.image.save(screensurf, (os.path.join('CAP', 'SCREENSHOT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F2:
					stepbystep=1
					STEPLED=LEDGREENON
					break
				if event.type == KEYDOWN and event.key == K_F10:
					ramdmp=open((os.path.join('CAP', 'IOBUSman.dmp')),  'w')
					for IOitm in RAMbank:
						ramdmp.write("A:" + str(IOitm) + " D:" + RAMbank[IOitm] + "\n")
					ramdmp.close()
					libtrom.manualdumptroms()
					break
		abt=libTDAcommon.abtslackline(abt, ("\n"))
		USRWAIT=0
	
	
	if USRYN==1:
		evhappenflg2=0
		while evhappenflg2==0:
			time.sleep(.1)
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_y:
					EXECADDRNEXT=curdata
					EXECCHANGE=1
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_n:
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					evhappenflg2=1
					stopflag=1
					abt=libTDAcommon.abtslackline(abt, "")
					abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
					abt=libTDAcommon.abtslackline(abt, "User stop.")
					break
				if event.type == KEYDOWN and event.key == K_F7:
					pygame.image.save(COLORDISP, (os.path.join('CAP', 'COLORDISP-OUT.png')))
					pygame.image.save(MONODISP, (os.path.join('CAP', 'MONODISP-OUT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F8:
					pygame.image.save(screensurf, (os.path.join('CAP', 'SCREENSHOT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F2:
					stepbystep=1
					STEPLED=LEDGREENON
					break
				if event.type == KEYDOWN and event.key == K_F10:
					ramdmp=open((os.path.join('CAP', 'IOBUSman.dmp')),  'w')
					for IOitm in RAMbank:
						ramdmp.write("A:" + str(IOitm) + " D:" + RAMbank[IOitm] + "\n")
					ramdmp.close()
					libtrom.manualdumptroms()
					break
		abt=libTDAcommon.abtslackline(abt, ("\n"))
		USRYN=0
	
	#print(EXECADDR)
	if stepbystep==1:
		#this is used when step-by-step mode is enabled
		evhappenflg2=0
		while evhappenflg2==0:
			time.sleep(.1)
			for event in pygame.event.get():
				if event.type == KEYDOWN and event.key == K_RETURN:
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					stopflag=1
					
					abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
					abt=libTDAcommon.abtslackline(abt, "User stop.")
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_F7:
					pygame.image.save(COLORDISP, (os.path.join('CAP', 'COLORDISP-OUT.png')))
					pygame.image.save(MONODISP, (os.path.join('CAP', 'MONODISP-OUT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F8:
					pygame.image.save(screensurf, (os.path.join('CAP', 'SCREENSHOT.png')))
					break
				if event.type == KEYDOWN and event.key == K_F2:
					stepbystep=0
					STEPLED=LEDGREENOFF
					evhappenflg2=1
					break
				if event.type == KEYDOWN and event.key == K_F10:
					ramdmp=open((os.path.join('CAP', 'IOBUSman.dmp')),  'w')
					for IOitm in RAMbank:
						ramdmp.write("A:" + str(IOitm) + " D:" + RAMbank[IOitm] + "\n")
					ramdmp.close()
					libtrom.manualdumptroms()
					break
				
		
	else:
		#...otherwise this is used to passivly check for imput
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				stopflag=1
				abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
				abt=libTDAcommon.abtslackline(abt, "User stop.")
				break
			if event.type == KEYDOWN and event.key == K_F7:
				pygame.image.save(COLORDISP, (os.path.join('CAP', 'COLORDISP-OUT.png')))
				pygame.image.save(MONODISP, (os.path.join('CAP', 'MONODISP-OUT.png')))
				break
			if event.type == KEYDOWN and event.key == K_F8:
				pygame.image.save(screensurf, (os.path.join('CAP', 'SCREENSHOT.png')))
				break
			if event.type == KEYDOWN and event.key == K_F10:
				ramdmp=open((os.path.join('CAP', 'IOBUSman.dmp')),  'w')
				for IOitm in RAMbank:
					ramdmp.write("A:" + str(IOitm) + " D:" + RAMbank[IOitm] + "\n")
				ramdmp.close()
				libtrom.manualdumptroms()
				break
			if event.type == KEYDOWN and event.key == K_F2:
				stepbystep=1
				STEPLED=LEDGREENON
				break
	#pygame.event.clear()
	
	
	
	#aaaaannnnddd update display! :D
	pygame.display.update()
	
	if curinst=="":
		stopflag=1
		abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
		abt=libTDAcommon.abtslackline(abt, "End Of Rom.")
	if EXECADDR=="+------":
		stopflag=1
		abt=libTDAcommon.abtslackline(abt, "VM SYSHALT:")
		abt=libTDAcommon.abtslackline(abt, "End Of RomBus.")
	EXECADDR=libbaltcalc.btadd(EXECADDR, "+")
	if EXECCHANGE==1:
		EXECCHANGE=0
		#print("ding")
		EXECADDR=EXECADDRNEXT
	if stopflag==1:
		abt=libTDAcommon.abtslackline(abt, "Press enter to exit.")
		screensurf.fill((0,127,255))
		screensurf.blit(vmbg, (0, 0))
	
		#these show the instruction and data in the instruction/data box :)
		insttext=smldispfont.render(curinst, True, (0, 255, 255), (0, 0, 0))
		datatext=smldispfont.render(curdata, True, (0, 255, 127), (0, 0, 0))
		screensurf.blit(insttext, (6, 495))
		screensurf.blit(datatext, (44, 495))
		#these draw the register displays :)
		reg1text=lgdispfont.render(REG1, True, (255, 0, 127), (0, 0, 0))
		reg2text=lgdispfont.render(REG2, True, (255, 127, 0), (0, 0, 0))
		screensurf.blit(reg1text, (98, 491))
		screensurf.blit(reg2text, (189, 491))
		#and here is what draws the ROM address display :)
		reg2text=lgdispfont.render(EXECADDR, True, (0, 127, 255), (0, 0, 0))
		screensurf.blit(reg2text, (280, 491))
		#and the current rom display :)
		CURROMTEXT=("ROM " + ROMLAMPFLG)
		reg2text=lgdispfont.render(CURROMTEXT, True, (255, 0, 255), (0, 0, 0))
		screensurf.blit(reg2text, (371, 491))
		#LED LAMPS
		screensurf.blit(CPULEDSTANDBY, (514, 493))
		#STEP
		screensurf.blit(STEPLED, (514, 500))
		screensurf.blit(COLORDISPBIG, (649, 1))
		screensurf.blit(MONODISPBIG, (649, 150))
		CURROMTEXT=("ROM " + ROMLAMPFLG)
		reg2text=lgdispfont.render(CURROMTEXT, True, (255, 0, 255), (0, 0, 0))
		#screensurf.blit(reg2text, (558, 198))
		
		#screensurf.blit(CPULEDSTANDBY, (605, 433))
		#screensurf.blit(STEPLED, (605, 440))
		#for fnx in abt:
		#	fnx=fnx.replace('\n', '')
		#	abttext=simplefont.render(fnx, True, (0, 127, 255), (0, 0, 0))
		#	screensurf.blit(abttext, (45, pixcnt1))
		#	pixcnt1 += pixjmp
		#pixcnt1=38
		lineq=0
		stcgsurf.fill((127, 127, 127))
		for fnx in abt:
			fnx=fnx.replace('\n', '')
			colq=0
			for qlin in fnx:
				#print qlin
				charq=libttext.charlookupdict.get(qlin)
				#print charq
				stcg.charblit(stcgsurf, colq, lineq, charq)
				colq +=1
			lineq +=1
		#screensurf.blit(stcgsurf, (45, 40))
		if tuibig==0:
			screensurf.blit(stcgsurf, (45, 40))
		else:
			bigstcg=pygame.transform.scale(stcgsurf, (648, 486))
			screensurf.blit(bigstcg, (0, 0))
	
	pygame.display.update()
	#clear buffer secion of IObus
	#this means: DONT USE THE BUFFER SECTION OF THE IObus AS RAM :|
	#chklist = open("ORDEREDLIST6REGISTER.txt")
	#for ramadr in libTDAcommon.chklist:
	#	#print "foobar"
	#	ramadr=ramadr.replace("\n", "")
	#	RAMbank[ramadr] = "000000"
	#	#
	
	
	time.sleep(CPUWAIT)
	
	evhappenflg2=0


if logromexit==1:
	print "logging TROM MEMORY into CAP dir..."
	libtrom.dumptroms()
if logIOexit==1:
	print "logging final IObus state into CAP dir..."
	ramdmp=open((os.path.join('CAP', 'IOBUS.dmp')),  'w')
	for IOitm in RAMbank:
		ramdmp.write("A:" + str(IOitm) + " D:" + RAMbank[IOitm] + "\n")
	ramdmp.close()
while evhappenflg2==0:
		time.sleep(.1)
		for event in pygame.event.get():
			if event.type == KEYDOWN and event.key == K_RETURN:
				evhappenflg2=1
				break
	