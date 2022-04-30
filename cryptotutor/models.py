import subprocess,uuid,glob,os
from django.db import models
from django.urls import reverse

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
    """Class defining nicad use"""

    # methods
    def callNicad(studentUsername, threshold):
        location = "./cryptotutor/ExtraFiles/SubmittedFiles/" + studentUsername + "/Submissions"
        nc = subprocess.Popen(["nicad6cross", "blocks", "java", location,
                          "./cryptotutor/ExtraFiles/TestFiles", threshold], shell=False)

        nc.wait()
        return True

    def cleanNicad(studentUsername):
        list1 = glob.glob("./cryptotutor/ExtraFiles/TestFiles_*")
        list2 = glob.glob("./cryptotutor/ExtraFiles/SubmittedFiles/" + studentUsername + "/Submissions_*")
        list3 = glob.glob("./cryptotutor/ExtraFiles/SubmittedFiles/" + studentUsername + "/Submissions_*/Submissions_*")
        for f in list1:
            try:
                os.remove(f)
            except:
                print("")
        for f in list2:
            try:
                os.remove(f)
            except:
                print("")
        for f in list3:
            try:
                os.remove(f)
            except:
                print("")
        


class CodeSubmission(models.Model):
    codeSnippet = models.TextField()
    studentUsername = models.TextField()
    threshold = models.TextField()


class Question(models.Model):
    # CATEGORIES = (
    #     ('T1', 'Tag1'),
    #     ('T2', 'Tag2'),
    #     ('T3', 'Tag3'),
    # format: ('InternalVariableName', 'UIButtonName'),
    # ) # change as needed, not implemented yet

    id = models.AutoField(primary_key=True)
    #StudentID = models.CharField(max_length=10) 
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
    #studentID = models.IntegerField()
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