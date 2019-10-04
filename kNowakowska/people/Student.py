from kNowakowska.people.Person import SchoolPerson


class Student(SchoolPerson):
    def __init__(self, name, surname, birthday, obedience, cv):
        super().__init__(name, surname, birthday)
        self._obedience = float(obedience)
        self._cv = str(cv)

    def download_cv(self):
        curriculum_vitae = open(f'{self._name}{self._surname}_CV.txt', "w")
        curriculum_vitae.write(self._cv)
        curriculum_vitae.close()

    def present_cv(self):
        show_cv = open(f'{self._name}{self._surname}_CV.txt').read()
        return show_cv