import json
import os
import difflib

from django.shortcuts import render
#from .models import User,Nicad
from .models import CodeSubmission, User, Nicad, Question


### HOME PAGE ###
def index(request): 
    """View function for home page of site."""

    #TODO: get whatever is necessary for the page
    #f = open(os.getcwd() + "/cryptotutor/static/json/sample_questions.json")
    #context = {'questions':json.load(f)}
    #f.close()
    test = Nicad.callNicad()
    questions = []
    # context = {'questions': Question.objects.all()}
    print(Question.objects.all())
    questionList = Question.objects.all()
    for q in questionList:
        questions.append(
            {'title': q.title, 'author': q.StudentName, 'body': q.description,
             'points': q.points, 'answers': q.responses, 'views': 0}
        )


    context = {'questions': questions}
    print(context)
   # f.close()

    #render html page
    return render(request, 'index.html', context=context)


### QUESTION VIEW ###
def question(request):
    """View function for looking at an individual question."""

    #TODO: get whatever is necessary for the page
    f = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json")
    context = json.load(f)
    f.close()

    f.close()
    # context = {
    #     'questions': Question.objects.all()
    # }

    #render html page
    return render(request, 'question.html', context=context)


### QUESTION FORM ###
def questionForm(request):
    """View function for asking a question."""

    #TODO: get whatever is necessary for the page
    context = {}
    #print(type(request))
    #print(request.method)
    #print(request)      
    #if request.method == 'POST':
    #    print("True")
    #else:
    #    print("False")

    if request.method == 'POST':
        #x = request.POST.get['code']
        #x = request.POST['code']
        ID = request.POST['student_id']
        name = request.POST['student_name']
        link = request.POST['vcs']
        title = request.POST['title']
        description = request.POST['description']
        new_item = Question(StudentID=ID, StudentName=name, 
                            projectLink=link, title=title, description=description)
        #print(new_item)
        #print(title)
        #print(name)
        #print(description)
        new_item.save()
    

    #render html page
    return render(request, 'question-form.html', context=context)


### CODE FORM ###
def codeForm(request):
    """View function for submitting code for comparison."""

    #TODO: get whatever is necessary for the page
    context = {}

    print(type(request))
    print(request.method)
   # print(request)	
   # if request.method == 'POST':
    #    print("True")
    if request.method == 'POST':
        x = request.POST['code']
        #Fixed issue with codesubmission, can now use it for date and names.
        new_item = CodeSubmission(codeSnippet=x)
        new_item.save()
        with open('./cryptotutor/ExtraFiles/SubmittedFiles/Submissions/temp.java', 'w') as f:
            f.writelines('public class temp { \n')
            f.writelines('public static void main(String[] args) { \n')
            f.writelines(new_item.codeSnippet)
            f.writelines('\n}\n')
            f.writelines('}')
            f.close()
        Nicad.callNicad()

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
    file1file = os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json"
    file2file = os.getcwd() + "/cryptotutor/static/json/sample_question_detail_diff.json"


    file1lines = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json",'U').readlines()
    file2lines = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail_diff.json",'U').readlines()

    context = {
        "file1": file1file,
        "file2": file2file,
        "diff": difflib.HtmlDiff().make_table(file1lines,file2lines,file1file,file2file)
    }

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'diff-viewer.html', context=context)
