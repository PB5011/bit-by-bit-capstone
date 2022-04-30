from django.forms import ModelForm
from cryptotutor.models import *


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['StudentID','StudentName','projectLink', 'description']

class CodeForm(ModelForm):
    class Meta:
        #model = CodeSub
        fields = ['studentID','studentName','codeFragments']
