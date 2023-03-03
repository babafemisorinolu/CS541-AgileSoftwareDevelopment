# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------

from datetime import date, datetime
from itertools import groupby
 
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