from PytPOZ02_School.kNowakowska.people.Person import SchoolPerson


class Teacher(SchoolPerson):
    def __init__(self, name, surname, birthday, engagement, vacation_day=26):
        super().__init__(name, surname, birthday)
        self._engagement = float(engagement)
        self._vacation_day = int(vacation_day)

    def take_vacation(self, number_of_day):
        self._vacation_day -= int(number_of_day)
        if self._vacation_day < 0:
            raise ValueError(f'For {self._name} {self._surname} is not possible to take {number_of_day} days off')

    def check_vacation_left(self):
        return self._vacation_day