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
    """ Serializer for the CodeSubmission model """ 
    class Meta:
        model = CodeSubmission
        fields = ('id', 'codeSnippet', 'studentUsername', 'threshold')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Question model """
    class Meta:
        model = Question
        fields = ('id', 'StudentName', 'projectLink', 'description', 'title', 'points', 'responses')

class ResponsesSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Responses model """
    class Meta:
        model = Responses
        fields = ('id', 'reviewerName', 'reviewedAt', 'points', 'solution', 'questionID')


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

# class RequestsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Requests
#         fields = ('id', 'studentID', 'studentName', 'VCS', 'requestedAt', 'code', 'errType', 'description')