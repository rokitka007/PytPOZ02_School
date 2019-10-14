from jTrojanowski.people.Person import SchoolPerson
from jTrojanowski.people.Skill import Skills


class StudentException(Exception):
    pass


class Student(SchoolPerson):
    def __init__(self, name, surname, birthday, obedience, cv, skills=None, preferences=None):
        super().__init__(name, surname, birthday, skills)
        self._obedience = float(obedience)
        self._cv = str(cv)
        if not preferences:
            self._preferences = []
        self._preferences = preferences

    def download_cv(self):
        curriculum_vitae = open(f'{self._name}{self._surname}_CV.txt', "w")
        curriculum_vitae.write(self._cv)
        curriculum_vitae.close()

    def present_cv(self):
        show_cv = open(f'{self._name}{self._surname}_CV.txt').read()
        return show_cv

    def set_preferences(self, preferences):
        if not isinstance(preferences, list):
            raise StudentException('preferences has to be list')
        for el in preferences:
            if not isinstance(el, Skills):
                raise StudentException("Element need to be a skill")
        self._preferences = preferences

    def get_preferences(self):
        print("My preferences are: ")
        for el in self._preferences:
            print(f'{el.name}')

    def get_knowledge(self, skill, value):
        if skill not in self._skills.keys():
            self._skills.update({skill: 0})
        if self._skills.get(skill) == 1:
            print("You're already expert in {}".format(skill.name))
        knowledge = value * self._obedience
        if skill in self._preferences:
            knowledge *= 2
        if self._skills.get(skill) + knowledge >= 1:
            print(
                "Congartulation. You gained expert level in {}. For further education go to collage with {} faculty".format(
                    skill.name, skill.name))
            self._skills.update({skill: 1})
        else:
            self._skills.update({skill: self._skills.get(skill) + knowledge})
            self.present_skills()

