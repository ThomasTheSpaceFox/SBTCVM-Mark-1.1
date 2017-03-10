#!/usr/bin/env python
import libTDAcommon
import libbaltcalc
import libttext
import sys
#tasmfile="assmtst1.tasm"

#tasminput=open(tasmfile)
import fileinput

print("SBTCVM-asm version 1.2.0 starting")

assmoverrun=729
instcnt=0
txtblk=0

outfile="assmout.trom"

def getlinetern(line):
	line=(line-364)
	tline=libTDAcommon.trunkto6(libbaltcalc.DECTOBT(line))
	return tline


class gotoref:
	def __init__(self, line, gtname):
		self.line=line
		self.tline=getlinetern(line)
		self.gtname=gtname

gotoreflist=list()
print "preforming gotoref prescan pass"
for linen in fileinput.input():
	
	lined=linen
	linen=linen.replace("\n", "")
	linen=linen.replace("	", "")
	linelist=linen.split("|")
	
	if (len(linelist))==2:
		instword=(linelist[0])
		instdat=(linelist[1])
	else:
		instword=(linelist[0])
		instdat="000000"
	if instword=="textstop":
		txtblk=0
	gtflag=1
	if txtblk==1:
		for f in lined:
			#outn.write("+++0" + (libttext.charlook(f)) + "\n")
			instcnt += 1
	elif instword=="textstart":
		txtblk=1
	#raw class
	elif instword=="romread1":
		#outn.write("----" + instdat + "\n")
		instcnt += 1
	elif instword=="romread2":
		#outn.write("---0" + instdat + "\n")
		instcnt += 1
	elif instword=="IOread1":
		#outn.write("---+" + instdat + "\n")
		instcnt += 1
	elif instword=="IOread2":
		#outn.write("--0-" + instdat + "\n")
		instcnt += 1
	elif instword=="IOwrite1":
		#outn.write("--00" + instdat + "\n")
		instcnt += 1
	elif instword=="IOwrite2":
		#outn.write("--0+" + instdat + "\n")
		instcnt += 1
	elif instword=="regswap":
		#outn.write("--+-" + instdat + "\n")
		instcnt += 1
	elif instword=="copy1to2":
		#outn.write("--+0" + instdat + "\n")
		instcnt += 1
	elif instword=="copy2to1":
		#outn.write("--++" + instdat + "\n")
		instcnt += 1
	elif instword=="invert1":
		#outn.write("-0--" + instdat + "\n")
		instcnt += 1
	elif instword=="invert2":
		#outn.write("-0-0" + instdat + "\n")
		instcnt += 1
	elif instword=="add":
		#outn.write("-0-+" + instdat + "\n")
		instcnt += 1
	elif instword=="subtract":
		#outn.write("-00-" + instdat + "\n")
		instcnt += 1
	elif instword=="multiply":
		#outn.write("-000" + instdat + "\n")
		instcnt += 1
	elif instword=="divide":
		#outn.write("-00+" + instdat + "\n")
		instcnt += 1
	elif instword=="setreg1":
		#outn.write("-0+-" + instdat + "\n")
		instcnt += 1
	elif instword=="setreg2":
		#outn.write("-0+0" + instdat + "\n")
		instcnt += 1
	elif instword=="setinst":
		#outn.write("-0++" + instdat + "\n")
		instcnt += 1
	elif instword=="setdata":
		#outn.write("-+--" + instdat + "\n")
		instcnt += 1
	#----jump in used opcodes----
	#color drawing
	elif instword=="colorpixel":
		#outn.write("0---" + instdat + "\n")
		instcnt += 1
	elif instword=="setcolorreg":
		#outn.write("0--0" + instdat + "\n")
		instcnt += 1
	elif instword=="colorfill":
		#outn.write("0--+" + instdat + "\n")
		instcnt += 1
	elif instword=="setcolorvect":
		#outn.write("0-0-" + instdat + "\n")
		instcnt += 1
	elif instword=="colorline":
		#outn.write("0-00" + instdat + "\n")
		instcnt += 1
	elif instword=="colorrect":
		#outn.write("0-0+" + instdat + "\n")
		instcnt += 1
	#mono drawing
	elif instword=="monopixel":
		#outn.write("0-+-" + instdat + "\n")
		instcnt += 1
	elif instword=="monofill":
		#outn.write("0-+0" + instdat + "\n")
		instcnt += 1
	elif instword=="setmonovect":
		#outn.write("0-++" + instdat + "\n")
		instcnt += 1
	elif instword=="monoline":
		#outn.write("00--" + instdat + "\n")
		instcnt += 1
	elif instword=="monorect":
		#outn.write("00-0" + instdat + "\n")
		instcnt += 1
	#----opcode 00-+ unused----
	elif instword=="stop":
		#outn.write("000-" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="null":
		#outn.write("0000" + instdat + "\n")
		instcnt += 1
	elif instword=="gotodata":
		#outn.write("000+" + instdat + "\n")#
		instcnt += 1
		#autostpflg=1
	elif instword=="gotoreg1":
		#outn.write("00+-" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="gotodataif":
		#outn.write("00+0" + instdat + "\n")#
		instcnt += 1
	elif instword=="wait":
		#outn.write("00++" + instdat + "\n")
		instcnt += 1
	elif instword=="YNgoto":
		#outn.write("0+--" + instdat + "\n")#
		instcnt += 1
	elif instword=="userwait":
		#outn.write("0+-0" + instdat + "\n")
		instcnt += 1
	elif instword=="TTYclear":
		#outn.write("0+-+" + instdat + "\n")
		instcnt += 1
	#----gap in used opcodes----
	elif instword=="gotoA":
		#outn.write("+---" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoAif":
		#outn.write("+--0" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoB":
		#outn.write("+--+" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoBif":
		#outn.write("+-0-" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoC":
		#outn.write("+-00" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="gotoCif":
		#outn.write("+-0+" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoD":
		#outn.write("+-+-" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="gotoDif":
		#outn.write("+-+0" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoE":
	#	outn.write("+-++" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="gotoEif":
		#outn.write("+0--" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoF":
		#outn.write("+0-0" + instdat + "\n")
		instcnt += 1
		#autostpflg=1
	elif instword=="gotoFif":
		outn.write("+0-+" + instdat + "\n")
		instcnt += 1
	#----gap in used opcodes----
	elif instword=="dumpreg1":
		#outn.write("++0+" + instdat + "\n")
		instcnt += 1
	elif instword=="dumpreg2":
		#outn.write("+++-" + instdat + "\n")
		instcnt += 1
	elif instword=="TTYwrite":
		#outn.write("+++0" + instdat + "\n")
		instcnt += 1
	elif instword=="buzzer":
		#outn.write("++++" + instdat + "\n")
		instcnt += 1
	else:
		gtflag=0
	if (len(linelist))==3 and gtflag==1:
		gtox=gotoref((instcnt - 1), linelist[2])
		gotoreflist.extend([gtox])
		print ("found gotoref: \"" + linelist[2] + "\", at instruction:\"" + str((instcnt - 1)) + "\"")

#print gotoreflist
instcnt=0
firstloop=1
for linen in fileinput.input():
	if firstloop==1:
		print "preforming firstloop startup..."
		assmflename=fileinput.filename()
		assmnamelst=assmflename.rsplit('.', 1)
		outfile=(assmnamelst[0] + (".trom"))
		outn = open(outfile, 'w')
		firstloop=0
		print "done. begin compile."
	lined=linen
	linen=linen.replace("\n", "")
	linen=linen.replace("	", "")
	linelist=linen.split("|")
	autostpflg=0
	if (len(linelist))==2 or (len(linelist))==3:
		instword=(linelist[0])
		instdat=(linelist[1])
	else:
		instword=(linelist[0])
		instdat="000000"
	if instword=="textstop":
		txtblk=0
	
	if txtblk==1:
		for f in lined:
			outn.write("+++0" + (libttext.charlook(f)) + "\n")
			instcnt += 1
	elif instword=="textstart":
		txtblk=1
	#raw class
	elif instword=="romread1":
		outn.write("----" + instdat + "\n")
		instcnt += 1
	elif instword=="romread2":
		outn.write("---0" + instdat + "\n")
		instcnt += 1
	elif instword=="IOread1":
		outn.write("---+" + instdat + "\n")
		instcnt += 1
	elif instword=="IOread2":
		outn.write("--0-" + instdat + "\n")
		instcnt += 1
	elif instword=="IOwrite1":
		outn.write("--00" + instdat + "\n")
		instcnt += 1
	elif instword=="IOwrite2":
		outn.write("--0+" + instdat + "\n")
		instcnt += 1
	elif instword=="regswap":
		outn.write("--+-" + instdat + "\n")
		instcnt += 1
	elif instword=="copy1to2":
		outn.write("--+0" + instdat + "\n")
		instcnt += 1
	elif instword=="copy2to1":
		outn.write("--++" + instdat + "\n")
		instcnt += 1
	elif instword=="invert1":
		outn.write("-0--" + instdat + "\n")
		instcnt += 1
	elif instword=="invert2":
		outn.write("-0-0" + instdat + "\n")
		instcnt += 1
	elif instword=="add":
		outn.write("-0-+" + instdat + "\n")
		instcnt += 1
	elif instword=="subtract":
		outn.write("-00-" + instdat + "\n")
		instcnt += 1
	elif instword=="multiply":
		outn.write("-000" + instdat + "\n")
		instcnt += 1
	elif instword=="divide":
		outn.write("-00+" + instdat + "\n")
		instcnt += 1
	elif instword=="setreg1":
		outn.write("-0+-" + instdat + "\n")
		instcnt += 1
	elif instword=="setreg2":
		outn.write("-0+0" + instdat + "\n")
		instcnt += 1
	elif instword=="setinst":
		instgpe=instdat.split(">")
		if (len(instgpe))==1:
			outn.write("-0++" + instdat + "\n")#
			instcnt += 1
			autostpflg=1
		else:
			gtpoint=instgpe[1]
			gtmatch=0
			instcnt += 1
			for fx in gotoreflist:
				if fx.gtname==gtpoint:
					outn.write("-0++" + fx.tline + "\n")
					gtmatch=1
			if gtmatch==0:
				print "ERROR: pointer: \"" + gtpoint + "\"not found. STOP"
				sys.exit()
	elif instword=="setdata":
		instgpe=instdat.split(">")
		if (len(instgpe))==1:
			outn.write("-+--" + instdat + "\n")#
			instcnt += 1
			autostpflg=1
		else:
			gtpoint=instgpe[1]
			gtmatch=0
			instcnt += 1
			for fx in gotoreflist:
				if fx.gtname==gtpoint:
					outn.write("-+--" + fx.tline + "\n")
					gtmatch=1
			if gtmatch==0:
				print "ERROR: pointer: \"" + gtpoint + "\"not found. STOP"
				sys.exit()
	#----jump in used opcodes----
	#color drawing
	elif instword=="colorpixel":
		outn.write("0---" + instdat + "\n")
		instcnt += 1
	elif instword=="setcolorreg":
		outn.write("0--0" + instdat + "\n")
		instcnt += 1
	elif instword=="colorfill":
		outn.write("0--+" + instdat + "\n")
		instcnt += 1
	elif instword=="setcolorvect":
		outn.write("0-0-" + instdat + "\n")
		instcnt += 1
	elif instword=="colorline":
		outn.write("0-00" + instdat + "\n")
		instcnt += 1
	elif instword=="colorrect":
		outn.write("0-0+" + instdat + "\n")
		instcnt += 1
	#mono drawing
	elif instword=="monopixel":
		outn.write("0-+-" + instdat + "\n")
		instcnt += 1
	elif instword=="monofill":
		outn.write("0-+0" + instdat + "\n")
		instcnt += 1
	elif instword=="setmonovect":
		outn.write("0-++" + instdat + "\n")
		instcnt += 1
	elif instword=="monoline":
		outn.write("00--" + instdat + "\n")
		instcnt += 1
	elif instword=="monorect":
		outn.write("00-0" + instdat + "\n")
		instcnt += 1
	#----opcode 00-+ unused----
	elif instword=="stop":
		outn.write("000-" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="null":
		outn.write("0000" + instdat + "\n")
		instcnt += 1
	elif instword=="gotodata":
		instgpe=instdat.split(">")
		if (len(instgpe))==1:
			outn.write("000+" + instdat + "\n")#
			instcnt += 1
			autostpflg=1
		else:
			gtpoint=instgpe[1]
			gtmatch=0
			instcnt += 1
			for fx in gotoreflist:
				if fx.gtname==gtpoint:
					outn.write("000+" + fx.tline + "\n")
					gtmatch=1
			if gtmatch==0:
				print "ERROR: pointer: \"" + gtpoint + "\"not found. STOP"
				sys.exit()
			
	elif instword=="gotoreg1":
		outn.write("00+-" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotodataif":
		instgpe=instdat.split(">")
		if (len(instgpe))==1:
			outn.write("00+0" + instdat + "\n")#
			instcnt += 1
			autostpflg=1
		else:
			gtpoint=instgpe[1]
			gtmatch=0
			instcnt += 1
			for fx in gotoreflist:
				if fx.gtname==gtpoint:
					outn.write("00+0" + fx.tline + "\n")
					gtmatch=1
			if gtmatch==0:
				print "ERROR: pointer: \"" + gtpoint + "\"not found. STOP"
				sys.exit()
	elif instword=="wait":
		outn.write("00++" + instdat + "\n")
		instcnt += 1
	elif instword=="YNgoto":
		instgpe=instdat.split(">")
		if (len(instgpe))==1:
			outn.write("0+--" + instdat + "\n")#
			instcnt += 1
			autostpflg=1
		else:
			gtpoint=instgpe[1]
			gtmatch=0
			instcnt += 1
			for fx in gotoreflist:
				if fx.gtname==gtpoint:
					outn.write("0+--" + fx.tline + "\n")
					gtmatch=1
			if gtmatch==0:
				print "ERROR: pointer: \"" + gtpoint + "\"not found. STOP"
				sys.exit()
	elif instword=="userwait":
		outn.write("0+-0" + instdat + "\n")
		instcnt += 1
	elif instword=="TTYclear":
		outn.write("0+-+" + instdat + "\n")
		instcnt += 1
	#----gap in used opcodes----
	elif instword=="gotoA":
		outn.write("+---" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoAif":
		outn.write("+--0" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoB":
		outn.write("+--+" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoBif":
		outn.write("+-0-" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoC":
		outn.write("+-00" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoCif":
		outn.write("+-0+" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoD":
		outn.write("+-+-" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoDif":
		outn.write("+-+0" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoE":
		outn.write("+-++" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoEif":
		outn.write("+0--" + instdat + "\n")
		instcnt += 1
	elif instword=="gotoF":
		outn.write("+0-0" + instdat + "\n")
		instcnt += 1
		autostpflg=1
	elif instword=="gotoFif":
		outn.write("+0-+" + instdat + "\n")
		instcnt += 1
	#----gap in used opcodes----
	elif instword=="dumpreg1":
		outn.write("++0+" + instdat + "\n")
		instcnt += 1
	elif instword=="dumpreg2":
		outn.write("+++-" + instdat + "\n")
		instcnt += 1
	elif instword=="TTYwrite":
		outn.write("+++0" + instdat + "\n")
		instcnt += 1
	elif instword=="buzzer":
		outn.write("++++" + instdat + "\n")
		instcnt += 1
	if instcnt>assmoverrun:
		print("ERROR!: assembler has exceded rom size limit of 729!")

if txtblk==1:
	print "WARNING: unclosed Text block!"

if instcnt==0:
	print "ERROR: No instructions found. nothing to compile."

if autostpflg==0 and instcnt<729:
	print "NOTICE: no explicit goto or stop instruction at end of program.  SBTCVM-asm will add a stop automatically."
	outn.write("000-" + "000000" + "\n")
	instcnt += 1

instpad=instcnt
while instpad!=729:
	outn.write("0000" + "000000" + "\n")
	instpad += 1

instextra=(instpad - instcnt)
print ("SBTCVM Mk1.1 assembly file \"" + assmflename + "\" has been compiled into: \"" + outfile + "\"")
print ("total instructions: " + str(instcnt))
print ("extra space: " + str(instextra))