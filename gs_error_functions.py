#!/usr/bin/python

# -------------------
# Team 1
# CS 555 Sprint 1
# -------------------
# This is statement is required by the build system to query build infos
if __name__ == '__build__':
	raise Exception;

from datetime import date, datetime
	
def dateBeforeToday(today, date):
	return (today.year - date.year - ((today.month, today.day) < (date.month, date.day))) >= 0
	


