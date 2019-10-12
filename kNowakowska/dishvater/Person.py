from datetime import datetime
from Skill import Skill
from random import randrange, uniform


class PersonException(Exception):
    pass


class Person:

    def __init__(self, name, surname, dateOfBirth, skills=None):
        if skills is None:
            skills = {}
        self.name = name
        self.surname = surname
        self.dateOfBirth = datetime.strptime(dateOfBirth, "%d-%m-%Y")
        self.skills = skills

    def presentYourself(self):
        print("Hi, I'm {} {} and I'm {} years old".format(self.name, self.surname, self.getAge()))

    def getAge(self):
        now = datetime.now().year
        then = self.dateOfBirth.year
        return now - then

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def defineSkills(self, skills=None, automatic=True):
        if not skills and automatic is True:
            self.skills = {Skill.CHEMISTRY: round(uniform(0, 1), 2), Skill.ENGLISH: round(uniform(0, 1), 2),
                           Skill.BIOLOGY: round(uniform(0, 1), 2), Skill.HISTORY: round(uniform(0, 1), 2),
                           Skill.MATH: round(uniform(0, 1), 2)}
        elif not skills and automatic is False:
            raise PersonException("Give skills or try automatic skills creation")
        else:
            self.skills = skills

    def presentSkills(self):
        print("my skills: \n")
        for k, v in self.skills.items():
            print(f'{k.name} : {v}')

    def _getSkillValue(self, skill):
        return self.skills.get(skill)
