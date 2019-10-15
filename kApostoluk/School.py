from kApostoluk.people.Skill import Skill
from kApostoluk.people.Teacher import Teacher
from kApostoluk.people.Student import Student
from kApostoluk.people.Skill import Skill

if __name__ == '__main__':
    print("Welcome in my School")

    skill = Skill.CHEMISTRY
    print(skill.name)
    print(skill.value)

teacher = Teacher("Jan", "Nauczyciel" , "02-06-1985", 0.5)

student = Student('Kamil', 'Student', '01-05-2015', {Skill.ENGLISH: 0.5})

student.SetPreferences(['BIOLOGY', 'MATH'])
student._getSkillValue('ENGLISH')

teacher.defineSkills()

student.presentYourself()
student.presentSkills()

teacher.presentYourself()
teacher.presentSkills()

