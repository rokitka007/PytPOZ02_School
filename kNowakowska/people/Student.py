from kNowakowska.people.Person import Person


class StudentException(Exception):
    pass


class Student(Person):

    def __init__(self, name, surname, birthDay, obedience = 1, skills=None, exp="cos", hobby="cos", preferences=None):
        super().__init__(name, surname, birthDay, skills)
        self.cv = self.setCV([exp], [hobby])
        if not preferences:
            preferences = []
        self.preferences = preferences
        self.obedience = obedience

    def setCV(self, exp, hobby):
        self.cv = "Curriculum Vitae"
        self.cv += "Name {}\nSurname{}\nAge{}\n".format(self.name, self.surname, self.getAge())
        self.cv += "Doswiadczenie:"


        for el in exp:
            self.cv += el + "\n"
        self.cv += "Zainteresowania:\n"
        for el in hobby:
            self.cv += el + "\n"

    def presentCV(self):
        print(self.cv)

    def setPreferences(self,preferences):
        if not isinstance(preferences, list):
            raise StudentException("Preferences has to be list!")
        self.preferences = preferences

    def getPreferences(self):
        print ("My preferences are: ")
        for el in self.preferences:
            print ("{}".format(el.name))

    def getKnowledge(self, skill, value):
        if skill not in self.skills.keys():
            self.skills.update({skill: 0})
        if self.skills.get(skill) == 1:
            print("You're already expert in {}".format(skill.name))
            return self.skills
        knowledge = value * self.obedience
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