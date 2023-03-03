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
#list of individual ids
indis_id = []
#list of family ids
fams_id = []

# list of all GEDCOM errors in the source file
errors = []

# today's date for error checking and age calculation
currDate = date.today()

# read and evalute if each new line is in valid GEDCOM format, then populate individual and family arrays
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
				#US22 Unique IDs
				if args[1] not in indis_id: # check whether the individual IDs are unique or not
					indi = Individual(args[1]) # creates new individual object with id specified by args[1]
					indis.append(indi.info) # add object dict to list of individuals
					indis_id.append(args[1])
				else:
					errors.append("ERROR: INDIVIDUAL: US22 : Individual IDs are duplicate. Please provide correct ID.")
			else:
				#check whether the family ID is unique or not
				if args[1] not in fams_id:
					fam = Family(args[1]) # creates new family object with id specified by args[1]
					fams.append(fam.info) # add object dict to list of families
					fams_id.append(args[1])
				else:
					errors.append("ERROR: INDIVIDUAL: US22 : Family IDs are duplicate. Please provide correct ID.")

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

	# print(fams)
	print(indis)
	#US31 - List living single
	livingSingles= (listLivingSingle(indis,currDate)) # US3

	#US16 - All male members of a family should have the same last name
	err=verifyMaleMembersSurname(indis)

	#US18 - Siblings should not marry one another
	err2=verifySiblingsCannotMarry(fams,indis)


	errors.extend(err)
	errors.extend(err2)

	#US29 - List of deceased individuals
	list_of_deceased = []

	for person in indis:
		person = getAge(currDate, person)
		# print(person)
		# US07 - Less then 150 years old
		if AgeGreaterThan150(person):
			p_name=person["NAME"]
			p_age=str(person["AGE"])
			errors.append("ERROR: INDIVIDUAL: US07: " + p_name + " age (" + p_age + ") should be less than 150 years old ")			
		
		#US03 - Birth before death
		birth = person["BIRT"]

		if 'DEAT' in person:
			list_of_deceased.append(person)
			death = person["DEAT"]
			if birthBeforeDeath(birth, death):
				errors.append("Birth should occur before death of an individual")

		# US02 - Birth before Marriage
		if 'FAMS' in person:
			for family in person['FAMS']:

				famID = int(''.join(filter(str.isdigit, family)))
				marriageDate = searchByID(fams, len(fams)-1, 0, famID)['MARR']

				if birthBeforeMarriage(birth, marriageDate):
					errors.append("ERROR: INDIVIDUAL: US02: " + person["NAME"] + " birth " + birth.strftime("%x") + " should be before marriage " + marriageDate.strftime("%x") + ".")			

	for family in fams:
		#names of all the individuals in the family
		family_names = []
		# turn husband string ID into a number
		husbID = int(''.join(filter(str.isdigit, family["HUSB"])))
		husb = searchByID(indis, len(indis), 0, husbID)
		if not husb:
			raise Exception("Husband ID must exist.")
		else:
			family_names.append(husb['NAME'])

		# turn wife string ID into a number
		wifeID = int(''.join(filter(str.isdigit, family["WIFE"])))
		wife = searchByID(indis, len(indis), 0, wifeID)
		if not wife:
			raise Exception("Wife ID must exist.")
		else:
			family_names.append(wife['NAME'])

		family["HUSB NAME"] = husb["NAME"]
		family["WIFE NAME"] = wife["NAME"]
		
		# US05 - Marriage before death
		marr = family["MARR"]
		if 'DEAT' in husb:
			hdeath = husb["DEAT"]
			marriageBeforeDeath(marr, hdeath)
					
		if 'DEAT' in wife:
			wdeath = wife["DEAT"]
			marriageBeforeDeath(marr, wdeath)

		# US04 - Marriage before divorce
		if 'DIV' in family:
			divorce = family["DIV"]
			if marriageBeforeDivorce(marr, divorce):
					errors.append("ERROR: FAMILY: US04: " + family["ID"] + " marriage " + marr.strftime("%x") + " should be before divorce " + divorce.strftime("%x") + ".")

		# US10 - Marriage after 14
		hbirth = husb["BIRT"]
		wbirth = wife["BIRT"]
		
		if marriageAfter14(hbirth, marr):
			errors.append("Marriage should be at least 14 years after birth of husband")
		if marriageAfter14(wbirth, marr):
			errors.append("Marriage should be at least 14 years after birth of wife")
 
		# US09 - Birth before death of parents
		if "CHIL" in family:
			for childStringID in family["CHIL"]:
				childID = int(''.join(filter(str.isdigit, childStringID)))
				child = searchByID(indis, len(indis), 0, childID)
				if not child:
					raise Exception("Wife ID must exist.")
				else:
					family_names.append(child['NAME'])
	
				childBirthdate = child["BIRT"]


				if not wife["ALIVE"] and not birthBeforeMomDeath(childBirthdate, wife["DEAT"]):
					errors.append("ERROR: FAMILY: US09: " + family["ID"] + ": Child " + childStringID + ": BIRT " + childBirthdate.strftime("%x") + " after DEAT of mother on " + wife["DEAT"].strftime("%x") + ".")

				if not husb["ALIVE"] and not birthBeforeDadDeath(childBirthdate, husb["DEAT"]):
					errors.append("ERROR: FAMILY: US09: " + family["ID"] + ": Child " + childStringID + ": BIRT " + childBirthdate.strftime("%x") + " 9 months after DEAT of father on " + husb["DEAT"].strftime("%x") + ".")

				#US08 - Birth before the marriage of parents(and no more than 9 months after their divorce)
				if "DIV" in family:
					divorce = family["DIV"]
					if birthbeforeDivorceofParents(divorce, childBirthdate):
						errors.append("ERROR : FAMILY: US08: " + family["ID"] + ": Child " + childStringID + ": BIRT " + childBirthdate.strftime("%x") + " should be no more than 9 months after the divorce of the parents on " + marr.strftime("%x") + ".")
				else:		
					if birthBeforeMarriageofParents(marr, childBirthdate):
						errors.append("ERROR : FAMILY: US08: " + family["ID"] + ": Child " + childStringID + ": BIRT " + childBirthdate.strftime("%x") + " should be after marriage " + marr.strftime("%x") + ".")

		result = Family_names(family_names)
		if result :
			errors.append("ERROR: INDIVIDUAL: US25 : First names of individuals in the family cannot be same.")
			

	
	# write table results to a new file
	outfile = open(filename + ".txt", "w")

	outfile.write(tabulate(indis, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')
	outfile.write(tabulate(fams, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')

	outfile.write('Living people over 30 who have never been married\n')
	outfile.write(tabulate(livingSingles, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')

	outfile.write('List of deceased individuals\n')
	outfile.write(tabulate(list_of_deceased, headers = "keys", tablefmt="github"))
	outfile.write('\n\n')

	outfile.write('ERRORS\n')	
	for error in errors:
		outfile.write(error)
		outfile.write('\n')	

	outfile.close()


init()
sys.exit();
