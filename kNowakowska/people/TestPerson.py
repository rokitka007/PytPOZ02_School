import unittest
#from kNowakowska.people.Person import Person
from Person import Person

class TestPerson(unittest.TestCase):
    def test_age(self):
        self.AsseertEqual(self.Person.getAge(), self.Person.dateOfBirth)



