from datetime import date
import random

from aDzbanuszek.people.Skill import Skill


class PersonException(Exception):
    pass


class Person:

    def __init__(self, name, second_name, born_data=date(1982, 5, 20), skills=None):
        self.name = str(name)
        self.second_name = str(second_name)
        self.born_data = born_data
        if skills is None:
            skills = {}
        self.skills = skills

    def get_age(self):
        age = date.today()
        age = age.year - self.born_data.year
        return age

    def present_yourself(self):
        print('Hello! \nMy name is ' + self.name + ' ')

    def getName(self):
        return self.name

    def getSecond_name(self):
        return self.second_name

    def defineSkills(self, skills=None, automatic=True):
        if not skills and automatic is True:
            self.skills = {Skill.CHEMISTRY: round(random.uniform(0, 1), 1),
                           Skill.BIOLOGY: round(random.uniform(0, 1), 1),
                           Skill.MATH: round(random.uniform(0, 1), 1),
                           Skill.ENGLISH: round(random.uniform(0, 1), 1),
                           Skill.HISTORY: round(random.uniform(0, 1), 1)}
        elif not skills and automatic is False:
            raise PersonException("Give skills or try automatic skills creation")
        else:
            self.skills = skills

    def presentSkills(self):
        print("My skills: \n")
        for k, v in self.skills.items():
            print("{}: {}".format(k.name, v))

    def _getSkillValue(self, skill):
        return self.skills.get(skill)
