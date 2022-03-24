from django.db import models
from django.urls import reverse
import subprocess
from xml.dom import minidom

# Create your models here.
class User(models.Model):
    """Class defining a user of CryptoTutor"""

    #fields
    #TODO: flesh these out past the very basics
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    #metadata
    class Meta:
        ordering = ['username', 'password']

    #methods
    def get_absolute_url(self):
        """returns the url to access a particular instance of User"""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the User object (in Admin site etc.)"""
        return self.username + self.password

class Nicad(models.Model):
    """Class defining nicad use?"""

    #methods
    def callNicad():
        subprocess.Popen(["nicad6cross", "blocks", "java", "./cryptotutor/ExtraFiles/SubmittedFiles/Submissions", "./cryptotutor/ExtraFiles/TestFiles", "default-report"], shell=False)
        return True 

class CodeSubmission(models.Model):
    codeSnippet = models.TextField()
