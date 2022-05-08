# CryptoTutor - A question and answer forum with code comparison capabilities.
# Copyright (C) 2022 Zoe Larson, Maya Lentsch, Tyler Bauer, Daniel Brinkman

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.test import TestCase, Client
from .models import *
import os.path

"""
This file contains a series of test cases for testing the backend database and
the various core functions of the application.
"""

# Create your tests here.
class CodeSubmissionTestCase(TestCase):
    """ Test case for code submission """
    def test_codeObject(self):
        """ Tests that a code snippet is saved correctly to the database. """
        new_item = CodeSubmission(codeSnippet="This is a code snippet")
        new_item.save()
        self.assertEqual(new_item.codeSnippet, "This is a code snippet")

    def test_questionObjectPass(self):
        """ Tests that a question is saved correctly to the database. """
        new_item = Question(StudentID = "123456",StudentName="Rob Zombie",projectLink="https://pancakes.com",description="Pancakes")
        new_item.save()
        self.assertEqual(new_item.StudentID, "123456")
        self.assertEqual(new_item.StudentName, 'Rob Zombie')
        self.assertEqual(new_item.projectLink, "https://pancakes.com")
        self.assertEqual(new_item.description, "Pancakes")

   # def test_questionObjectFail(self):
    #    new_item = Question(StudentID = "123456",StudentName="Rob Zombie",projectLink="https://pancakes.com",description="Pancakes")
   #     new_item.save()
   #     self.assertEqual(new_item.StudentID, "12346")
   #     self.assertEqual(new_item.StudentName, 'Rob Zobie')
   #     self.assertEqual(new_item.projectLink, "https://pacakes.com")
   #     self.assertEqual(new_item.description, "Pancaes")

    def test_inheritedQuestionObject(self):
        new_item = inheritedQuestion(codeFragment = "This is code",dataTime = "12pm",fileName="pancakes.java",question="question?",studentID="123456",username="usernameStudent",threshold="50",misuse="yes")
        new_item.save()
        self.assertEqual(new_item.codeFragment, "This is code")
        self.assertEqual(new_item.dataTime, "12pm")
        self.assertEqual(new_item.fileName, "pancakes.java")
        self.assertEqual(new_item.question, "question?")
        self.assertEqual(new_item.studentID, "123456")
        self.assertEqual(new_item.username, "usernameStudent")
        self.assertEqual(new_item.threshold, "50")
        self.assertEqual(new_item.misuse, "yes")

    def test_studentObject(self):
        new_item = student(address="street address 111",name="Rob Zombie")
        new_item.save()
        self.assertEqual(new_item.address, "street address 111")
        self.assertEqual(new_item.name, "Rob Zombie")

    def test_nicadCreateFiles(self):
        new_item = CodeSubmission(codeSnippet="This is a code snippet")
        new_item.save()
        with open('./cryptotutor/ExtraFiles/SubmittedFiles/Submissions/temp.java', 'w') as f:
            f.writelines('public class temp { \n')
            f.writelines('public static void main(String[] args) { \n')
            f.writelines(new_item.codeSnippet)
            f.writelines('\n}\n')
            f.writelines('}')
            f.close()
        Nicad.callNicad()
        self.assertTrue(os.path.exists('./cryptotutor/ExtraFiles/SubmittedFiles/Submissions_blocks-blind-crossclones'))

    #Maybe a test about post data?