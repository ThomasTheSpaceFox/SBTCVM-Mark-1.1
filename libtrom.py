#!/usr/bin/env python
import libTDAcommon
import os

TROMB=("DEFAULTdud.TROM")
TROMC=("DEFAULTdud.TROM")
TROMD=("DEFAULTdud.TROM")
TROME=("DEFAULTdud.TROM")
TROMF=("DEFAULTdud.TROM")

libtromready=0
tromlogging=0
logreads=0
def initwait():
	return libtromready

scconf=open('BOOTUP.CFG', 'r')
exconf=compile(scconf.read(), 'BOOTUP.CFG', 'exec')
exec(exconf)

if tromlogging==0:
	logreads=0

if tromlogging==1:
	tromlog1=open(os.path.join('CAP', "libtrom.log"), "w")




#load TROMS from TROM files to respective dictionaries
print "libtrom: parsing TROMs into dictionaries..."
if tromlogging==1:
	tromlog1.write("Load TROMs into dictionaries... \n")
AROM= {}
TROMAfile=open(TROMA, "r")
linecnt=1
for rmline in TROMAfile:
	rmline=rmline.replace("\n", "")
	AROM[linecnt]=rmline
	linecnt += 1
BROM= {}
TROMBfile=open(TROMB, "r")
linecnt=1
for rmline in TROMBfile:
	rmline=rmline.replace("\n", "")
	BROM[linecnt]=rmline
	linecnt += 1
CROM= {}
TROMCfile=open(TROMC, "r")
linecnt=1
for rmline in TROMCfile:
	rmline=rmline.replace("\n", "")
	CROM[linecnt]=rmline
	linecnt += 1
DROM= {}
TROMDfile=open(TROMD, "r")
linecnt=1
for rmline in TROMDfile:
	rmline=rmline.replace("\n", "")
	DROM[linecnt]=rmline
	linecnt += 1
EROM= {}
TROMEfile=open(TROME, "r")
linecnt=1
for rmline in TROMEfile:
	rmline=rmline.replace("\n", "")
	EROM[linecnt]=rmline
	linecnt += 1
FROM= {}
TROMFfile=open(TROMF, "r")
linecnt=1
for rmline in TROMFfile:
	rmline=rmline.replace("\n", "")
	FROM[linecnt]=rmline
	linecnt += 1
if tromlogging==1:
	tromlog1.write("Done.  Logging TROM filenames for refrence:\n")
	tromlog1.write("TROMA:" + TROMA + "\n")
	tromlog1.write("TROMB:" + TROMB + "\n")
	tromlog1.write("TROMC:" + TROMC + "\n")
	tromlog1.write("TROMD:" + TROMD + "\n")
	tromlog1.write("TROME:" + TROME + "\n")
	tromlog1.write("TROMF:" + TROMF + "\n")




libtromready=1

#read instruction function

def tromreadinst(romaddr, ROMNAME):
	line=libTDAcommon.numstruct(romaddr)
	#n = open(ROMNAME)
	linecnt=1
	#for fdelta in n:
	#	if linecnt==line:
	if ROMNAME==TROMA:
		fdelta=AROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROMA, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMB:
		fdelta=BROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROMB, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMC:
		fdelta=CROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROMC, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMD:
		fdelta=DROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROMD, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROME:
		fdelta=EROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROME, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMF:
		fdelta=FROM[line]
		if logreads==1:
			tromlog1.write("READ INST. TROMF, Addr:" + romaddr + " line:" + str(line) + "\n")
	dataret=((fdelta[0]) + (fdelta[1]) + (fdelta[2]) + (fdelta[3]))
			
	return dataret
	#	linecnt += 1

#set data function

def tromsetdata(romaddr, datax, ROMNAME):
	line=libTDAcommon.numstruct(romaddr)
	global AROM
	global BROM
	global CROM
	global DROM
	global EROM
	global FROM
	if ROMNAME==TROMA:
		inst=(AROM[line])[0] + (AROM[line])[1] + (AROM[line])[2] + (AROM[line])[3]
		AROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROMA, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")
	elif ROMNAME==TROMB:
		inst=(BROM[line])[0] + (BROM[line])[1] + (BROM[line])[2] + (BROM[line])[3]
		BROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROMB, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")
	elif ROMNAME==TROMC:
		inst=(CROM[line])[0] + (CROM[line])[1] + (CROM[line])[2] + (CROM[line])[3]
		CROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROMC, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")
	elif ROMNAME==TROMD:
		inst=(DROM[line])[0] + (DROM[line])[1] + (DROM[line])[2] + (DROM[line])[3]
		DROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROMD, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")
	elif ROMNAME==TROME:
		inst=(EROM[line])[0] + (EROM[line])[1] + (EROM[line])[2] + (EROM[line])[3]
		EROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROME, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")
	elif ROMNAME==TROMF:
		inst=(FROM[line])[0] + (FROM[line])[1] + (FROM[line])[2] + (FROM[line])[3]
		FROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET DATA. TROMF, Addr:" + romaddr + " line:" + str(line) + " Data:" + datax + "\n")


#set instruction function


def tromsetinst(romaddr, inst, ROMNAME):
	line=libTDAcommon.numstruct(romaddr)
	global AROM
	global BROM
	global CROM
	global DROM
	global EROM
	global FROM
	if ROMNAME==TROMA:
		datax=(AROM[line])[4] + (AROM[line])[5] + (AROM[line])[6] + (AROM[line])[7] + (AROM[line])[8] + (AROM[line])[9]
		AROM[line]=(inst + datax)
		if logwrites==1:
			
			tromlog1.write("SET inst. TROMA, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")
	elif ROMNAME==TROMB:
		datax=(BROM[line])[4] + (BROM[line])[5] + (BROM[line])[6] + (BROM[line])[7] + (BROM[line])[8] + (BROM[line])[9]
		BROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET inst. TROMB, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")
	elif ROMNAME==TROMC:
		datax=(CROM[line])[4] + (CROM[line])[5] + (CROM[line])[6] + (CROM[line])[7] + (CROM[line])[8] + (CROM[line])[9]
		CROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET inst. TROMC, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")
	elif ROMNAME==TROMD:
		datax=(DROM[line])[4] + (DROM[line])[5] + (DROM[line])[6] + (DROM[line])[7] + (DROM[line])[8] + (DROM[line])[9]
		DROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET inst. TROMD, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")
	elif ROMNAME==TROME:
		datax=(EROM[line])[4] + (EROM[line])[5] + (EROM[line])[6] + (EROM[line])[7] + (EROM[line])[8] + (EROM[line])[9]
		EROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET inst. TROME, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")
	elif ROMNAME==TROMF:
		datax=(FROM[line])[4] + (FROM[line])[5] + (FROM[line])[6] + (FROM[line])[7] + (FROM[line])[8] + (FROM[line])[9]
		FROM[line]=(inst + datax)
		if logwrites==1:
			tromlog1.write("SET inst. TROMF, Addr:" + romaddr + " line:" + str(line) + " inst:" + inst + "\n")


	
def tromreaddata(romaddr, ROMNAME):
	line=libTDAcommon.numstruct(romaddr)
	#n = open(ROMNAME)
	linecnt=1
	if ROMNAME==TROMA:
		fdelta=AROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROMA, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMB:
		fdelta=BROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROMB, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMC:
		fdelta=CROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROMC, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMD:
		fdelta=DROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROMD, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROME:
		fdelta=EROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROME, Addr:" + romaddr + " line:" + str(line) + "\n")
	elif ROMNAME==TROMF:
		fdelta=FROM[line]
		if logreads==1:
			tromlog1.write("READ DATA. TROMF, Addr:" + romaddr + " line:" + str(line) + "\n")
	#for fdelta in n:
	#	if linecnt==line:
	dataret=((fdelta[4]) + (fdelta[5]) + (fdelta[6]) + (fdelta[7]) + (fdelta[8]) + (fdelta[9]))
	return dataret
	#	linecnt += 1


def dumptroms():
	ROMAdmp=open(os.path.join('CAP', "TROMA.dmp"), "w")
	#itercnt=1
	for itm in AROM:
		ROMAdmp.write(AROM[itm])
		ROMAdmp.write('\n')
	ROMAdmp.close()
	ROMBdmp=open(os.path.join('CAP', "TROMB.dmp"), "w")
	#itercnt=1
	for itm in BROM:
		ROMBdmp.write(BROM[itm])
		ROMBdmp.write('\n')
	ROMBdmp.close()
	ROMCdmp=open(os.path.join('CAP', "TROMC.dmp"), "w")
	#itercnt=1
	for itm in CROM:
		ROMCdmp.write(CROM[itm])
		ROMCdmp.write('\n')
	ROMCdmp.close()
	ROMDdmp=open(os.path.join('CAP', "TROMD.dmp"), "w")
	#itercnt=1
	for itm in DROM:
		ROMDdmp.write(DROM[itm])
		ROMDdmp.write('\n')
	ROMDdmp.close()
	ROMEdmp=open(os.path.join('CAP', "TROME.dmp"), "w")
	#itercnt=1
	for itm in EROM:
		ROMEdmp.write(EROM[itm])
		ROMEdmp.write('\n')
	ROMEdmp.close()
	ROMFdmp=open(os.path.join('CAP', "TROMF.dmp"), "w")
	#itercnt=1
	for itm in FROM:
		ROMFdmp.write(FROM[itm])
		ROMFdmp.write('\n')
	ROMFdmp.close()

def manualdumptroms():
	ROMAdmp=open(os.path.join('CAP', "TROMAman.dmp"), "w")
	#itercnt=1
	for itm in AROM:
		ROMAdmp.write(AROM[itm])
		ROMAdmp.write('\n')
	ROMAdmp.close()
	ROMBdmp=open(os.path.join('CAP', "TROMBman.dmp"), "w")
	#itercnt=1
	for itm in BROM:
		ROMBdmp.write(BROM[itm])
		ROMBdmp.write('\n')
	ROMBdmp.close()
	ROMCdmp=open(os.path.join('CAP', "TROMCman.dmp"), "w")
	#itercnt=1
	for itm in CROM:
		ROMCdmp.write(CROM[itm])
		ROMCdmp.write('\n')
	ROMCdmp.close()
	ROMDdmp=open(os.path.join('CAP', "TROMDman.dmp"), "w")
	#itercnt=1
	for itm in DROM:
		ROMDdmp.write(DROM[itm])
		ROMDdmp.write('\n')
	ROMDdmp.close()
	ROMEdmp=open(os.path.join('CAP', "TROMEman.dmp"), "w")
	#itercnt=1
	for itm in EROM:
		ROMEdmp.write(EROM[itm])
		ROMEdmp.write('\n')
	ROMEdmp.close()
	ROMFdmp=open(os.path.join('CAP', "TROMFman.dmp"), "w")
	#itercnt=1
	for itm in FROM:
		ROMFdmp.write(FROM[itm])
		ROMFdmp.write('\n')
	ROMFdmp.close()


#print(tromreadinst("------", "BOOTUP.TROM"))
#print(tromreaddata("------", "BOOTUP.TROM"))



