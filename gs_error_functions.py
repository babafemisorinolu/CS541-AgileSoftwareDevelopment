# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------

from datetime import date, datetime, timedelta
	
# US01 - Dates before current date
def dateBeforeToday(today, date):
	return today.year - date.year - ((today.month, today.day) < (date.month, date.day)) >= 0

# US09 - Birth before death of parents
def birthBeforeMomDeath(birth, momDeath):
	return momDeath.year - birth.year - ((momDeath.month, momDeath.day) < (birth.month, birth.day)) >= 0

def birthBeforeDadDeath(birth, dadDeath):
	# calculate from 40 weeks (abt. 9 months) before dad's death
	dadDeath -= timedelta(weeks = 40)
	return dadDeath.year - birth.year - ((dadDeath.month, dadDeath.day) < (birth.month, birth.day)) >= 0

#US03 - Birth before Death
def birthBeforeDeath(birth, death):
    return birth.year - death.year - ((death.month, death.day) < (birth.month, birth.day)) >= 0

#US10 - Marriage after 14
def marriageAfter14(bdate, mdate):
    return bdate.year - mdate.year - ((mdate.month, mdate.day) < (bdate.month, bdate.day)) > 14

# US02 - Birth before marriage
def birthBeforeMarriage(birth, marriage):
	return birth.year - marriage.year - ((birth.month, birth.day) < (marriage.month, marriage.day)) >= 0

# US05 - Marriage before death
def marriageBeforeDeath(marriage,death):
	return marriage.year - death.year - ((marriage.month, marriage.day) < (death.month, death.day)) >= 0
	
# US04 - Marriage before divorce
def marriageBeforeDivorce(marriage,divorce):
	return marriage.year - divorce.year - ((marriage.month, marriage.day) < (divorce.month, divorce.day)) >= 0

# US08 - Birth before marriage of parents
def birthBeforeMarriageofParents(marriage,birthchild):
	return marriage.year - birthchild.year - ((marriage.month, marriage.day) < (birthchild.month , birthchild.day)) >=  0

def birthbeforeDivorceofParents(childBirthdate, divorce):
	divorce -= timedelta(weeks = 40)
	return divorce.year - childBirthdate.year - ((divorce.month, divorce.day) < (childBirthdate.month, childBirthdate.day)) >= 0

# US02 - Birth before marriage
def birthBeforeMarriage(birth, marriage):
	return birth.year - marriage.year - ((birth.month, birth.day) < (marriage.month, marriage.day)) >= 0