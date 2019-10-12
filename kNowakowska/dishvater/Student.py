from Skill import Skill
from kNowakowska.dishvater.Person import Person


class StudentException(Exception):
    pass


class Student(Person):

    def __init__(self, name, surname, birthDay, obedience=1, skills=None, exp='cos', hobby='cos', preferences=None):
        super().__init__(name, surname, birthDay, skills)
        self.cv = self.setCV([exp], [hobby])
        if not preferences:
            preferences = []
        self.preferences = preferences
        self.obedience = obedience

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

    def setPreferences(self, preferences):
        if not isinstance(preferences, list):
            raise StudentException("preferences has to be list!")
        for el in preferences:
            if not isinstance(el, Skill):
                raise StudentException("Element need to be skill")
        self.preferences = preferences

    def getPreferences(self):
        print("My preferences are: ")
        for el in self.preferences:
            print(f'{el.name}')

    def getKnoledge(self, skill, value):
        if skill not in self.skills.keys():
            self.skills.update({skill: 0})
        if self.skills.get(skill) == 1:
            print(f"You're already expert in {skill.name}")
        knowledge = round((value * self.obedience), 2)
        if skill in self.preferences:
            knowledge *= 2
        if self.skills.get(skill) + value >= 1:
            print(f"Congratulation. You gained expert level in {skill.name}. "
                  f"for further education go to collage with {skill.name} faculty")
            self.skills.update({skill: 1})
        else:
            self.skills.update({skill: self.skills.get(skill) + knowledge})
            self.presentSkills()

        # for k, v in self.preferences:
        #     self.obedience * v
