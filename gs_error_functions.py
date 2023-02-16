# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------
# This is statement is required by the build system to query build infos

from datetime import date, datetime, timedelta
	
# US01 - Dates before current date
def dateBeforeToday(today, date):
	return (today.year - date.year - ((today.month, today.day) < (date.month, date.day))) >= 0

# US09 - Birth before death of parents
def birthBeforeMomDeath(birth, momDeath):
	return (momDeath.year - birth.year - ((momDeath.month, momDeath.day) < (birth.month, birth.day))) >= 0

def birthBeforeDadDeath(birth, dadDeath):
	# calculate from 40 weeks (abt. 9 months) before dad's death
	dadDeath -= timedelta(weeks = 40)
	return (dadDeath.year - birth.year - ((dadDeath.month, dadDeath.day) < (birth.month, birth.day))) >= 0

