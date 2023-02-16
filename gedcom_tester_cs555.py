#!/usr/bin/python

# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------

from tabulate import tabulate

from gs_error_functions import *
from general_functions import *


# This is statement is required by the build system to query build infos
if __name__ == '__build__':
	raise Exception;

import sys;

# creates a new "person" object
class Individual:
	def __init__(self, id):
		self.info = {'ID': id} # dict to save individual information


# creates a new "family" object
class Family:
	def __init__(self, id):
		self.info = {'ID': id} # dict to save family information
	   

# all the valid tags for the project, along with their corresponding levels
validTags = {
	'0': [{'HEAD', 'TRLR', 'NOTE'}, {'INDI', 'FAM'}],
	'1': [{'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS'}, {'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'}],
	'2': {'DATE'},
};

# list of all individuals
indis = []
# list of all families
fams = []

# list of all GEDCOM errors in the source file
errors = []

# today's date for error checking and age calculation
currDate = date.today()
	
# read and evalute if each new line is in valid GEDCOM format
def readLine(fileLine):
	args = fileLine.split();

	# end of file check
	if not args: 
		return;

	# valid level check (cannot go past level 2)
	if args[0] not in validTags:
		print(validOutput(fileLine, args, 'N'))
		raise Exception("Please provide a valid level number") 

	if args[0] == '0':

		if args[1] in validTags[args[0]][0]:
			return # these tags aren''t needed
		
		# individual and family id tags have a different format
		elif args[2] in validTags[args[0]][1]:
			if args[2] == 'INDI':
				indi = Individual(args[1]) # creates new individual object with id specified by args[1]
				indis.append(indi.info) # add object dict to list of individuals
			else:
				fam = Family(args[1]) # creates new family object with id specified by args[1]
				fams.append(fam.info) # add object dict to list of families

		# valid tag check (must be a tag specified in valid tags)
		else:
			print(validOutput(fileLine, args, 'N'))
			raise Exception("Please provide a valid id tag in the proper format") 

	elif args[0] == '1':

		# these tags specify certain information for the individual it describes 
		if args[1] in validTags[args[0]][0]: 
			# FAMS information should be a list of strings since you can have multiple spouses
			if args[1] == 'FAMS':
				if args[1] not in indis[len(indis)-1]:
					indis[len(indis)-1][args[1]] = [' '.join(args[2:])]
				else:
					indis[len(indis)-1][args[1]].append(' '.join(args[2:]))

			# store the infomation for the most recent person added to the "indis" list
			elif len(args) > 2:
				indis[len(indis)-1][args[1]] = ' '.join(args[2:]) 

			else:
				# information is within a nested date tag and not on the same line, save the tag for later
				indis.append(args[1])

		# these tags specify certain information for the family it describes 		
		elif args[1] in validTags[args[0]][1]: 
			
			# CHIL information should be a list of strings since you can have multiple children
			if args[1] == 'CHIL':
				if args[1] not in fams[len(fams)-1]:
					fams[len(fams)-1][args[1]] = [' '.join(args[2:])]
				else:
					fams[len(fams)-1][args[1]].append(' '.join(args[2:]))

			# store the infomation for the most recent family added to the "fams" list
			elif len(args) > 2:
				fams[len(fams)-1][args[1]] = ' '.join(args[2:]) 
			
			# information is within a nested date tag and not on the same line, save the tag for later
			else:
				fams.append(args[1]) 
		
		# valid tag check (must be a tag specified in valid tags)
		else:
			print(validOutput(fileLine, args, 'N'))
			raise Exception("Please provide a valid tag in the proper format") 

	# date tag - take the previous saved string tag and add date information to the previously saved object in array
	elif args[1] in validTags[args[0]]:
		date = dateConversion(' '.join(args[2:]))

		# makes sure the previously saved object in the array is the necessary string tag
		if isinstance(indis[len(indis)-1], str): 
			tag = indis.pop()
			indis[len(indis)-1][tag] = date
			
			# US01 - Dates before current date
			if not dateBeforeToday(currDate, date):
				errors.append("ERROR: INDIVIDUAL: US01: " + indis[len(indis)-1]["ID"] + ": " + tag + " "+ date.strftime("%x") + " occurs in the future.")
		
		# makes sure the previously saved object in the array is the necessary string tag
		elif isinstance(fams[len(fams)-1], str):
			tag = fams.pop()
			fams[len(fams)-1][tag] = date

			# US01 - Dates before current date
			if not dateBeforeToday(currDate, date):
				errors.append("ERROR: FAMILY: US01: " + fams[len(indis)-1]["ID"], ": " + tag + " "+ date.strftime("%x") + " occurs in the future.")

		# throw error if date tag does not proceed a level 1 tag)
		else:
			print(validOutput(fileLine, args, 'N'))
			raise Exception("Please make sure your DATE tag belongs to a valid tag") 
	else:
		print(validOutput(fileLine, args, 'N'))
		raise Exception("Improper GEDCOM format") 	

	return


# main method
def init():
	try:
		filename = input("Please enter the name of the file (defaults to test3.ged if no file given): ")
		if(filename==""):
			filename="test3.ged"
		with open(filename, 'r') as infile:
			for line in infile:
				readLine(line);
	except FileNotFoundError:
		print ('''
		ERROR: GEDCOM file does not exist.
		''');
		sys.exit();

	# sort each list by their ID nums
	indis.sort(key=lambda info: int(''.join(filter(str.isdigit, info["ID"]))))
	fams.sort(key=lambda info: int(''.join(filter(str.isdigit, info["ID"]))))

	for person in indis:
		person = getAge(currDate, person)

	for family in fams:
		# turn husband string ID into a number
		husbID = int(''.join(filter(str.isdigit, family["HUSB"])))
		husbName = searchID(indis, len(indis), 0, husbID)

		# turn wife string ID into a number
		wifeID = int(''.join(filter(str.isdigit, family["WIFE"])))
		wifeName = searchID(indis, len(indis), 0, wifeID)

		if not husbName or not wifeName: # ID not found in list
			print(wifeID, husbID)
			raise Exception("Family Husband and Wife IDs must exist.")

		family["HUSB NAME"] = husbName
		family["WIFE NAME"] = wifeName

	
	# write table results to a new file
	outfile = open(filename + ".txt", "w")

	outfile.write(tabulate(indis, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')
	outfile.write(tabulate(fams, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')

	for error in errors:
		outfile.write(error)
		outfile.write('\n')	

	outfile.close()


init()
sys.exit();
