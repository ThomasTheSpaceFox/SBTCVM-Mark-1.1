#!/usr/bin/env python

#primary character code lookup dictionary
charcodedict = {"------": "a", "-----0": "b", "-----+": "c", "----0-": "d", "----00": "e", "----0+": "f", "----+-": "g", "----+0": "h", "----++": "i", "---0--": "j", "---0-0": "k", "---0-+": "l", "---00-": "m", "---000": "n", "---00+": "o", "---0+-": "p", "---0+0": "q", "---0++": "r", "---+--": "s", "---+-0": "t", "---+-+": "u", "---+0-": "v", "---+00": "w", "---+0+": "x", "---++-": "y", "---++0": "z", "---+++": "A", "--0---": "B", "--0--0": "C", "--0--+": "D", "--0-0-": "E", "--0-00": "F", "--0-0+": "G", "--0-+-": "H", "--0-+0": "I", "--0-++": "J", "--00--": "K", "--00-0": "L", "--00-+": "M", "--000-": "N", "--0000": "O", "--000+": "P", "--00+-": "Q", "--00+0": "R", "--00++": "S", "--0+--": "T", "--0+-0": "U", "--0+-+": "V", "--0+0-": "W", "--0+00": "X", "--0+0+": "Y", "--0++-": "Z", "--0++0": "0", "--0+++": "1", "--+---": "2", "--+--0": "3", "--+--+": "4", "--+-0-": "5", "--+-00": "6", "--+-0+": "7", "--+-+-": "8", "--+-+0": "9", "--+-++": "`", "--+0--": "~", "--+0-0": "!", "--+0-+": "@", "--+00-": "#", "--+000": "$", "--+00+": "%", "--+0+-": "^", "--+0+0": "&", "--+0++": "*", "--++--": "(", "--++-0": ")", "--++-+": "-", "--++0-": "=", "--++00": "_", "--++0+": "+", "--+++-": "[", "--+++0": "]", "--++++": "\\", "-0----": "{", "-0---0": "}", "-0---+": "|", "-0--0-": ";", "-0--00": "\'", "-0--0+": ",", "-0--+-": ".", "-0--+0": "/", "-0--++": ":", "-0-0--": '\"', "-0-0-0": "<", "-0-0-+": ">", "-0-00-": "?", "-0-000": "\n", "-0-00+": " "}
#primary character lookup dictionary (returns code of a character)
charlookupdict={"a": "------", "b": "-----0", "c": "-----+", "d": "----0-", "e": "----00", "f": "----0+", "g": "----+-", "h": "----+0", "i": "----++", "j": "---0--", "k": "---0-0", "l": "---0-+", "m": "---00-", "n": "---000", "o": "---00+", "p": "---0+-", "q": "---0+0", "r": "---0++", "s": "---+--", "t": "---+-0", "u": "---+-+", "v": "---+0-", "w": "---+00", "x": "---+0+", "y": "---++-", "z": "---++0", "A": "---+++", "B": "--0---", "C": "--0--0", "D": "--0--+", "E": "--0-0-", "F": "--0-00", "G": "--0-0+", "H": "--0-+-", "I": "--0-+0", "J": "--0-++", "K": "--00--", "L": "--00-0", "M": "--00-+", "N": "--000-", "O": "--0000", "P": "--000+", "Q": "--00+-", "R": "--00+0", "S": "--00++", "T": "--0+--", "U": "--0+-0", "V": "--0+-+", "W": "--0+0-", "X": "--0+00", "Y": "--0+0+", "Z": "--0++-", "0": "--0++0", "1": "--0+++", "2": "--+---", "3": "--+--0", "4": "--+--+", "5": "--+-0-", "6": "--+-00", "7": "--+-0+", "8": "--+-+-", "9": "--+-+0", "`": "--+-++", "~": "--+0--", "!": "--+0-0", "@": "--+0-+", "#": "--+00-", "$": "--+000", "%": "--+00+", "^": "--+0+-", "&": "--+0+0", "*": "--+0++", "(": "--++--", ")": "--++-0", "-": "--++-+", "=": "--++0-", "_": "--++00", "+": "--++0+", "[": "--+++-", "]": "--+++0", "\\": "--++++", "{": "-0----", "}": "-0---0", "|": "-0---+", ";": "-0--0-", "\'": "-0--00", ",": "-0--0+", ".": "-0--+-", "/": "-0--+0", ":": "-0--++", '\"': "-0-0--", "<": "-0-0-0", ">": "-0-0-+", "?": "-0-00-", "\n": "-0-000", " ": "-0-00+"}
#character gliph table.
chargliph={"a": "chara.gif", "b": "charb.gif", "c": "charc.gif", "d": "chard.gif", "e": "chare.gif", "f": "charf.gif", "g": "charg.gif", "h": "charh.gif", "i": "chari.gif", "j": "charj.gif", "k": "chark.gif", "l": "charl.gif", "m": "charm.gif", "n": "charn.gif", "o": "charo.gif", "p": "charp.gif", "q": "charq.gif", "r": "charr.gif", "s": "chars.gif", "t": "chart.gif", "u": "charu.gif", "v": "charv.gif", "w": "charw.gif", "x": "charx.gif", "y": "chary.gif", "z": "charz.gif", "A": "charAc.gif", "B": "charBc.gif", "C": "charCc.gif", "D": "charDc.gif", "E": "charEc.gif", "F": "charFc.gif", "G": "charGc.gif", "H": "charHc.gif", "I": "charIc.gif", "J": "charJc.gif", "K": "charKc.gif", "L": "charLc.gif", "M": "charMc.gif", "N": "charNc.gif", "O": "charOc.gif", "P": "charPc.gif", "Q": "charQc.gif", "R": "charRc.gif", "S": "charSc.gif", "T": "charTc.gif", "U": "charUc.gif", "V": "charVc.gif", "W": "charWc.gif", "X": "charXc.gif", "Y": "charYc.gif", "Z": "charZc.gif", "0": "char0.gif", "1": "char1.gif", "2": "char2.gif", "3": "char3.gif", "4": "char4.gif", "5": "char5.gif", "6": "char6.gif", "7": "char7.gif", "8": "char8.gif", "9": "char9.gif", "`": "characcent.gif", "~": "chartild.gif", "!": "charexclaim.gif", "@": "charAT.gif", "#": "charhash.gif", "$": "charUSD.gif", "%": "charPERC.gif", "^": "charCARROT.gif", "&": "charAND.gif", "*": "charATRISK.gif", "(": "charLPAR.gif", ")": "charRPAR.gif", "-": "charHYPHON.gif", "=": "charEQUAL.gif", "_": "charUNDERSC.gif", "+": "charPLUS.gif", "[": "charLBRAK.gif", "]": "charRBRAK.gif", "\\": "charBKSLASH.gif", "{": "charLCURL.gif", "}": "charRCURL.gif", "|": "charVERTBAR.gif", ";": "charsemicol.gif", "\'": "charapos.gif", ",": "charcomma.gif", ".": "charpereod.gif", "/": "charFDSLASH.gif", ":": "charcol.gif", '\"': "charDUBQTE.gif", "<": "charLESSTHAN.gif", ">": "charGREATTHAN.gif", "?": "charquestion.gif", " ": "charSPACE.gif"}

#primary character list. use to check if a character has a valid code
charscrossck=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "_", "+", "[", "]", "\\", "{", "}", "|", ";", "\'", ",", ".", "/", ":", '\"', "<", ">", "?", "\n", " "]

def charcodelook(code):
	return(charcodedict[code])

def charlook(char):
	return(charlookupdict[char])

#print(charcodelook("-0--00"))
#print(charlook("a"))
	
