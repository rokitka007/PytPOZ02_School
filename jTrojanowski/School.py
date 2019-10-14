from jTrojanowski.people.Student import Student
from jTrojanowski.people.Teacher import Teacher
from jTrojanowski.people.OfficeWorker import OfficeWorker
from jTrojanowski.people.Skill import Skills

if __name__ == '__main__':
    person_one = OfficeWorker("Ken", "Follet", "05.06.1949", {Skills.ENGLISH: 0.5})
    person_two = Student("Jacek", "Trojanowski", "26.07.1985", 0.8, "Krótki życiorys dotyczący danej osoby")
    person_three = Teacher("Stephen", "King", "21.09.1947", 9.9, )

    person_two.define_skills()
    # person_two.present_skills()
    person_two.set_preferences([Skills.HISTORY])
    person_two.get_knowledge("HISTORY", 0.7)
    # print(person_two.get_preferences())

    # print(person_one.present_yourself())
    # print(person_one.get_age())
    # person_two.download_cv()
    # print(person_two.present_cv())
    # person_three.take_vacation(25)
    # print(person_three.check_vacation_left())
