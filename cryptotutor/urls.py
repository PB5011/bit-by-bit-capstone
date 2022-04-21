from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/', views.question, name='question'),
    path('question-form/', views.questionForm, name='question-form'),
    path('code-form/', views.codeForm, name='code-form'),
    path('code-selection/', views.codeSelection, name='code-selection'),
    path('diff-viewer/', views.diffViewer, name='diff-viewer'),
    path('results/', views.nicadResults, name='nicad-results'),
]