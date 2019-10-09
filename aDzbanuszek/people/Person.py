from datetime import date


class Person:

    def __init__(self, name, second_name, born_data=date(1982, 5, 20), skills={'Biology': 0.8, 'Chemistry': 0.8, 'Math': 0.8, 'English':0.8, 'History' : 0.8}):
        self.name = str(name)
        self.second_name = str(second_name)
        self.born_data = born_data
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

    def getSkillsValue(self):
        return self.skills
