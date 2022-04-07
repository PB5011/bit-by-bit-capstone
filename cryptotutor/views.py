import json
import os
import difflib
from lxml import objectify

from django.shortcuts import render, redirect
#from .models import User,Nicad

from .models import CodeSubmission, User, Nicad, Question



### HOME PAGE ###
def index(request): 
    """View function for home page of site."""

    #TODO: get whatever is necessary for the page
    f = open(os.getcwd() + "/cryptotutor/static/json/sample_questions.json")
    context = {'questions':json.load(f)}
    f.close()

    f.close()

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

    #render html page
    return render(request, 'question.html', context=context)


### QUESTION FORM ###
def questionForm(request):
    """View function for asking a question."""

    #TODO: get whatever is necessary for the page
    context = {}
#     this is just debugging -- keeping it for later in case needed, will delete
#     print(type(request))
#     print(request.method)
#     print(request)      
#     if request.method == 'POST':
#         print("True")
#     else:
#         print("False")

    if request.method == 'POST':
        studentID = request.POST['student_id']
        name = request.POST['student_name']
        link = request.POST['vcs']
        description = request.POST['description']
        new_item = Question(StudentID=studentID, StudentName=name, 
                            projectLink=link, description=description)
#         print(new_item)
#         print(studentID)
#         print(name)
#         print(description)
        new_item.save()



    #render html page
    return render(request, 'question-form.html', context=context)


### CODE FORM ###
def codeForm(request):
    """View function for submitting code for comparison."""

    #TODO: get whatever is necessary for the page
    context = {}

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
        return redirect('code-selection')

    #render html page
    return render(request, 'code-form.html', context=context)


### CODE SELECTION ###
def codeSelection(request):
    """View function for selecting code for the diff viewer."""

    fileLoc = "/cryptotutor/ExtraFiles/TestFiles_functions-blind-crossclones/TestFiles_functions-blind-crossclones-0.30-classes-withsource.xml"

    f = open(os.getcwd() + fileLoc)
    xml = f.read()
    f.close()
    clones = objectify.fromstring(xml)

    for clazz in clones['class']:
        print("classid", clazz.attrib)

    context = {
        "xmlResultFilePath" : os.getcwd() + fileLoc,
        "result": clones
    }

    if request.method == 'POST':
        compareFilePath = request.POST['file']
        #need to get rid of everything before /cryptotutor
        compareFilePath = "/" + compareFilePath.split('/', 2)[2] #make sure everybody tests this; unsure if the file
        request.session['compareFile'] = compareFilePath # setting in the session
        print("request submitted to compare code with file path: ", compareFilePath)
        #navigate to diff viewer
        return redirect('diff-viewer')
        #give the diff viewer the two files... somehow
        


    #render html page
    return render(request, 'code-selection.html', context=context)


### DIFF VIEWER  ###
def diffViewer(request):
    """View function for the diff viewer."""

    #test files to make sure view/diff works
    #file1file = os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json"
    #file2file = os.getcwd() + "/cryptotutor/static/json/sample_question_detail_diff.json"

    #file1lines = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json",'U').readlines()
    #file2lines = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail_diff.json",'U').readlines()


    #submitted files - need to test
    file1file = os.getcwd() + "/cryptotutor/ExtraFiles/SubmittedFiles/Submissions/temp.java"
    file2file = os.getcwd() + request.session['compareFile']

    file1lines = open(os.getcwd() + "/cryptotutor/ExtraFiles/SubmittedFiles/Submissions/temp.java", "U").readlines()
    file2lines = open(os.getcwd() + request.session['compareFile'], 'U').readlines()

    context = {
        "file1": file1file,
        "file2": file2file,
        "diff": difflib.HtmlDiff().make_table(file1lines,file2lines,file1file,file2file)
    }

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'diff-viewer.html', context=context)


### NICAD RESULTS  ###
def nicadResults(request):
    fileLoc = '/' + request.GET.get('file', '/cryptotutor/ExtraFiles/TestFiles_functions-blind-crossclones/TestFiles_functions-blind-crossclones-0.30-classes-withsource.xml')

    f = open(os.getcwd() + fileLoc)
    xml = f.read()
    f.close()
    clones = objectify.fromstring(xml)

    for clazz in clones['class']:
        print("classid", clazz.attrib)

    context = {
        "xmlResultFilePath" : os.getcwd() + fileLoc,
        "result": clones
    }

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'nicad-results.html', context=context)