# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------

from datetime import date, datetime, timedelta

# used for all user stories that compares Dates
# earlierDate returns true if it is before laterDate, else returns false 
def compareDates(earlierDate, laterDate):
	return laterDate.year - earlierDate.year - ((laterDate.month, laterDate.day) < (earlierDate.month, earlierDate.day)) >= 0

#US42 - Reject illegitimate dates
def invalidDate(dates):
    return dates.month > 12
