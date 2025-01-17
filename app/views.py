from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")

def job_details(request, id):
    return HttpResponse(f"This is the job detail page {id}")

