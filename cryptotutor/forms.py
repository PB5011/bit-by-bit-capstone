"""Facilitates mapping models to form submissions."""

from django.forms import ModelForm
from cryptotutor.models import *


class QuestionForm(ModelForm):
    """Class defining models in use by question form"""
    class Meta:
        """Class defining metadata for models in use by question form"""
        model = Question
        fields = ['StudentName','StudentName','projectLink', 'description']

class CodeForm(ModelForm):
    """Class defining models in use by code form"""
    class Meta:
        """Class defining metadata for models in use by code form"""
        #model = CodeSub
        fields = ['studentID','studentName','codeFragments']
