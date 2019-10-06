from datetime import date
import os
from aDzbanuszek.people.Person import Person


class Student(Person):

    def __init__(self, name, second_name, born_data, CV, obedience):
        super(Student, self).__init__(name, second_name, born_data)
        self.CV = str(CV)
        self.obedience = float(obedience)

    def getCV(self):
        tekst = str(self.CV)
        return tekst


    '''zapisuje CV do plikuImieNazwisko_CV.txt'''

    def downloadCV(self):
        file_CV = open('{}{}.txt'.format(Student.getName(self), Student.getSecond_name(self)), '+w')
        file_CV.write(self.getCV())
        file_CV.close()

    def presentCV(self):
        print(Student.getCV(self))
