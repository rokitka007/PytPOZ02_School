from datetime import datetime

from kNowakowska.people.Skill import Skill


class PersonException(Exception):
    pass


class Person():

    def __init__(self, name, surname, dateOfBirth, skills=None):
        self.name = name
        self.surname = surname
        self.dateOfBirth = datetime.strptime(dateOfBirth, "%d-%m-%Y")
        if skills is None:
            skills = {}
        self.defineSkills(skills)

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
        if automatic is True and not skills:
            self.skills = dict({ Skill.BIOLOGY: 0, Skill.HISTORY: 0, Skill.CHEMISTRY: 0, Skill.ENGLISH: 0, Skill.MATH: 0 })
        elif skills is None and automatic is False:
            raise PersonException("Define skills or choose automatic creation of skills")
        else:
            self.skills = skills

    def presentSkills(self):
        print("My skills are:")
        for k, v in self.skills.items():
            print("{}: {}".format(k.name, v))

    def _getSkillValue(self, skill):
        if skill not in self.skills.keys():
            return 0
        return self.skills.get(skill)

    def _updateSkill(self, skill, value):
        self.skills.update({skill: value})