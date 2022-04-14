from rest_framework import serializers
from .models import inheritedQuestion #, student, inheritedUser, etc.

class InheritedQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inheritedQuestion
        fields = ('codeFragment', 'dataTime', 'fileName', 'question', 'studentID', 'username', 'threshold', 'misuse')

#TODO: add rest of the tables in here