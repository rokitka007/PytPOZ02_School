import unittest

from kNowakowska.dishvater.Person import Person


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.person = Person(name='Wojciech', surname='Wawrzyniak', dateOfBirth='23-04-1986')

    def test_name(self):
        self.assertEqual(self.person.getName(), 'Wojciech')
        self.assertEqual(self.person.getName(), self.person.name)

    def test_surname(self):
        self.assertEqual(self.person.getSurname(), 'Wawrzyniak')
        self.assertEqual(self.person.getSurname(), self.person.surname)

    def test_getAge(self):
        self.assertEqual(self.person.getAge(), 33)


if __name__ == '__main__':
    unittest.main()
