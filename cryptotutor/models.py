from django.db import models
from django.urls import reverse
import subprocess
from xml.dom import minidom
import uuid


# Create your models here.
class User(models.Model):
    """Class defining a user of CryptoTutor"""

    # fields
    # TODO: flesh these out past the very basics
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    # metadata
    class Meta:
        ordering = ['username', 'password']

    # methods
    def get_absolute_url(self):
        """returns the url to access a particular instance of User"""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the User object (in Admin site etc.)"""
        return self.username + self.password


class Nicad(models.Model):
    """Class defining nicad use?"""

    # methods
    def callNicad():
        subprocess.Popen(["nicad6cross", "blocks", "java", "./cryptotutor/ExtraFiles/SubmittedFiles/Submissions",
                          "./cryptotutor/ExtraFiles/TestFiles", "default-report"], shell=False)
        return True


class CodeSubmission(models.Model):
    codeSnippet = models.TextField()


class Question(models.Model):
    # CATEGORIES = (
    #     ('T1', 'Tag1'),
    #     ('T2', 'Tag2'),
    #     ('T3', 'Tag3'),
    # format: ('InternalVariableName', 'UIButtonName'),
    # ) # change as needed, not implemented yet

    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    StudentID = models.CharField(max_length=10) 
    StudentName = models.CharField(max_length=50)
    projectLink = models.CharField(max_length=50)
    description = models.TextField()
    title = models.CharField(max_length=100, default='test')
    points = models.IntegerField(default='0')
    responses = models.PositiveSmallIntegerField(default='0')
    
    def __str__(self):
        return self.id



class inheritedQuestion(models.Model):
    codeFragment = models.CharField(max_length=2048)
    dataTime = models.CharField(max_length=255)
    fileName = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    studentID = models.IntegerField()
    username = models.CharField(max_length=255)
    threshold = models.CharField(max_length=255)
    misuse = models.CharField(max_length=255)


class student(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class inheritedUser(models.Model):
    password = models.CharField(max_length=255)
    schoolID = models.IntegerField()
    userType = models.IntegerField()
    username = models.CharField(max_length=255)


class answers(models.Model):
    answer = models.CharField(max_length=255)
    questionID = models.IntegerField()
    studentID = models.IntegerField()
    username = models.CharField(max_length=255)


class keywords(models.Model):
    # keywordID = models.PositiveSmallIntegerField()
    keyword = models.CharField(max_length=255)


class responses(models.Model):
    # responseID = models.PositiveSmallIntegerField()
    requestID = models.PositiveSmallIntegerField()
    reviewerName = models.CharField(max_length=255)
    reviewedAt = models.DateTimeField()
    voteUp = models.PositiveSmallIntegerField()
    voteDown = models.PositiveSmallIntegerField()
    solution = models.TextField()


class Notifications(models.Model):
    # notificationID = models.PositiveSmallIntegerField()
    requestID = models.PositiveSmallIntegerField()
    responseID = models.PositiveSmallIntegerField()


class Requests(models.Model):
    # requestID = models.PositiveSmallIntegerField()
    studentID = models.PositiveSmallIntegerField()
    studentName = models.CharField(max_length=20)
    VCS = models.CharField(max_length=255)
    requestedAt = models.DateTimeField()
    code = models.TextField()
    errType = models.CharField(max_length=20)
    description = models.TextField()
