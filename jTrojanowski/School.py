from kNowakowska.people.Student import Student
from kNowakowska.people.Teacher import Teacher
from kNowakowska.people.OfficeWorker import OfficeWorker

if __name__ == '__main__':

    person_one = OfficeWorker("Ken", "Follet", "05.06.1949")
    person_two = Student("Jacek", "Trojanowski", "26.07.1985", 6.6, "Krótki życiorys dotyczący danej osoby")
    person_three = Teacher("Stephen", "King", "21.09.1947", 9.9)

    print(person_one.present_yourself())
    print(person_one.get_age())
    person_two.download_cv()
    print(person_two.present_cv())
    person_three.take_vacation(25)
    print(person_three.check_vacation_left())
