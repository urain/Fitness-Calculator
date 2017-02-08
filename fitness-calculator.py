#Fitness Calculator

import os
import re

def menu():
	os.system('clear')

	waist 	= 0
	pushups = 0
	situps 	= 0
	run 	= 0
	choice 	= 0
	while choice != 6:
		currentScore = updateScore(waist,pushups,situps,run)
		print "#   OPTIONS                    Amount\t\tPoints" 
		print "-   -------                    ------\t\t------"
		print "1 - Enter All Results"
		print "2 - Update Waist               %.2f\t\t%.2f" % (waist,checkWaist(waist))
		print "3 - Update Pushups             %02d\t\t%.2f" % (pushups,checkPushups(pushups))
		print "4 - Update Situps              %02d\t\t%.2f" % (situps,checkSitups(situps))
		print "5 - Update Run                 %.2f\t\t%.2f" % (run,checkRun(run))
		print "6 - Quit"
		print "                                   Total Score: %.2f" % currentScore
		try:
			choice = input(">> ")
			if choice == 1:
				waist 	= getWaist()
				pushups = getPushups()
				situps 	= getSitups()
				run 	= getRun()
			elif choice == 2:
				waist 	= getWaist()
			elif choice == 3:
				pushups = getPushups()
			elif choice == 4:
				situps 	= getSitups()
			elif choice == 5:
				run 	= getRun()
			os.system('clear')


		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			os.system('clear')
			print "[*] INVALID INPUT\n"
			


def getWaist():
	i = 0
 	while i != 1:
 		try:
 			waist = raw_input("Enter Waist Measurement: ")
 			waist = float(re.sub('[\D]','.',waist))
 			if isinstance(waist, int) or isinstance(waist, float):
 				i = 1
				return waist
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			print "invalid input"


def getPushups():
	i = 0
 	while i != 1:
 		try:
 			pushups = input("Enter Pushups: ")
 			if isinstance(pushups, int):
 				i = 1
				return pushups
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			print "invalid input"


def getSitups():
	i = 0
 	while i != 1:
 		try:
 			situps = input("Enter Situps: ")
 			if isinstance(situps, int):
 				i = 1
				return situps
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			print "invalid input"


def getRun():
	i = 0
 	while i != 1:
 		try:
 			run = raw_input("Enter Run: ")
 			run = float(re.sub('[\D]','.',run))

 			if isinstance(run, int) or isinstance(run, float) or isinstance(run, str):
 				i = 1
				return run
		except (KeyboardInterrupt, SystemExit):
			raise
		except:
			print "invalid input"

def updateScore(waist,pushups,situps,run):
	waist = checkWaist(waist)
	pushups = checkPushups(pushups)
	situps = checkSitups(situps)
	run = checkRun(run)
	total = waist + pushups + situps + run
	return total

def checkWaist(waist):
	wDict = {
				35.0: 20.0,
				35.5: 17.6,
				36.0: 17.0,
				36.5: 16.4,
				37.0: 15.8,
				37.5: 15.1,
				38.0: 14.4,
				38.5: 13.5,
				39.0: 12.6
			}
	if waist < 35.0 and waist != 0:
		return 20.0
	elif waist > 39.0:
		return 0
	elif waist >= 35.0 and waist <= 39.0:
		key = wDict[max(k for k in wDict if k <= waist)]
		return key
	else:
		return 0

def checkPushups(pushups):
	pDict = {
				33: 5.0,
				34: 5.3,
				35: 5.5,
				36: 5.8,
				37: 6.0,
				38: 6.3,
				39: 6.5,
				40: 6.8,
				41: 7.0,
				42: 7.2,
				43: 7.3,
				44: 7.5,
				45: 7.7,
				46: 7.8,
				47: 8.0,
				48: 8.1,
				49: 8.3,
				50: 8.4,
				51: 8.5,
				52: 8.6,
				53: 8.7,
				54: 8.8,
				55: 8.8,
				56: 8.9,
				57: 9.0,
				58: 9.1,
				59: 9.2,
				60: 9.3,
				61: 9.4,
				62: 9.5,
				67: 10.0
			}
	if pushups < 33:
		return 0
	elif pushups > 67:
		return 10
	elif pushups >= 33 and pushups <=67:
		key = pDict[max(k for k in pDict if k <= pushups)]
		return key
	else:
		return 0

def checkSitups(situps):
	sDict = {
				42: 6.0,
				43: 6.3,
				44: 6.5,
				45: 7.0,
				46: 7.5,
				47: 8.0,
				48: 8.3,
				49: 8.5,
				50: 8.7,
				51: 8.8,
				52: 9.0,
				53: 9.2,
				54: 9.4,
				55: 9.5,
				58: 10.0
			}
	if situps < 42:
		return 0
	elif situps > 58:
		return 10
	elif situps >= 42 and situps <=58:
		key = sDict[max(k for k in sDict if k <= situps)]
		return key
	else:
		return 0

def checkRun(run):
	rDict = {
				9.12: 60.0,
				9.13: 59.7,
				9.35: 59.3,
				9.46: 58.9,
				9.59: 58.5,
				10.11: 57.9,
				10.24: 57.3,
				10.38: 56.6,
				10.52: 55.7,
				11.07: 54.8,
				11.23: 53.7,
				11.39: 52.4,
				11.57: 50.9,
				12.15: 49.2,
				12.34: 47.2,
				12.54: 44.9,
				13.15: 42.3
			}
	if run < 9.12 and run != 0:
		return 60.0
	elif run > 13.36:
		return 0
	elif run >= 9.12 and run <= 13.36:
		key = rDict[max(k for k in rDict if k <= run)]
		return key
	else:
		return 0

menu()

