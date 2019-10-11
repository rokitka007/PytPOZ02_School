from datetime import date
from aDzbanuszek.people.Person import Person
from aDzbanuszek.people.Student import Student
from aDzbanuszek.people.Teacher import Teacher

if __name__ == '__main__':
    print("Welcome in my School")

    person_1 = Person('Jacek', 'DD')
    person_2 = Person('Dominika', 'Kot', date(1997, 10, 20))
    print(person_1.name + ' ' + str(person_1.born_data))
    print(person_1.get_age())
    person_1.present_yourself()
    print(person_2.name + ' ' + str(person_2.born_data))
    print(person_2.get_age())
    print('\n')
    student_1 = Student('Ryszard', 'Zorro', date(1998, 5, 20), 'pierwszy', 0.2, skills={'Biology': 1.0, 'Chemistry': 0.2, 'Math': 0.80, 'English':0.2, 'History' : 0.0})
    student_1.downloadCV()
    student_1.presentCV()
    print('\n')
    teacher_1 = Teacher('Franciszek', 'Lubawy', date(1980, 5, 15), 26, 0.7)
    print(teacher_1.name + ' ' + str(teacher_1.born_data))
    teacher_1.takeVacation(10)
    print('(-10) {}'.format(teacher_1.checkVacationLeft()))
    teacher_1.takeVacation(10)
    print('(-10) {}'.format(teacher_1.checkVacationLeft()))
    teacher_1.takeVacation(10)
    print('(-10) {}'.format(teacher_1.checkVacationLeft()))
    teacher_1.takeVacation(6)
    print('(-6) {}'.format(teacher_1.checkVacationLeft()))
    teacher_1.takeVacation(4)
    print('(-4) {}'.format(teacher_1.checkVacationLeft()))
    print(teacher_1.checkVacationLeft())

    print(teacher_1.checkVacationLeft())
#    print(person_1.getSkillsValue())
    print(student_1.obedience)
    print(student_1.getSkillsValue())
    print(student_1.getKnowledge(1))
    print(teacher_1.transferKnowledge('Math', student_1))
    print(student_1.defineSkills())
