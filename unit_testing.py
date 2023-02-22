# -------------------
# Gabriel Souza
# CS 555 Sprint 1
# -------------------

import unittest

from gs_error_functions import *

class TestUserStoryOne(unittest.TestCase):	

	print ("US01 - Dates before current date")

	def testCurrentDate(self):
		print()

		today = date.today()
		testDate =  date.today()
		isBefore = dateBeforeToday(today, testDate)

		print("comparing the same dates")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayBefore(self):
		print()

		today = date.today()
		testDate = today - timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("comparing with the day before")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayAfter(self):
		print()

		today = date.today()
		testDate = today + timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("comparing with the day after")
		print (today, testDate, isBefore)

		self.assertFalse(isBefore)
		
	def testThreeYearsBefore(self):
		print()

		today = date.today()
		testDate = today - timedelta(days = 1000)
		isBefore = dateBeforeToday(today, testDate)

		print("comparing with three years before")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testFiveYearsAfter(self):
		print()

		today = date.today()
		testDate = today + timedelta(days = 1900)
		isBefore = dateBeforeToday(today, testDate)

		print("comparing with five years after")
		print (today, testDate, isBefore)

		self.assertFalse(isBefore)






'''		
class TestUserStoryNine(unittest.TestCase):	

	print("US09 - Birth before death of parents")
	print()
	print("Mother - tests")

	def testMomDeathSameDate(self):
		print()
		birth = date.today()
		death =  date.today()
		print("comparing the same dates")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertTrue(isBefore)

	def testMomDeathDayBefore(self):
		print()
		birth = date(2021, 2, 28)
		death = date(2021, 2, 27)
		print("comparing with the day before")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertFalse(isBefore)

	def testMomDeathDayAfter(self):
		print()
		birth = date(2020, 2, 29)
		death = date(2020, 3, 1)
		print("comparing with the day after")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertTrue(isBefore)
		
	def testMomDeathNineMonthsBefore(self):
		print()
		birth = date.today()
		death = birth - timedelta(days = 270)
		print("comparing with three years before")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertFalse(isBefore)

	def testMomDeath100WeeksAfter(self):
		print()
		birth = date.today()
		death = birth + timedelta(weeks = 100)
		print("comparing with five years after")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertTrue(isBefore)
'''