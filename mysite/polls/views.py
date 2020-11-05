from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_iddd):
    return HttpResponse("You're looking at question %s." % question_iddd)

def results(request, question_id):
 #   responseBitch = "You're looking at the results of question %s."
 #   return HttpResponse(responseBitch % question_id)
    return HttpResponse("You're looking at the results of question %s." % question_id)
    

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)