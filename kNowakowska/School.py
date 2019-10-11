from kNowakowska.people.Skill import Skill
from kNowakowska.people.Student import Student
from kNowakowska.people.Teacher import Teacher

if __name__ == '__main__':
    print("Welcome in my School")

    teacher_biology = Teacher(name="Jan", surname="Nauczycielski", dateOfBirth="01-12-1985", engagement=0.1)
    student = Student("Karol", "Kruczek", "25-03-2005", 0.9, skills={Skill.HISTORY: 0.5}, preferences=[Skill.HISTORY])

    teacher_biology.presentYourself()
    teacher_biology.checkVacationLeft()
    teacher_biology.takeVacation(15)
    teacher_biology.checkVacationLeft()

    student.presentYourself()
    student.presentCV()
    student.setCV(["2010: Intel Technology Poland", "2014: Allegro Sp. z o.o"], ["Dancing", "Coding", "Living"])
    student.presentCV()
    student.downloadCV()
    student.getPreferences()
    student.presentSkills()
    student.getKnowledge(Skill.HISTORY, 0.1)
    student.presentSkills()
    student.getKnowledge(Skill.ENGLISH, 0.2)
    student.presentSkills()
