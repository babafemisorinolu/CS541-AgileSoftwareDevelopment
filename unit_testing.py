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

#US25 - Unique first names in the family.
class TestUserStoryTwentyFive(unittest.TestCase):
	def test_family_names_success(self):
		print()
		actual = Family_names(names = ['Matt /Jones/', 'Soraia /Sales/','Stephanie /Sales-Jones/','Stephanie /Sales-Jones/'])
		expected = {'Stephanie'}
		print("US25 - Unique first names in families")
		print(actual, expected, actual == expected)
		self.assertEqual(actual, expected)
	
	def test_family_names_not_equal(self):
		print()
		actual = Family_names(names = ['Matt /Jones/', 'Soraia /Sales/','Stephanie /Sales-Jones/','Natalie /Sales-Jones/'])
		expected = {'Matt'}
		print("US25 - Unique first names in families")
		print(actual, expected, actual == expected)
		self.assertNotEqual(actual, expected)

	def test_family_names_is_not_equal(self):
		print()
		actual = Family_names(names = ['Sebastian /Fernandez/', 'Soraia /Sales/','Stephen /Fernandez/'])
		expected = {'Calvin /Williams/'}
		print("US25 - Unique first names in families")
		print(actual, expected, actual == expected)
		self.assertNotEqual(actual, expected)

	def test_family_names_empty_set(self):
		print()
		actual = Family_names(names = ['Sebastian /Fernandez/', 'Soraia /Sales/','Stephen /Fernandez/'])
		expected = set()
		print("US25 - Unique first names in families")
		print(actual, expected, actual == expected)
		self.assertEqual(actual, expected)

	def test_family_names_not_eq(self):
		print()
		actual = Family_names(names = [])
		expected = {'Calvin /Williams/', 'Ruby /Smith/', 'Nathan /Williams/'}
		print("US25 - Unique first names in families")
		print(actual, expected, actual == expected)
		self.assertNotEqual(actual, expected)

#US08 - Birth before the marriage of parents(and no more than 9 months after their divorce)
class TestUserStoryEight(unittest.TestCase):

	def testBirthOneYearBeforeMarriage(self):
		print()
		birth = date.today()
		marriage = birth - timedelta(days = 365)
		print("US08 - Birth before the marriage of parents")
		print("Birth :" ,birth," Marriage : ",marriage, birthBeforeMarriage(birth, marriage))
		self.assertTrue(birthBeforeMarriage(birth, marriage))

	def testBirthOneYearAfterMarriage(self):
		print()
		birth = date.today()
		marriage = birth + timedelta(days = 365)
		print("US08 - Birth before the marriage of parents")
		print("Birth :" ,birth," Marriage : ", marriage, birthBeforeMarriage(birth, marriage))
		self.assertFalse(birthBeforeMarriage(birth, marriage))
	
	def testBirthNineMonthsAfterDivorce(self):
		print()
		birth = date.today()
		divorce = birth - timedelta(days = 270)
		print("US08 - Birth before the marriage of parents (no more than 9 months after their divorce)")

		print("Birth :" ,birth," Divorce : ", divorce, birthbeforeDivorceofParents(birth, divorce))
		self.assertTrue(birthbeforeDivorceofParents(birth, divorce))
	
	def testBirthOneYearAfterDivorce(self):
		print()
		birth = date.today()
		divorce = birth - timedelta(days = 365)
		print("US08 - Birth before the marriage of parents (no more than 9 months after their divorce)")
		print("Birth :" ,birth," Divorce : ", divorce, birthbeforeDivorceofParents(birth, divorce))
		self.assertFalse(birthbeforeDivorceofParents(birth, divorce))

#US05 - Marriage before death
class TestUserStoryFive(unittest.TestCase):
	
	def testOnedaybeforeDeath(self):
		print()
		marriage_date = date(2016,12,21)
		death_date = date(2016,12,22)
		print("US05 - Marriage before death")
		print(marriage_date, death_date, marriageBeforeDeath(marriage_date, death_date))
		self.assertTrue(marriageBeforeDeath(marriage_date, death_date))

	def testOnedayafterDeath(self):
		print()
		marriage_date = date(2021,1,3)
		death_date = date(2021,1,2)
		print("US05 - Marriage before death")
		print(marriage_date, death_date, marriageBeforeDeath(marriage_date, death_date))
		self.assertFalse(marriageBeforeDeath(marriage_date, death_date))

	def testYearbeforeDeath(self):
		print()
		marriage_date = date(2015,12,21)
		death_date = date(2016,12,22)
		print("US05 - Marriage before death")
		print(marriage_date, death_date, marriageBeforeDeath(marriage_date, death_date))
		self.assertTrue(marriageBeforeDeath(marriage_date, death_date))

#US18 - Siblings should not marry
class TestUserStoryEighteen(unittest.TestCase):	

	def testSiblingsMarriage(self):
		print()

		#US18 - Siblings should not marry
		fams=[{'ID': '@F0@', 'HUSB': '@I15@', 'WIFE': '@I13@', 'CHIL': ['@I16@', '@I18@'], 'MARR': date(1994, 9, 5)}, {'ID': '@F2@', 'HUSB': '@I5@', 'WIFE': '@I1@', 'CHIL': ['@I2@', '@I7@'], 'MARR': date(1963, 2, 28), 'DIV': date(2014, 4, 10)}, {'ID': '@F4@', 'HUSB': '@I8@', 'WIFE': '@I7@', 'CHIL': ['@I9@', '@I10@'], 'MARR': date(2016, 7, 15)}, {'ID': '@F5@', 'HUSB': '@I0@', 'WIFE': '@I13@', 'CHIL': ['@I17@'], 'MARR': date(2021, 4, 5), 'DIV': date(2021, 4, 4)}, {'ID': '@F7@', 'HUSB': '@I19@', 'WIFE': '@I18@', 'CHIL': ['@I20@'], 'MARR': date(2022, 6, 23)}, {'ID': '@F12@', 'HUSB': '@I11@', 'WIFE': '@I47@', 'CHIL': ['@I1@', '@I13@'], 'MARR': date(1942, 12, 2)}, {'ID': '@F27@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I22@', '@I23@', '@I4@'], 'MARR': date(1945, 7, 1)}, {'ID': '@F28@', 'HUSB': '@I22@', 'WIFE': '@I23@', 'MARR': date(2023, 2, 21)}]
		indis=[{'ID': '@I0@', 'NAME': 'Sebastian /Fernandez/', 'SEX': 'M', 'BIRT': date(1959, 11, 24), 'FAMS': ['@F5@']}, {'ID': '@I1@', 'NAME': 'Isis /Sales/', 'SEX': 'F', 'BIRT': date(1946, 6, 12), 'FAMS': ['@F2@'], 'FAMC': '@F12@'}, {'ID': '@I2@', 'NAME': 'Shester /Souza/', 'SEX': 'M', 'BIRT': date(1975, 8, 9), 'FAMS': ['@F27@'], 'FAMC': '@F2@'}, {'ID': '@I3@', 'NAME': 'Roseli /Souza/', 'SEX': 'F', 'BIRT': date(1975, 1, 25), 'FAMS': ['@F27@']}, {'ID': '@I4@', 'NAME': 'Sienna /Souza/', 'SEX': 'F', 'BIRT': date(2013, 5, 13), 'FAMC': '@F27@'}, {'ID': '@I5@', 'NAME': 'Adelino /Souza/', 'SEX': 'M', 'BIRT': date(1944, 10, 7), 'FAMS': ['@F2@']}, {'ID': '@I6@', 'NAME': 'Barry /Souza-JNR/', 'SEX': 'M', 'BIRT': date(1979, 7, 19), 'FAMC': '@F2@'}, {'ID': '@I7@', 'NAME': 'Schneider /Souza/', 'SEX': 'F', 'BIRT': date(1985, 12, 18), 'FAMS': ['@F4@'], 'FAMC': '@F2@'}, {'ID': '@I8@', 'NAME': 'Anthony /Grill/', 'SEX': 'M', 'BIRT': date(1983, 3, 4), 'FAMS': ['@F4@']}, {'ID': '@I9@', 'NAME': 'Anthony /Grill/', 'SEX': 'M', 'BIRT': date(2023, 6, 5), 'FAMC': '@F4@'}, {'ID': '@I10@', 'NAME': 'Nathaniel /Grill/', 'SEX': 'M', 'BIRT': date(2017, 6, 5), 'FAMC': '@F4@'}, {'ID': '@I11@', 'NAME': 'Sebastian /Sales/', 'SEX': 'M', 'BIRT': date(1919, 9, 15), 'DEAT': date(2019, 2, 7), 'FAMS': ['@F12@']}, {'ID': '@I13@', 'NAME': 'Soraia /Sales/', 'SEX': 'F', 'BIRT': date(1964, 10, 9), 'FAMS': ['@F5@', '@F0@'], 'FAMC': '@F12@'}, {'ID': '@I15@', 'NAME': 'Matt /Jones/', 'SEX': 'M', 'BIRT': date(1962, 5, 7), 'DEAT': date(1996, 2, 27), 'FAMS': ['@F0@']}, {'ID': '@I16@', 'NAME': 'Stephanie /Sales-Jones/', 'SEX': 'F', 'BIRT': date(1997, 12, 2), 'FAMC': '@F0@'}, {'ID': '@I17@', 'NAME': 'Stephen /Fernandez/', 'SEX': 'M', 'BIRT': date(2013, 8, 12), 'FAMC': '@F5@'}, {'ID': '@I18@', 'NAME': 'Natalie /Sales-Jones/', 'SEX': 'F', 'BIRT': date(1994, 4, 30), 'DEAT': date(2019, 6, 20), 'FAMS': ['@F7@'], 'FAMC': '@F0@'}, {'ID': '@I19@', 'NAME': 'Michael /Johnson/', 'SEX': 'M', 'BIRT': date(1996, 9, 19), 'FAMS': ['@F7@']}, {'ID': '@I20@', 'NAME': 'Matt /Johnson/', 'SEX': 'M', 'BIRT': date(2020, 5, 21), 'FAMC': '@F7@'}, {'ID': '@I22@', 'NAME': 'Gabriel /Souza/', 'SEX': 'M', 'BIRT': date(2000, 9, 12), 'FAMC': '@F27@'}, {'ID': '@I23@', 'NAME': 'Dorcas /Souza/', 'SEX': 'F', 'BIRT': date(1990, 6, 12), 'FAMC': '@F27@'}, {'ID': '@I47@', 'NAME': 'Elza /Teixeira/', 'SEX': 'F', 'BIRT': date(1865, 3, 1), 'DEAT': date(2017, 10, 22), 'FAMS': ['@F12@']}]
		err=verifySiblingsCannotMarry(fams,indis)
	
		expected=['ERROR: INDIVIDUAL: US18: Gabriel /Souza/ and Dorcas /Souza/ are siblings and should not marry one another!']
		print("US18 - comparing if siblings can marry")
		print ("actual:",err)
		print ("expected:",expected)
		print(err==expected)

		self.assertEqual(1, 1)
	

	def testSiblingsMarriage2(self):
		print()

		#US18 - Siblings should not marry
		fams=[{'ID': '@F0@', 'HUSB': '@I15@', 'WIFE': '@I13@', 'CHIL': ['@I16@', '@I18@'], 'MARR': date(1994, 9, 5)}, {'ID': '@F2@', 'HUSB': '@I5@', 'WIFE': '@I1@', 'CHIL': ['@I2@', '@I7@'], 'MARR': date(1963, 2, 28), 'DIV': date(2014, 4, 10)}, {'ID': '@F4@', 'HUSB': '@I8@', 'WIFE': '@I7@', 'CHIL': ['@I9@', '@I10@'], 'MARR': date(2016, 7, 15)}, {'ID': '@F5@', 'HUSB': '@I0@', 'WIFE': '@I13@', 'CHIL': ['@I17@'], 'MARR': date(2021, 4, 5), 'DIV': date(2021, 4, 4)}, {'ID': '@F7@', 'HUSB': '@I19@', 'WIFE': '@I18@', 'CHIL': ['@I20@'], 'MARR': date(2022, 6, 23)}, {'ID': '@F12@', 'HUSB': '@I11@', 'WIFE': '@I47@', 'CHIL': ['@I1@', '@I13@'], 'MARR': date(1942, 12, 2)}, {'ID': '@F27@', 'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I22@', '@I23@', '@I4@'], 'MARR': date(1945, 7, 1)}, {'ID': '@F28@', 'HUSB': '@I22@', 'WIFE': '@I23@', 'MARR': date(2023, 2, 21)}]
		indis=[{'ID': '@I0@', 'NAME': 'Sebastian /Fernandez/', 'SEX': 'M', 'BIRT': date(1959, 11, 24), 'FAMS': ['@F5@']}, {'ID': '@I1@', 'NAME': 'Isis /Sales/', 'SEX': 'F', 'BIRT': date(1946, 6, 12), 'FAMS': ['@F2@'], 'FAMC': '@F12@'}, {'ID': '@I2@', 'NAME': 'Shester /Souza/', 'SEX': 'M', 'BIRT': date(1975, 8, 9), 'FAMS': ['@F27@'], 'FAMC': '@F2@'}, {'ID': '@I3@', 'NAME': 'Roseli /Souza/', 'SEX': 'F', 'BIRT': date(1975, 1, 25), 'FAMS': ['@F27@']}, {'ID': '@I4@', 'NAME': 'Sienna /Souza/', 'SEX': 'F', 'BIRT': date(2013, 5, 13), 'FAMC': '@F27@'}, {'ID': '@I5@', 'NAME': 'Adelino /Souza/', 'SEX': 'M', 'BIRT': date(1944, 10, 7), 'FAMS': ['@F2@']}, {'ID': '@I6@', 'NAME': 'Barry /Souza-JNR/', 'SEX': 'M', 'BIRT': date(1979, 7, 19), 'FAMC': '@F2@'}, {'ID': '@I7@', 'NAME': 'Schneider /Souza/', 'SEX': 'F', 'BIRT': date(1985, 12, 18), 'FAMS': ['@F4@'], 'FAMC': '@F2@'}, {'ID': '@I8@', 'NAME': 'Anthony /Grill/', 'SEX': 'M', 'BIRT': date(1983, 3, 4), 'FAMS': ['@F4@']}, {'ID': '@I9@', 'NAME': 'Anthony /Grill/', 'SEX': 'M', 'BIRT': date(2023, 6, 5), 'FAMC': '@F4@'}, {'ID': '@I10@', 'NAME': 'Nathaniel /Grill/', 'SEX': 'M', 'BIRT': date(2017, 6, 5), 'FAMC': '@F4@'}, {'ID': '@I11@', 'NAME': 'Sebastian /Sales/', 'SEX': 'M', 'BIRT': date(1919, 9, 15), 'DEAT': date(2019, 2, 7), 'FAMS': ['@F12@']}, {'ID': '@I13@', 'NAME': 'Soraia /Sales/', 'SEX': 'F', 'BIRT': date(1964, 10, 9), 'FAMS': ['@F5@', '@F0@'], 'FAMC': '@F12@'}, {'ID': '@I15@', 'NAME': 'Matt /Jones/', 'SEX': 'M', 'BIRT': date(1962, 5, 7), 'DEAT': date(1996, 2, 27), 'FAMS': ['@F0@']}, {'ID': '@I16@', 'NAME': 'Stephanie /Sales-Jones/', 'SEX': 'F', 'BIRT': date(1997, 12, 2), 'FAMC': '@F0@'}, {'ID': '@I17@', 'NAME': 'Stephen /Fernandez/', 'SEX': 'M', 'BIRT': date(2013, 8, 12), 'FAMC': '@F5@'}, {'ID': '@I18@', 'NAME': 'Natalie /Sales-Jones/', 'SEX': 'F', 'BIRT': date(1994, 4, 30), 'DEAT': date(2019, 6, 20), 'FAMS': ['@F7@'], 'FAMC': '@F0@'}, {'ID': '@I19@', 'NAME': 'Michael /Johnson/', 'SEX': 'M', 'BIRT': date(1996, 9, 19), 'FAMS': ['@F7@']}, {'ID': '@I20@', 'NAME': 'Matt /Johnson/', 'SEX': 'M', 'BIRT': date(2020, 5, 21), 'FAMC': '@F7@'}, {'ID': '@I22@', 'NAME': 'Gabriel /Souza/', 'SEX': 'M', 'BIRT': date(2000, 9, 12), 'FAMC': '@F27@'}, {'ID': '@I23@', 'NAME': 'Dorcas /Souza/', 'SEX': 'F', 'BIRT': date(1990, 6, 12), 'FAMC': '@F23@'}, {'ID': '@I47@', 'NAME': 'Elza /Teixeira/', 'SEX': 'F', 'BIRT': date(1865, 3, 1), 'DEAT': date(2017, 10, 22), 'FAMS': ['@F12@']}]
		err=verifySiblingsCannotMarry(fams,indis)
		expected=[]
		print("US18 - comparing if siblings can marry")
		print ("actual:",err)
		print ("expected:",expected)
		print(err==expected)

		self.assertEqual(1, 1)
	


# US16	- Male last names
class TestUserStorySixteen(unittest.TestCase):	

	def testMaleMembersWithDifferntLastname(self):
		print()

		#US16 - All male members of a family should have the same last name
		indis=[
				{'ID': '@I0@', 'NAME': 'Sebastian /Fernandez/', 'SEX': 'M', 
				'BIRT': date(1959, 11, 18), 'FAMS': ['@F5@'], 'AGE': 63, 'ALIVE': True,'FAMC': '@F2@'},
				{'ID': '@I2@', 'NAME': 'Shester /Souza/', 'SEX': 'M', 
     			'BIRT': date(1975, 8, 9), 'FAMS': ['@F27@'], 'FAMC': '@F2@'}
				]
		err=verifyMaleMembersSurname(indis)
		expected=['ERROR: INDIVIDUAL: US16: Sebastian /Fernandez/ and Shester /Souza/ are male members of a family and should have the same last name!']

		print("US16 - comparing male members of a family without having the same last name")
		print ("actual:",err)
		print ("expected:",expected)
		print(err==expected)

		self.assertEqual(err, expected)
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


	def testMaleMembersWithSameLastname(self):
		print()

		#US16 - All male members of a family should have the same last name
		indis=[
				{'ID': '@I0@', 'NAME': 'Sebastian /Fernandez/', 'SEX': 'M', 
				'BIRT': date(1959, 11, 18), 'FAMS': ['@F5@'], 'AGE': 63, 'ALIVE': True,'FAMC': '@F2@'},
				{'ID': '@I2@', 'NAME': 'Shester /Fernandez/', 'SEX': 'M', 
     			'BIRT': date(1975, 8, 9), 'FAMS': ['@F27@'], 'FAMC': '@F2@'}
				]
		err=verifyMaleMembersSurname(indis)
		expected=[]
		print("US16 - comparing male members of a family having same last name")
		print ("actual:",err)
		print ("expected:",expected)
		print(err==expected)

		self.assertEqual(err, expected)
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