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

class TestUserStoryTwentyFive(unittest.TestCase):
	def test_family_names_success(self):
		print()
		actual = Family_names(names = ['Matt /Jones/', 'Soraia /Sales/','Stephanie /Sales-Jones/','Stephanie /Sales-Jones/'])
		expected = {'Stephanie'}
		print("US25 - Unique first names in families")
		print(actual,expected)
		self.assertEqual(actual, expected)
	
	def test_family_names_not_equal(self):
		print()
		actual = Family_names(names = ['Matt /Jones/', 'Soraia /Sales/','Stephanie /Sales-Jones/','Natalie /Sales-Jones/'])
		expected = {'Matt'}
		print("US25 - Unique first names in families")
		print(actual,expected)
		self.assertNotEqual(actual, expected)

	def test_family_names_is_not_equal(self):
		print()
		actual = Family_names(names = ['Sebastian /Fernandez/', 'Soraia /Sales/','Stephen /Fernandez/'])
		expected = {'Calvin /Williams/'}
		print("US25 - Unique first names in families")
		print(actual,expected)
		self.assertNotEqual(actual, expected)

	def test_family_names_empty_set(self):
		print()
		actual = Family_names(names = ['Sebastian /Fernandez/', 'Soraia /Sales/','Stephen /Fernandez/'])
		expected = set()
		print("US25 - Unique first names in families")
		print(actual,expected)
		self.assertEqual(actual, expected)

	def test_family_names_not_eq(self):
		print()
		actual = Family_names(names = [])
		expected = {'Calvin /Williams/', 'Ruby /Smith/', 'Nathan /Williams/'}
		print("US25 - Unique first names in families")
		print(actual,expected)
		self.assertNotEqual(actual, expected)





if __name__ == '__main__':
	# tihs logs stdout to a file instead of the command line
	with open('unit_testing.txt', 'w') as sys.stdout:
		testSuite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
		unittest.main(testRunner = unittest.TextTestRunner(sys.stdout)).run(testSuite)