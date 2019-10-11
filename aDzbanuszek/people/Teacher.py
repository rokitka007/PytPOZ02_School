from datetime import date
import os
from aDzbanuszek.people.Person import Person
from aDzbanuszek.people.Student import Student


class Teacher(Person):

    def __init__(self, name, second_name, born_data, vacationDay, engagement):
        super(Teacher, self).__init__(name, second_name, born_data)
        self.vacationDay = int(vacationDay)
        self.engagement = float(engagement)
        self.vacationDayMax = 26

    def takeVacation(self, delta):
        if self.vacationDay == 0:
            print('Teacher ' + self.getName() + self.getSecond_name() + ' do not have vacation day left')
            return self.vacationDay == 0
        if self.vacationDay < delta:
            print(
                'Teacher ' + self.getName() + self.getSecond_name() + ' do not have enough days')
            return self.vacationDay == self.vacationDay
        self.vacationDay = self.vacationDay - delta

    def checkVacationLeft(self):
        return self.vacationDay

    def transferKnowledge(self, key, Student):
        skill = Student.getSkillsValue()
        value_skill = skill[key]
        transfer_knowledge = value_skill*self.engagement

        return transfer_knowledge

