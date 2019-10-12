from kNowakowska.people.konradzadanietest.Skill import Skill
from kNowakowska.people.konradzadanietest.Student import Student
from kNowakowska.people.konradzadanietest.Teacher import Teacher

if __name__ == '__main__':
    print("Welcome in my School")

    skill = Skill.CHEMISTRY
    print(skill.CHEMISTRY.name)
    print(skill.CHEMISTRY.value)

    teacher = Teacher("Jan", "Nauczyciel", "02-06-1985", 0.5)
    student = Student("Kamil", "Student", "01-05-1995", {Skill.ENGLISH: 0.5})

    teacher.defineSkills()

    student.presentYourself()
    student.presentSkills()
    student.setPreferences([Skill.BIOLOGY, Skill.ENGLISH])
    student.getPreferences()

    student.getKnowledge(Skill.CHEMISTRY, 0.2)
    #
    # teacher.presentYourself()
    # teacher.presentSkills()
