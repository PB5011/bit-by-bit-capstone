from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:sort_type>', views.index, name='index'),
    path('', views.index, name='index'),
    path('question/<int:id>', views.question, name='question'),
    path('question-form/', views.questionForm, name='question-form'),
    path('code-form/', views.codeForm, name='code-form'),
    path('code-selection/', views.codeSelection, name='code-selection'),
    path('diff-viewer/', views.diffViewer, name='diff-viewer'),
    path('results/', views.nicadResults, name='nicad-results'),
    path('register/', views.register, name='register'),
    path('code-error', views.codeError, name='code-error'),
    path('change-password/', views.changePassword, name='change-password')
]