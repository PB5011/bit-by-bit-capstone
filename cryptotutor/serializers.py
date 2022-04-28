from rest_framework import serializers
from .models import CodeSubmission, Question, inheritedQuestion, student, inheritedUser, answers, keywords, responses, Notifications, Requests

#Bit-by-Bit defined models
class CodeSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodeSubmission
        fields = ('codeSnippet')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'StudentID', 'StudentName', 'projectLink', 'description', 'title', 'points', 'responses')


#Client defined models
class InheritedQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inheritedQuestion
        fields = ('id', 'codeFragment', 'dataTime', 'fileName', 'question', 'studentID', 'username', 'threshold', 'misuse')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = student
        fields = ('address', 'name')

class InheritedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = inheritedUser
        fields = ('password', 'schoolID', 'userType', 'username')

class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = answers
        fields = ('answer', 'questionID', 'studentID', 'username')

class KeywordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = keywords
        fields = ('keyword')

class ResponsesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = responses
        fields = ('requestID', 'reviewerName', 'reviewedAt', 'voteUp', 'voteDown', 'solution')

class NotificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notifications
        fields = ('requestID', 'responseID')

class RequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requests
        fields = ('studentID', 'studentName', 'VCS', 'requestedAt', 'code', 'errType', 'description')