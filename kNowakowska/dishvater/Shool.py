from Student import Student
from Teacher import Teacher
from Skill import Skill

if __name__ == '__main__':
    print("Welcome in my Shool")

    # skill = Skill.CHEMISTRY
    # print(skill.name)
    # print(skill.value)

    teacher = Teacher("Jan", "Nauczyciel", "02-06-1985", 0.5)
    student = Student("Kamil", "Student", "02-06-1985", 0.2, {Skill.ENGLISH: 0.5})

    teacher.defineSkills()

    student.presentYourself()
    student.presentSkills()

    teacher.presentYourself()
    teacher.presentSkills()

    student.setPreferences([Skill.CHEMISTRY, Skill.BIOLOGY, Skill.MATH])
    student.getPreferences()

    student.getKnoledge(Skill.ENGLISH, 0.2)
    student.getKnoledge(Skill.CHEMISTRY, 0.2)
