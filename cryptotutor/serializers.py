from rest_framework import serializers
from .models import *

"""
    Each of these classes has a model and a fields array. The model connects to the model defined
    in models.py that matches the serializer, while the fields array lists out the fields in each
    model.

    There are a number of serializers commented out; these were included in the original code, but
    became out of scope or redundant at some point in development. They've been kept in the code
    in case future developers decide that these models are better (in the case of inherited models)
    or in case the features that they are used for are implemented (in the case of notifications, etc.)
"""
class CodeSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodeSubmission
        fields = ('id', 'codeSnippet', 'studentUsername', 'threshold')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'StudentName', 'projectLink', 'description', 'title', 'points', 'responses')

class ResponsesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Responses
        fields = ('id', 'reviewerName', 'reviewedAt', 'points', 'solution', 'questionID')

class RequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'studentID', 'studentName', 'VCS', 'requestedAt', 'code', 'errType', 'description')


### NOT IN USE ###
# class InheritedQuestionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = inheritedQuestion
#         fields = ('id', 'codeFragment', 'dataTime', 'fileName', 'question', 'username', 'threshold', 'misuse')

# class InheritedUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = inheritedUser
#         fields = ('id', 'password', 'schoolID', 'userType', 'username')

# class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Notifications
#         fields = ('id', 'requestID', 'responseID')

# class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = keywords
#         fields = ('id', 'keyword')

# class StudentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = student
#         fields = ('id', 'address', 'name')