from kNowakowska.people.Skill import Skill
from kNowakowska.people.Student import Student
from kNowakowska.people.Teacher import Teacher

if __name__ == '__main__':
    print("Welcome in my School")

    skill = Skill.CHEMISTRY
    print(skill.name)
    print(skill.value)

    teacher = Teacher("Jan", "Nauczyciel", "02-06-1985", 0.5)
    student = Student("Kamil", "Student", "01-05-1995", 1, skills={Skill.ENGLISH: 0.5, Skill.CHEMISTRY:1})

    teacher.defineSkills()

    student.presentYourself()
    student.presentCV()
    student.presentSkills()
    student.setPreferences([Skill.ENGLISH, Skill.BIOLOGY])
    student.getPreferences()
    student.getKnowledge(Skill.CHEMISTRY, 0.2)
    student.getKnowledge(Skill.BIOLOGY, 0.6)

    # teacher.presentYourself()
    # teacher.presentSkills()
