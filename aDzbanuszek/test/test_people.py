import unittest
from datetime import date

from aDzbanuszek.people.Person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Jan', 'Kowalski', born_data=date(2000, 2, 2))

    def test_Person_name(self):
        self.assertEqual(self.person.name, self.person.getName())
        self.assertEqual(self.person.name, "Jan")

    def test_Person_second_name(self):
        self.assertEqual(self.person.getSecond_name(), self.person.second_name)
        self.assertEqual(self.person.second_name, "Kowalski")

    def test_Person_born_data(self):
        self.assertEqual(self.person.get_age(), 19)
