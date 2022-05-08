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

import subprocess,uuid,glob,os,datetime
from django.db import models
from django.urls import reverse

"""
This file contains all models used in the cryptotutor application. Models provide information
about data, including the essential fields and behaviors of the data being stored. Each model maps
to a single database table. The only model not related to the database is the NiCad model, used to define
methods related to the NiCad process.

There are a number of models commented out; these were included in the original code, but
became out of scope or redundant at some point in development. They've been kept in the code
in case future developers decide that these models are better (in the case of inherited models)
or in case the features that they are used for are implemented (in the case of notifications, etc.)
"""


class Nicad(models.Model):
    """Class defining methods involving NiCad"""

    # methods
    def callNicad(studentUsername, threshold):
        """Function for running the NiCad process.
    
        This function calls the nicad6cross process to operate on the code that is
        submitted by the student. The code must already exist within the submissions
        folder, which is defined by the location variable.

        :param studentUsername: The student's username
        :param threshold: The threshold that NiCad should run at. This is an alias for
                the configuration filename located within the NiCad installation
                directory.
        """
        location = "./cryptotutor/ExtraFiles/SubmittedFiles/" + studentUsername + "/Submissions"
        print("running nicad6cross blocks java", location, "./cryptotutor/ExtraFiles/TestFiles", threshold)
        nc = subprocess.Popen(["nicad6cross", "blocks", "java", location,
                          "./cryptotutor/ExtraFiles/TestFiles", threshold], shell=False)

        nc.wait()
        return True

    def cleanNicad(studentUsername):
        """Function for cleaning the student's NiCad folder.
    
        This function cleans the NiCad folders associated with the student's username.
        Used primarily for when NiCad encounters errors, as it was discovered NiCad
        output should be cleaned upon error.

        :param studentUsername: The student's username.
        """
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
    """Model for CodeSubmission"""
    id = models.AutoField(primary_key=True)
    codeSnippet = models.TextField()
    studentUsername = models.TextField(default="anonymous")
    threshold = models.TextField(default="0") #if it's ever 0 in the DB then there's a problem somewhere


class Question(models.Model):
    """Model for Questions"""
    # CATEGORIES = (
    #     ('T1', 'Tag1'),
    #     ('T2', 'Tag2'),
    #     ('T3', 'Tag3'),
    # format: ('InternalVariableName', 'UIButtonName'),
    # ) # change as needed, not implemented yet
    id = models.AutoField(primary_key=True)
    #StudentID = models.CharField(max_length=10) 
    StudentName = models.CharField(max_length=50, default='')
    projectLink = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    title = models.CharField(max_length=100, default='test')
    points = models.IntegerField(default='0')
    responseNumber = models.PositiveSmallIntegerField(default='0')
    views = models.PositiveIntegerField(default='0')
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

class Responses(models.Model):
    """Model for (Question) Responses"""
    id = models.AutoField(primary_key=True)
    reviewerName = models.CharField(max_length=255, default='')
    reviewedAt = models.DateTimeField(default='')
    points = models.IntegerField(default=0)
    solution = models.TextField(default='')
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)


### NOT IN USE ###
# class inheritedQuestion(models.Model):
#     id = models.AutoField(primary_key=True)
#     codeFragment = models.CharField(max_length=2048)
#     dataTime = models.CharField(max_length=255)
#     fileName = models.CharField(max_length=255)
#     question = models.CharField(max_length=255)
#     #studentID = models.IntegerField()
#     username = models.CharField(max_length=255)
#     threshold = models.CharField(max_length=255)
#     misuse = models.CharField(max_length=255)

# class inheritedUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     password = models.CharField(max_length=255)
#     schoolID = models.IntegerField()
#     userType = models.IntegerField()
#     username = models.CharField(max_length=255)

# class keywords(models.Model):
#     id = models.AutoField(primary_key=True)
#     keyword = models.CharField(max_length=255)

# class Notifications(models.Model):
#     id = models.AutoField(primary_key=True)
#     requestID = models.ForeignKey(Requests, on_delete=models.CASCADE)
#     responseID = models.ForeignKey(Responses, on_delete=models.CASCADE)

# class student(models.Model):
#     id = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)

# class Requests(models.Model):
#     """Model for Requests"""
#     id = models.AutoField(primary_key=True)
#     studentID = models.PositiveSmallIntegerField()
#     studentName = models.CharField(max_length=20)
#     VCS = models.CharField(max_length=255)
#     requestedAt = models.DateTimeField()
#     code = models.TextField()
#     errType = models.CharField(max_length=20)
#     description = models.TextField()
