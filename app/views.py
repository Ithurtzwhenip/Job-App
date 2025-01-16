from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")

def job_details(request):
    return HttpResponse("This is the job details")

