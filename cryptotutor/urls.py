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

from django.urls import path, include
from . import views

"""
This file defines all URL patterns for the CryptoTutor web application. URLs are mapped
between this class and the associated view function for Django to process.
"""

urlpatterns = [
    path('<str:sort_type>', views.index, name='index'),
    path('', views.index, name='index'),
    path('question/<int:id>', views.question, name='question'),
    path('delete-question/<int:id>', views.delete_question, name='delete-question'),
    path('question-form/', views.questionForm, name='question-form'),
    path('code-form/', views.codeForm, name='code-form'),
    path('code-selection/', views.codeSelection, name='code-selection'),
    path('diff-viewer/', views.diffViewer, name='diff-viewer'),
    path('results/', views.nicadResults, name='nicad-results'),
    path('register/', views.register, name='register'),
    path('change-password/', views.changePassword, name='change-password')
]