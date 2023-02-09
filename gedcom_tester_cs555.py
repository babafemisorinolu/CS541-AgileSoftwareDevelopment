valid_tags = {'0': ["HEAD", "NOTE", "TRLR", "FAM", "INDI"],
    '1': ["BIRT", "CHIL", "DEAT", "DIV", "FAMC", "FAMS", "HUSB","MARR", "NAME", "SEX", "WIFE"],
    '2': ["DATE"], '3': []}
    


def analyze_gedcom_line(line):
    arr=line.split(" ")
    
    res=""
    if(arr[0]=="0") and (("INDI" in arr) or ("FAM" in arr)):
        res=arr[0]+"|"+arr[2]+"|Y|"+arr[1]
    elif arr[1] in valid_tags[arr[0]]:
        res=arr[0]+"|"+arr[1]+"|Y|"+" ".join(arr[2:])
    else:
        res=arr[0]+"|"+arr[1]+"|N|"+" ".join(arr[2:])
    return res
    
print('Program that Reads each line of a GEDCOM file')
filename=input ("Please enter the name of the file")
if(filename==""):
    filename="GEDCOM_export-Forest.ged"
try:
    gedcom_file = open(filename, 'r')
except FileNotFoundError:
    raise FileNotFoundError(f"Can't open {path}")

with gedcom_file:
    for line in gedcom_file:
        line = line.rstrip()
        print("--> ",line)
        output_analysis=analyze_gedcom_line(line)
        print("<-- ",output_analysis)
        

