from django import forms
from django.db import models
from django.forms import ModelForm

from cryptotutor.models import *


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['qStudentID','qStudentName','projectLink', 'description']

class CodeForm(ModelForm):
    class Meta:
        model = CodeSub
        fields = ['studentID','studentName','codeFragments']
