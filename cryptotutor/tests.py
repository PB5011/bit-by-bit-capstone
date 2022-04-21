from django.test import TestCase, Client
from .models import *
import os.path

# Create your tests here.
class CodeSubmissionTestCase(TestCase):
    def test_codeObject(self):
        new_item = CodeSubmission(codeSnippet="This is a code snippet")
        new_item.save()
        self.assertEqual(new_item.codeSnippet, "This is a code snippet")

    def test_questionObjectPass(self):
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