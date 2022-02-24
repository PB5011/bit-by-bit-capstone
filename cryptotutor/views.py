from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    #TODO: get whatever is necessary for the page
    num_questions = 50
    num_unanswered = 35
    num_answered = 15
    num_users = 25


    context = {
        'num_questions': num_questions,
        'num_unanswered': num_unanswered,
        'num_answered': num_answered,
        'num_users': num_users
    }

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'index.html', context=context)