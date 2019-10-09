from datetime import date
import os
from aDzbanuszek.people.Person import Person


class Student(Person):

    def __init__(self, name, second_name, born_data, CV, obedience, skills, preferences=('Biology', 'Chemistry')):
        super(Student, self).__init__(name, second_name, born_data, skills)
        self.CV = str(CV)
        self.obedience = float(obedience)
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

    def getPreferences(self):
        return self.preferences

    def getKnowledge(self, val):
        for key, value in self.skills.items():
            if value == 1.0:
                print("I'm sorry, you've already gained expert level {} faculty".format(key))
            if key not in self.preferences and value < 1.0:
                a = self.skills[key] + val * self.obedience
                if a >= 1.0:
                    self.skills[key] = 1.0
                    print('Congratulations! You gained maximum of {}'.format(key))
                else:
                    self.skills[key] = self.skills[key] + val * self.obedience
            if key in self.preferences and value < 1.0:
                z = self.skills[key] + val * self.obedience * 2
                if z >= 1.0:
                    self.skills[key] = 1.0
                    print('Congratulations! You gained maximum of {}'.format(key))
                else:
                    self.skills[key] += val * self.obedience * 2

        return self.skills
