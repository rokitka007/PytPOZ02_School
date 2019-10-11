from kNowakowska.people.Person import Person

class Student(Person):
    def __init__(self, name, surname, dateOfBirth, obedience=1, skills = None, preferences=None):
        super().__init__(name, surname, dateOfBirth, skills)
        self.obedience = obedience
        self.setCV(["No experience"], ["No hobby"])
        if preferences is None:
            preferences = []
        self.preferences = preferences

    def setCV(self, exp, hobby):
        self.cv = "Curriculum Vitae\n"
        self.cv += "Name: {}\nSurname: {}\nAge: {}\n".format(self.name, self.surname, self.getAge())
        self.cv += "Doswiadczenie:\n"
        for el in exp:
            self.cv += el + "\n"
        self.cv += "Zainteresowania:\n"
        for el in hobby:
            self.cv += el + "\n"

    def presentCV(self):
        print(self.cv)

    def downloadCV(self):
        with open("{}_{}_CV.txt".format(self.name, self.surname), 'w') as f:
            f.writelines(self.cv)

    def getPreferences(self):
        if not self.preferences:
            print("I do not prefer any of subjects")
        else:
            print("I do prefer " + ', '.join(map(lambda x: x.name, self.preferences)))
        return self.preferences

    def getKnowledge(self, skill, value):
        skill_delta = value*self.obedience
        if skill in self.preferences:
            skill_delta *= 2
        skill_value = self._getSkillValue(skill)+skill_delta
        self._updateSkill(skill, skill_value)


class StudentException(Exception):
    pass