from datetime import date
from aDzbanuszek.people.Person import Person
from aDzbanuszek.people.Skill import Skill
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
    student_1 = Student(name='Ryszard', second_name='Zorro', born_data=date(1998, 5, 20), skills=None, CV="coś tam",
                        obedience=0.4, preferences=None)

    print('\n')
    teacher_1 = Teacher('Franciszek', 'Lubawy', date(1980, 5, 15), 26, 0.7)
    print(teacher_1.name + ' ' + str(teacher_1.born_data))


    # print(teacher_1.transferKnowledge('Math', student_1))

 #   person_2.defineSkills()
 #   person_2.presentSkills()

    student_1.setPreferences([Skill.BIOLOGY, Skill.MATH])
    student_1.getPreferences()

    print(student_1.getObedience())
    student_1.defineSkills()
    student_1.presentSkills()
    print(student_1.getGeneralKnowledge())
    student_1.presentSkills()
    student_1.getKnowledge(Skill.MATH, 0.1)
    student_1.presentSkills()