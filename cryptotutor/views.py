import json
import os

from django.shortcuts import render
from .models import User,Nicad

### HOME PAGE ###
def index(request): 
    """View function for home page of site."""

    #TODO: get whatever is necessary for the page
    f = open(os.getcwd() + "/cryptotutor/static/json/sample_questions.json")
    context = {'questions':json.load(f)}
    test = Nicad.callNicad()

    #render html page
    return render(request, 'index.html', context=context)


### QUESTION VIEW ###
def question(request):
    """View function for looking at an individual question."""

    #TODO: get whatever is necessary for the page
    context = {}
    f = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json")
    context = json.load(f)

    #render html page
    return render(request, 'question.html', context=context)


### QUESTION FORM ###
def questionForm(request):
    """View function for asking a question."""

    #TODO: get whatever is necessary for the page
    context = {}

    #render html page
    return render(request, 'question-form.html', context=context)


### CODE FORM ###
def codeForm(request):
    """View function for submitting code for comparison."""

    #TODO: get whatever is necessary for the page
    context = {}

    #render html page
    return render(request, 'code-form.html', context=context)


### CODE SELECTION ###
def codeSelection(request):
    """View function for selecting code for the diff viewer."""

    #TODO: get whatever is necessary for the page
    context = {}

    #render html page
    return render(request, 'code-selection.html', context=context)


### DIFF VIEWER  ###
def diffViewer(request):
    """View function for the diff viewer."""

    #TODO: get whatever is necessary for the page
    context = {}

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'diff-viewer.html', context=context)
