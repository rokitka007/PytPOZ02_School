from kNowakowska.dishvater.Person import Person


class TeacherException(Exception):
    pass


class Teacher(Person):

    def __init__(self, name, surname, dateOfBirth, engagement):
        super().__init__(name, surname, dateOfBirth)
        self.engagement = engagement
        self.vacationDays = 26

    def takeVacation(self, days):
        if days > self.vacationDays:
            raise TeacherException("You do not have so many days. You're left {}".format(self.vacationDays))
        else:
            self.vacationDays -= days

    def checkVacationLeft(self):
        print("I'm left () days of vacation".format(self.vacationDays))
