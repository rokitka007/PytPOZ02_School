from datetime import date
import os
from aDzbanuszek.people.Person import Person
from aDzbanuszek.people.Skill import Skill


class StudentExceptions(Exception):
    pass


class Student(Person):

    def __init__(self, name, second_name, born_data, skills, CV, obedience=1, preferences=None):
        super(Student, self).__init__(name, second_name, born_data, skills)
        self.CV = str(CV)
        self.obedience = float(obedience)
        if not preferences:
            preferences = []
        self.preferences = preferences

    def getCV(self):
        tekst = str(self.CV)
        return tekst

    '''zapisuje CV do plikuImieNazwisko_CV.txt'''

    def downloadCV(self):
        file_CV = open('{}{}.txt'.format(self.getName(), self.getSecond_name()), '+w')
        file_CV.write(self.getCV())
        file_CV.close()

    def presentCV(self):
        print(self.getCV())

    def setPreferences(self, preferences):
        if not isinstance(preferences, list):
            raise StudentExceptions('preferences has to be list!')
        for el in self.preferences:
            if not isinstance(el, Skill):
                raise StudentExceptions("Element need to be skill")

        self.preferences = preferences

    def getPreferences(self):
        print("My preferences are: ")
        for el in self.preferences:
            print("{}".format(el.name))

    def getObedience(self):
        return self.obedience

    # dodac: jesli mamy max z czegos uczsie czegos inneg?

    def getGeneralKnowledge(self):
        for key, value in self.skills.items():
            if value == 1.0:
                print("I'm sorry, you've already gained expert level {} faculty".format(key))
            if key not in self.preferences and value < 1.0:
                a = self.skills[key] + self.obedience
                if a >= 1.0:
                    self.skills[key] = 1.0
                    print('Congratulations! You gained maximum of {}'.format(key))
                else:
                    self.skills[key] = self.skills[key] +  self.obedience
            if key in self.preferences and value < 1.0:
                z = self.skills[key] + self.obedience * 2
                if z >= 1.0:
                    #self.skills[key] = 1.0
                    self.skills.update({key: 1.0})
                    print('Congratulations! You gained maximum of {}'.format(key))
                else:
                    self.skills[key] +=  self.obedience * 2

        return self.skills

    def getKnowledge(self, skill, value):
        if skill not in self.skills.keys():
            self.skills.update({skill: 0})
        if self.skills.get(skill) == 1:
            print("You're already expert in {}".format(skill.name))
            return self.skills
        knowledge = value * self.obnedience
        if skill in self.preferences:
            knowledge *= 2
        if self.skills.get(skill) + knowledge >= 1:
            print(
                "Congartulation. You gained expert level in {}. For further education go to collage with {} faculty".format(
                    skill.name, skill.name))
            self.skills.update({skill: 1})
        else:
            self.skills.update({skill: self.skills.get(skill) + knowledge})
            self.presentSkills()
