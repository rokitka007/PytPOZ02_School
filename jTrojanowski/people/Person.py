from random import uniform
from datetime import date
from jTrojanowski.people.Skill import Skills


class PersonExeption(Exception):
    pass


class SchoolPerson:

    def __init__(self, name, surname, birthday, skills=None):
        self._birthday = birthday.split(".")
        self._name = name
        self._surname = surname
        self._birthday_day = int(self._birthday[0])
        self._birthday_month = int(self._birthday[1])
        self._birthday_year = int(self._birthday[2])
        if skills is None:
            skills = {}
        self._skills = skills

    def get_age(self):
        today = date.today()
        person_age = today.year - self._birthday_year
        if today.month < self._birthday_month or today.month == self._birthday_month and today.day < self._birthday_day:
            person_age -= 1
        return person_age

    def present_yourself(self):
        return f'Name: {self._name} , Surname: {self._surname} , Age: {self.get_age()}'

    def define_skills(self, skills=None, automatic=True):
        if not skills and automatic is True:
            self._skills = {Skills.CHEMISTRY: round(uniform(0, 1), 2), Skills.BIOLOGY: round(uniform(0, 1), 2),
                            Skills.MATH: round(uniform(0, 1), 2),
                            Skills.HISTORY: round(uniform(0, 1), 2), Skills.ENGLISH: round(uniform(0, 1), 2)}
        elif not skills and automatic is False:
            raise PersonExeption("Give skills or try automatic skills creation")
        else:
            self._skills = skills

    def present_skills(self):
        for k, v in self._skills.items():
            print(f"{k} {v}")

    def _getSkillValue(self, skill):
        return self._skills.get(skill)
