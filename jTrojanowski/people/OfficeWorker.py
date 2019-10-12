from jTrojanowski.people.Person import SchoolPerson


class OfficeWorker(SchoolPerson):
    def __init__(self, name, surname, birthday, skills=None):
        super().__init__(name, surname, birthday, skills)
