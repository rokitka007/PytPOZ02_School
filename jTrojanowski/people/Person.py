from datetime import date


class SchoolPerson:

    def __init__(self, name, surname, birthday):
        self._birthday = birthday.split(".")
        self._name = name
        self._surname = surname
        self._birthday_day = int(self._birthday[0])
        self._birthday_month = int(self._birthday[1])
        self._birthday_year = int(self._birthday[2])

    def get_age(self):
        today = date.today()
        person_age = today.year - self._birthday_year
        if today.month < self._birthday_month or today.month == self._birthday_month and today.day < self._birthday_day:
            person_age -= 1
        return person_age

    def present_yourself(self):
        return f'Name: {self._name} , Surname: {self._surname} , Age: {self.get_age()}'