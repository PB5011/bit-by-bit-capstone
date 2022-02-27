import json
import os

from django.shortcuts import render
from .models import User

# Create your views here.
def index(request): 
    """View function for home page of site."""

    #TODO: get whatever is necessary for the page
    f = open(os.getcwd() + "/cryptotutor/static/json/sample_questions.json")
    context = {'questions':json.load(f)}

    #render html page - will need to add context/data once it's retrieved above
    return render(request, 'index.html', context=context)