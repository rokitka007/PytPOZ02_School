from kNowakowska.people.Person import SchoolPerson


class OfficeWorker(SchoolPerson):
    def __init__(self, name, surname, birthday):
        super().__init__(name, surname, birthday)
