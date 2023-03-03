import unittest
import sys

from gs_error_functions import *
from general_functions import *


# US01 - Dates before current date
class TestUserStoryOne(unittest.TestCase):	

	def testCurrentDate(self):
		print()

		today = date.today()
		testDate =  date.today()
		isBefore = dateBeforeToday(today, testDate)

		print("US01 - comparing the same dates")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayBefore(self):
		print()

		today = date.today()
		testDate = today - timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US01 - comparing with the day before")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayAfter(self):
		print()

		today = date.today()
		testDate = today + timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US01 - comparing with the day after")
		print (today, testDate, isBefore)

		self.assertFalse(isBefore)
		

# US02 - Birth before marriage
class TestUserStoryTwo(unittest.TestCase):	

	def testCurrentDate(self):
		print()

		today = date.today()
		testDate =  date.today()
		isBefore = dateBeforeToday(today, testDate)

		print("US02 - comparing the same dates")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayBefore(self):
		print()

		today = date.today()
		testDate = today - timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US02 - comparing with the day before")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayAfter(self):
		print()

		today = date.today()
		testDate = today + timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US02 - comparing with the day after")
		print (today, testDate, isBefore)

		self.assertFalse(isBefore)

# US04 - Marriage before divorce
class TestUserStoryFour(unittest.TestCase):	

	def testCurrentDate(self):
		print()

		today = date.today()
		testDate =  date.today()
		isBefore = dateBeforeToday(today, testDate)

		print("US04 - comparing the same dates")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayBefore(self):
		print()

		today = date.today()
		testDate = today - timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US04 - comparing with the day before")
		print (today, testDate, isBefore)

		self.assertTrue(isBefore)

	def testOneDayAfter(self):
		print()

		today = date.today()
		testDate = today + timedelta(days = 1)
		isBefore = dateBeforeToday(today, testDate)

		print("US04 - comparing with the day after")
		print (today, testDate, isBefore)

		self.assertFalse(isBefore)
		
	
# US09 - Birth before death of parents
class TestUserStoryNine(unittest.TestCase):	

	def testMomDeathSameDate(self):
		print()
		birth = date.today()
		death =  date.today()
		print("US09 - if death of mother was same day as birth")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertTrue(isBefore)

	def testMomDeathNineMonthsBefore(self):
		print()
		birth = date.today()
		death = birth - timedelta(days = 270)
		print("US09 - if death of mother was 9 months before")
		isBefore = birthBeforeMomDeath(birth, death)
		print (birth, death, isBefore)
		self.assertFalse(isBefore)	
		
	def testDadDeathOneMonthBefore(self):
		print()
		birth = date.today()
		death = birth - timedelta(days = 30)
		print("US09 - if death of father was 1 month before")
		isBefore = birthBeforeDadDeath(birth, death)
		print (birth, death, isBefore)
		self.assertTrue(isBefore)

#US03 - Birth before Death
class TestUserStoryThree(unittest.TestCase):
	def testBirthBeforeDeath(self):
		print()
		birth = datetime.strptime("2000-12-06", '%Y-%m-%d').date()
		death = datetime.strptime("2001-8-06", '%Y-%m-%d').date()
		print("US03 - Birth before Death")
		testResult = birthBeforeDeath(birth, death)
		print(birth, death, testResult)
		self.assertFalse(testResult)

#US06 - Divorce before death 
class TestUserStorySix(unittest.TestCase):
	def testDivorceBeforeDeath(self):
		print()
		divorce = datetime.strptime("2019-12-06", '%Y-%m-%d').date()
		death = datetime.strptime("2022-8-06", '%Y-%m-%d').date()
		print("US06 - Divorce before Death")
		testResult2 = divorceBeforeDeath(divorce, death)
		print(divorce, death, testResult2)
		self.assertFalse(testResult2)

#US35 - list recent birth 
class TestUserStoryThirtyFive(unittest.TestCase):
	def testListRecentBirth(self):
		print()
		td = date.today()
		birth = datetime.strptime("2023-02-23", '%Y-%m-%d').date()
		print("US35 - comparing birth if its within 30 days")
		testResult3 = listRecentBirth(td, birth)
		print(td, birth, testResult3)
		self.assertTrue(testResult3)

#US36 - list recent death
class TestUserStoryThirtySix(unittest.TestCase):
	def testListRecentBirth(self):
		print()
		td = date.today()
		death = datetime.strptime("2023-02-23", '%Y-%m-%d').date()
		print("US36 - comparing death if its within 30 days")
		testResult3 = listRecentDeath(td, death)
		print(td, death, testResult3)
		self.assertTrue(testResult3)

if __name__ == '__main__':
	# tihs logs stdout to a file instead of the command line
	with open('unit_testing.txt', 'w') as sys.stdout:
		testSuite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
		unittest.main(testRunner = unittest.TextTestRunner(sys.stdout)).run(testSuite)