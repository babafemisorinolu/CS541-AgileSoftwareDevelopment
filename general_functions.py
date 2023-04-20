# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------

from datetime import date, datetime, timedelta
from itertools import groupby
import collections
from collections import Counter

# convert string to datetime object
def dateConversion(date):
    try:
        return datetime.strptime(date, '%d %b %Y').date()
    except:
        raise Exception("Date should be in the format 'Day (Abbreviated)Month Year'; ex. 9 AUG 2022.")

# add date as a value with a key "tag" to dict object in array
def addDate(array, date, tag):
    date = dateConversion(' '.join(date))
    currObject = array[len(array)-1]
    currObject[tag] = date

    return currObject

# used for all user stories that compares Dates
# earlierDate returns true if it is before laterDate, else returns false 
def compareDates(earlierDate, laterDate):
	return laterDate.year - earlierDate.year - ((laterDate.month, laterDate.day) < (earlierDate.month, earlierDate.day)) >= 0

# add new error if date comparison does not pass
def dateError(earlierDate, laterDate, famID, userStory):
    newError = []
    if not compareDates(earlierDate, laterDate):
        newError.append("ERROR: FAMILY: " + userStory[0] + ": " + famID + ": " + userStory[1] + " " + earlierDate.strftime("%x") + " should be before " + userStory[2] + " " + laterDate.strftime("%x") + ".")
    return newError

#US42 - Reject illegitimate dates
def invalidDate(dates):
    return dates.month > 12


# print the input and output of each new line 
def validOutput(fileLine, args, isValid):
    returnOutput = "--> {0}\n".format(fileLine.rstrip('\r\n'));
    returnOutput += "<-- ";

    # print output in the format "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
    for i in range(len(args)):
        returnOutput += args[i];
        if i == 0:
            returnOutput += "|";
        elif i == 1:
            returnOutput += "|{}|".format(isValid)
            if len(args) == 2:
                returnOutput += "\n";
        elif i < len(args)-1:
            returnOutput += " ";
        else:
            returnOutput += "\n";
            
    return returnOutput;

# calculates an individual's age and whether they are alive, adds this to their dictionary
def getAge(today, personInfo):
    birth = personInfo["BIRT"]
    if 'DEAT' in personInfo:
        death = personInfo["DEAT"]
        personInfo["AGE"] = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
        personInfo["ALIVE"] = False
    else:
        personInfo["AGE"] = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        personInfo["ALIVE"] = True
        
    return personInfo

# binary search through the list of objects to find the one with matching ID key
def searchByID(array, high, low, target):
    if high <= low:
        raise Exception("ID " + target + " not found.") 

    mid = (high+low)//2

    # turn midpoint string ID into a number
    midNum = int(''.join(filter(str.isdigit, array[mid]['ID'])))

    if midNum > target:
        return searchByID(array, mid, low, target)
    if midNum < target:
        return searchByID(array, high, mid+1, target)
    return array[mid]

#US31- List all living people over 30 who have never been married in a GEDCOM file
def listLivingSingle(indis,currDate):
    livingSingles=[]
    for person in indis:
        person = getAge(currDate, person)
        if("FAMS" not in person):
            # print("person[AGE]>30",person["AGE"], int(person["AGE"])>30)
            if (person["ALIVE"]==True and person["AGE"]>30):
                # print(person)
                livingSingles.append(person)
    return livingSingles

#US07 - Death should be less than 150 years after birth for dead people, 
#and current date should be less than 150 years after birth for all living people
def AgeGreaterThan150(person):
    if (person["AGE"]>=150):
        return True
    return False	

#US-25 First Names should be unique in the family
def Family_names(names):
    first_names = []
    for nam in names :
            names = nam.split(" ")
            first_names.append(names[0])

    result = {x for x in first_names if first_names.count(x) > 1}
    return result
    
#US16 - All male members of a family should have the same last name

# define a function for key
def key_func(k):
    if ("FAMC" in k):
        return k['FAMC']
    return "False"
 


def verifyMaleMembersSurname(individuals):
    errors=[]
    # sort INFO data by 'FAMC' key.
    INFO = sorted(individuals, key=key_func)
    for key, value in groupby(INFO, key_func):
        # print("hey",key)
        if(key=="False"):
            continue
            
        # print(list(value))   
        temp=list(value)
        if(len(temp)>1):
            full=""
            last_name=""
            # sex=""
            # print(full, last_name, sex)
            for v in temp:
                fn=v["NAME"]
                ln=fn.split(" ")[1]
                s=v["SEX"]
                # print(fn,ln,s)
                if(s=="M" and last_name==""):
                    full=fn
                    last_name=ln
                    # sex=s
                elif(s=="M" and last_name!=""):
                    if(last_name!=ln):
                        #All male members of a family should have the same last name
                        # print("ERROR: INDIVIDUAL: US16: " + full + " and " + fn + " are male members of a family and should have the same last name!")
                        errors.append("ERROR: INDIVIDUAL: US16: " + full + " and " + fn + " are male members of a family and should have the same last name!")			
            

        # print("*"*20, "\n")
    # print(errors)
    
    return errors
   
    
#US18 - Siblings should not marry one another
def verifySiblingsCannotMarry(family, individuals):
    #  print(individuals)
     errors=[]
     for nam in family :
         husb=nam["HUSB"]
         wife=nam["WIFE"]
         husb_details=next(item for item in individuals if item["ID"] == husb)
         wife_details=next(item for item in individuals if item["ID"] == wife)
        #  print(wife,husb)
        
         
         if ("FAMC" in husb_details):
             h_fid=husb_details["FAMC"]
         else:
          h_fid="husb"

         if ("FAMC" in wife_details):
             w_fid=wife_details["FAMC"]
         else:
            w_fid="wife"
         
         if(h_fid==w_fid):
            errors.append("ERROR: INDIVIDUAL: US18: " + husb_details["NAME"] + " and " + wife_details["NAME"] + " are siblings and should not marry one another!")			
             
        #  print("*"*20,"\n")
    #  print(errors)   
     return errors;

#US35 - Recent Birth
def listRecentBirth(today, birth):
    diff = today - birth
    return diff.days < 30

#US36 - Recent Deaths
def listRecentDeath(today, death):
    diff = today - death
    return diff.days < 30


#US14 - Multiple births
def multipleBirths(birthdates):
    birthdate_counts = {}
    for date in birthdates:
        if date in birthdate_counts:
            birthdate_counts[date] += 1
        else:
            birthdate_counts[date] = 1
    
    for count in birthdate_counts.values():
        if count > 5:
            return False
    
    return True


#US12 parents are too old
def Parentstooold(childBirthdate, parentBirthdate, years):
    return compareDates(childBirthdate, parentBirthdate + timedelta(days = years * 365.25))

#US32 List multiple births
#List all multiple births in a GEDCOM file
def listMultipleBirths(fams,indis):
    output=[]
    for family in fams:
        if 'CHIL' in family:
            children=family["CHIL"]
            dobs=[]
            multipledob=[]
            for i in children:
                 chilID = int(''.join(filter(str.isdigit, i)))
                 chil = searchByID(indis, len(indis), 0, chilID)
                 dob=chil['BIRT']   
                 dobs.append(dob)
                 multipledob=([item for item, count in collections.Counter(dobs).items() if count > 1])

            for i in children:
                 chilID = int(''.join(filter(str.isdigit, i)))
                 chil = searchByID(indis, len(indis), 0, chilID)
                 dob=chil['BIRT']   
                 if (dob in multipledob):
                     output.append(chil)
                         
    return output;

#US34 List large age differences
#List all couples who were married when the older spouse was more than twice as old as the younger spouse
def listLargeAgeDiff(fams,indis):
    output=[]
    for family in fams:
        
        husbID = int(''.join(filter(str.isdigit, family["HUSB"])))
        husb = searchByID(indis, len(indis), 0, husbID)
        wifeID = int(''.join(filter(str.isdigit, family["WIFE"])))
        wife = searchByID(indis, len(indis), 0, wifeID)
        #print(wife, husb)
        ages = [wife['AGE'],husb['AGE']]
        ages.sort()

        #print('wife age', wife['AGE'])
        #print('husb age', husb['AGE'])
        #print(ages)

        if(ages[1]>=2*ages[0]):
            output.append(family);    
        
    return output