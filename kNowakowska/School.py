from kNowakowska.people.Skill import Skill
from kNowakowska.people.Student import Student
from kNowakowska.people.Teacher import Teacher

if __name__ == '__main__':
    print("Welcome in my School")

    #comment
    skill = Skill.CHEMISTRY
    print(skill.name)
    print(skill.value)

    teacher = Teacher("Jan", "Kowalski", "02-06-1985", 0.5)
    student = Student("Kamil", "Student", "01-01-1995", 1, skills =  {Skill.ENGLISH: 0.5}, preferences = [Skill.BIOLOGY])

    teacher.defineSkills()

    student.presentYourself()
    student.presentSkills()

    teacher.presentYourself()
    teacher.presentSkills()


    student.getPreferences()

    student.getKnowledge(Skill.ENGLISH, 0.2)