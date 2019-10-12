import os
import unittest
from unittest.mock import MagicMock, patch

from kNowakowska.people.Skill import Skill
from kNowakowska.people.Student import Student, StudentException


class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student = Student("Jan", "Testowy", "05-08-1991", 0.8)

    def test_generalKnowledge(self):
        self.student.getKnowledge = MagicMock(return_value=1)
        updated_skills = self.student.getGeneralKnowledge([Skill.CHEMISTRY, Skill.MATH], 5)
        self.assertEqual(updated_skills, [1,1])

    def test_setCV(self):
        exp = "My experience"
        hobby = "New hobby"
        self.student.setCV([exp], [hobby])
        self.assertIn(exp, self.student.cv)
        self.assertIn(hobby, self.student.cv)

    def test_downloadCV(self):
        self.student.getSurname = MagicMock(return_value="Surname")
        with patch.object(Student, 'getName', return_value = "Name"):
            self.student.downloadCV()
        self.assertTrue(os.path.exists("Name_Surname_CV.txt"))
        with open("Name_Surname_CV.txt", 'r') as f:
            lines = f.read()
        self.assertEqual(lines, self.student.cv)


    def test_setPreferences(self):
        with self.assertRaises(StudentException) as e:
            self.student.setPreferences("Hi")
        self.assertIn("list", str(e.exception))
        with self.assertRaises(StudentException) as e:
            self.student.setPreferences(["Hi"])
        self.assertIn("skill", str(e.exception))
        self.student.setPreferences([Skill.CHEMISTRY, Skill.MATH])
        self.assertIn(Skill.MATH, self.student.preferences)

    def test_checkSkillLack(self):
        self.student._getSkillValue = MagicMock(return_value=0.5)
        self.assertEqual(self.student.checkSkillLack(Skill.CHEMISTRY), 0.5)

