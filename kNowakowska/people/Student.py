import os

from kNowakowska.people.Person import Person
from kNowakowska.people.Skill import Skill


class StudentException(Exception):
    pass


class Student(Person):

    def __init__(self, name, surname, birthDay, obedience, skills=None, exp="cos", hobby="cos", preferences=None):
        super().__init__(name, surname, birthDay, skills)
        self.cv = self.setCV([exp], [hobby])
        if not preferences:
            preferences = []
        self.preferences = preferences
        self.obnedience=obedience

    def setCV(self, exp, hobby):
        self.cv = "Curriculum Vitae"
        self.cv += "Name {}\nSurname{}\nAge{}\n".format(self.name, self.surname, self.getAge())
        self.cv += "Doswiadczenie:\n"
        for el in exp:
            self.cv += el + "\n"
        self.cv += "Zainteresowania:\n"
        for el in hobby:
            self.cv += el + "\n"
        return self.cv

    def presentCV(self):
        print(self.cv)

    def downloadCV(self):
        with open("{}_{}_CV.txt".format(self.getName(), self.getSurname()), 'w') as f:
            f.writelines(self.getName())

    def setPreferences(self, preferences):
        if not isinstance(preferences, list):
            raise StudentException("preferences has to be list of Skills!")
        for el in preferences:
            if not isinstance(el, Skill):
                raise StudentException("Element needs to be skill")
        self.preferences = preferences

    def getPreferences(self):
        print("My preferences are:")
        for el in self.preferences:
            print("{}".format(el.name))

    def getKnowledge(self, skill, value):
        if skill not in self.skills.keys():
            self.skills.update({skill: 0})
         #   self.skills[skill] = 0
        if self.skills.get(skill) == 1:
            print("You're already expert in {}".format(skill.name))
            return self.skills
        knowledge = value*self.obnedience
        if skill in self.preferences:
            knowledge *= 2
        if self.skills.get(skill) + knowledge >= 1:
            print("Congartulation. You gained expert level in {}. For further education go to collage with {} faculty".format(
                  skill.name, skill.name))
            self.skills.update({skill:1})
        else:
            self.skills.update({skill: self.skills.get(skill)+knowledge})
            self.presentSkills()
        return self.skills.get(skill)

    def getGeneralKnowledge(self, skills, value):
        updated_skills = []
        for el in skills:
            learned = self.getKnowledge(el, value)
            updated_skills.append(learned)
        return updated_skills

    def checkSkillLack(self, skill):
        skill_value = self._getSkillValue(skill)
        lack_of_skill = 1-skill_value
        print("You will be expert in {} if you gain {}".format(skill.name, skill_value))
        return lack_of_skill

