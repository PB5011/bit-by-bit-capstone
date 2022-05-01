from rest_framework import serializers
from .models import *

"""
    Each of these classes has a model and a fields array. The model connects to the model defined
    in models.py that matches the serializer, while the fields array lists out the fields in each
    model.
"""
#Bit-by-Bit defined models
class CodeSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodeSubmission
        fields = ('id', 'codeSnippet', 'studentUsername', 'threshold')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'StudentName', 'projectLink', 'description', 'title', 'points', 'responses')


#Client defined models
class InheritedQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inheritedQuestion
        fields = ('id', 'codeFragment', 'dataTime', 'fileName', 'question', 'username', 'threshold', 'misuse')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ('id', 'address', 'name')

class InheritedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inheritedUser
        fields = ('id', 'password', 'schoolID', 'userType', 'username')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = keywords
        fields = ('id', 'keyword')

class ResponsesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = ('id', 'reviewerName', 'reviewedAt', 'points', 'solution', 'questionID')

class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notifications
        fields = ('id', 'requestID', 'responseID')

class RequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'studentID', 'studentName', 'VCS', 'requestedAt', 'code', 'errType', 'description')