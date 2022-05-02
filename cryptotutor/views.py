from datetime import datetime
import os,difflib,glob,traceback
from lxml import objectify

from django.shortcuts import render, redirect

from cryptotutor.serializers import QuestionSerializer
from django.contrib.auth.forms import UserCreationForm
from django.db.models import F
from .models import CodeSubmission, Nicad, Question, Responses

"""
This file defines all views for the CryptoTutor web application. This is where
http requests and responses throughout the app go through.
"""

### HOME PAGE ###
def index(request, sort_type=''): 
    """View function for home page of site.

    Retrieves all questions from the database. Sorting is not yet implemented because of
    prerequisites, but code has been left in and commented out to give a reference point
    of how it would be implemented using the sort_type URL param.

    Args:
        request: A request to view the home page.

    Returns:
        An HttpResponse with the original request, the home page url, and the
        context of the page. Context of the page includes all questions from the database.
    """
    
    questions = []

    # if sort_type == 'popularity':
        # questionList = Question.objects.all().order_by('points')
    # else if sort_type == 'newest': - requires dateTime to be added to questions
    # else if filtering by tags - requires keywords/tags to be added
    # else: #default sorting
    questionList = Question.objects.all()

    # serializer_class = QuestionSerializer

    for q in questionList:
        questions.append(
            {'id': q.id, 'title': q.title, 'author': q.StudentName, 'body': q.description,
             'points': q.points, 'answers': q.responseNumber, 'views': 0}
        )

    context = {'questions': questions}
   # print(context)

    #render html page
    return render(request, 'index.html', context=context)

### LOGIN PAGE ###
def login(request): 
    """View function for login page of site.

    A form for users to login.

    Args:
        request: A request to view the login page.

    Returns:
        An HttpResponse with the original request, the login page url, and the
        context of the page. The context of the page is empty because it is a simple form.
    """

    form = AuthenticationForm()

    context = { 'form': form }


    #render html page
    return render(request, 'login.html', context=context)


### QUESTION VIEW ###
def question(request, id):
    """View function for looking at an individual question.
    
    Currently retrieves questions from a json file of sample questions and
    answers. This will be updated to pull questions from the client-given database.

    Args:
        request: A request to view the individual question's page.

    Returns:
        An HttpResponse with the original request, the question page url, and the
        context of the page. Context of the page includes the questions and answers from
        the json file.
    """

    #this gets the sample question
    # f = open(os.getcwd() + "/cryptotutor/static/json/sample_question_detail.json")
    # context = json.load(f)
    # f.close()

    #retrieving questions and answers
    answers = []
    q = Question.objects.get(id=id)
    answerList = Responses.objects.filter(questionID=id)
    # answerList = Responses.objects.all()

    #TODO: add some responses and make sure this works
    for a in answerList:
        answers.append(
            {'answer': a.solution, 'questionID': a.questionID, 'username': a.reviewerName, 'points': a.points,
            'time': a.reviewedAt, 'id': a.id}
        )

    context = {
        'q': q,
        'responses': answers
    }

    #form for adding a response
    if request.method == 'POST':
        username = request.user.username
        time = datetime.now()
        p = 0
        s = request.POST['solution']
        new_item = Responses(reviewerName = username, reviewedAt = time, points = p, solution = s, questionID = q)

        new_item.save()

        Question.objects.all().filter(id=id).update(responseNumber=F('responseNumber') + 1)

        return redirect('question', id=id)

    #render html page
    return render(request, 'question.html', context=context)


### QUESTION FORM ###
def questionForm(request):
    """View function for asking a question.
    
    This is a form for submitting ("asking") a question on the CryptoTutor web
    application. Questions are submitted through the form to this function, and
    will eventually be passed to the database.
    
    Args:
        request: A request to view the form to ask a question. Once the user is
            done with the form and would like to submit their question, the fields
            are returned to this function as well to store and eventually be put into
            the database.

    Returns:
        An HttpResponse with the original request, the question submission page url,
        and the context of the page. This page requires no context to be rendered. 
    """

    context = {}
    #print(type(request))
    #print(request.method)
    #print(request)      
    #if request.method == 'POST':
    #    print("True")
    #else:
    #    print("False")

    if request.method == 'POST':
        #ID = request.POST['student_id']
        name = request.POST['student_name']
        link = request.POST['vcs']
        title = request.POST['title']
        description = request.POST['description']
        new_item = Question(StudentName=name, 
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
    """View function for submitting code for comparison.
    
    This is a form for submitting code to the CryptoTutor code comparison tool.

    Args:
        request: A request to view the form to submit code. Once the user is done
            with the form and would like to submit their code, the fields are returned
            to this function to store in a new file before NiCad is called.

    Returns:
        An HttpResponse with the original request, the code submission page url, and
        the context of the page. This page requires no context to be rendered.
    """

    #TODO: get whatever is necessary for the page
    context = {}

    #print(type(request))
    #print(request.method)
   # print(request)	
   # if request.method == 'POST':
    #    print("True")
    if request.method == 'POST':
        x = request.POST['code']
        y = request.POST['student_name']
        z = request.POST['threshold']
        #Fixed issue with codesubmission, can now use it for date and names.
        new_item = CodeSubmission(codeSnippet=x, studentUsername=y, threshold=z)
        new_item.save()
        openLoc = './cryptotutor/ExtraFiles/SubmittedFiles/' + new_item.studentUsername + '/Submissions/temp.java'
        Nicad.cleanNicad(new_item.studentUsername)
        if not os.path.exists('./cryptotutor/ExtraFiles/SubmittedFiles/' + new_item.studentUsername + '/Submissions/'):
            os.makedirs('./cryptotutor/ExtraFiles/SubmittedFiles/' + new_item.studentUsername + '/Submissions/')
        with open(openLoc, 'w') as f:
            f.writelines('public class temp { \n')
            f.writelines('public static void main(String[] args) { \n')
            f.writelines(new_item.codeSnippet)
            f.writelines('\n}\n')
            f.writelines('}')
            f.close()

            try:
                test = Nicad.callNicad(new_item.studentUsername, new_item.threshold)
            except FileNotFoundError:
                print('WARNING: NiCad or the configurations were not found on this system.')

        return redirect('code-selection')

    #render html page
    return render(request, 'code-form.html', context=context)


### CODE SELECTION ###
def codeSelection(request):
    """View function for selecting code for the diff viewer.
    
    This is where users can select which code they would like to compare with
    their own code submission.
    
    Args:
        request: A request to view the form to select which code to view in the diff
            viewer. This is also a form that can be submitted; once submitted, the
            selected code is given to the function to forward to the diff viewer.
        
    Returns:
        An HttpResponse with the original request, the code selection page url, and
        the context of the page. Context of this page includes the path of the NiCad result
        file and the parsed result file.
    """
    try:
        list = glob.glob("./cryptotutor/ExtraFiles/SubmittedFiles/" + str(request.user) + "/Submissions_*/Submissions_blocks-blind-crossclones-*-classes-withsource.xml")
        fileLoc = str(list[0])
        print(fileLoc)
        f = open(fileLoc)
        xml = f.read()
        f.close()
        clones = objectify.fromstring(xml)

        for clazz in clones['class']:
            print("classid", clazz.attrib)

        context = {
            "xmlResultFilePath" : fileLoc,
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
    except AttributeError:
        Nicad.cleanNicad(str(request.user))
        #traceback.print_exc()
        return render(request, 'attribute-error.html')
    except FileNotFoundError:
        Nicad.cleanNicad(str(request.user))
        #traceback.print_exc()
        return render(request, 'file-not-found-error.html')
    except:
        Nicad.cleanNicad(str(request.user))
        #traceback.print_exc()
        return render(request, 'general-error.html')


### DIFF VIEWER  ###
def diffViewer(request):
    """View function for the diff viewer.
    
    This is where users can see the differences between their submitted code and
    the code they selected on the code selection page.

    Args:
        request: A request to view the diff viewer with submitted and selected code.

    Returns:
        An HttpResponse with the original request, the diff viewer page url, and the
        context of the page. The context of this page includes the submitted file, the
        selected file, and the diff view comparing them.
    """

    file1file = "./cryptotutor/ExtraFiles/SubmittedFiles/" + str(request.user) + "/Submissions/temp.java"
    file2file = os.getcwd() + "/cryptotutor" + request.session['compareFile']

    file1lines = open("./cryptotutor/ExtraFiles/SubmittedFiles/" + str(request.user) + "/Submissions/temp.java", "U").readlines()
    file2lines = open(os.getcwd() + "/cryptotutor" + request.session['compareFile'], 'U').readlines()

    context = {
        "file1": file1file,
        "file2": file2file,
        "diff": difflib.HtmlDiff().make_table(file1lines,file2lines,file1file,file2file)
    }

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'diff-viewer.html', context=context)


### NICAD RESULTS  ###
def nicadResults(request):
    """View function for the NiCad results.

    This function is mostly intended for developer use. It displays the results
    from a NiCad run as given by the relevant file.

    Args:
        request: A request to view the results of a NiCad run.
        
    Returns:
        An HttpResponse with the original request, the NiCad results url, and
        the context of the page. Context of this page includes the path of the NiCad result
        file and the parsed result file.
    
    """
    try:

        list = glob.glob("./cryptotutor/ExtraFiles/SubmittedFiles/" + str(request.user) + "/Submissions_*/Submissions_*")
        fileLoc = str(list[1])
        print(fileLoc)
        f = open(fileLoc)
        xml = f.read()
        f.close()
        clones = objectify.fromstring(xml)

        for clazz in clones['class']:
            print("classid", clazz.attrib)

        context = {
            "xmlResultFilePath" : fileLoc,
            "result": clones
        }
        return render(request, 'nicad-results.html', context=context)
    except AttributeError:
        print(traceback.format_exc())
        Nicad.cleanNicad(str(request.user))
        return render(request, 'attribute-error.html')
    except FileNotFoundError:
        print(traceback.format_exc())
        Nicad.cleanNicad(str(request.user))
        return render(request, 'file-not-found-error.html')
    except:
        print(traceback.format_exc())
        Nicad.cleanNicad(str(request.user))
        return render(request, 'general-error.html')

  

def register(request):
    """View function for the registration form.

    This function serves the view for the user registration form. It utilizes
    the built-in Django UserCreationForm method to populate the form.

    Args:
        request: A request to view the registration page.
        
    Returns:
        An HttpResponse with the original request, and the resulting registration
        form contained within the context.
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Account registered successfully. You may now login.'
        else:
            message = 'There was an error with your registration form. Please try again.'
            
    else:
        form = UserCreationForm()
        message = ''

    context = { 'form': form, 'message': message }

    return render(request, 'registration/register.html', context=context)


def codeError(request):
    return render(request, 'code-error.html')