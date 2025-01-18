from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h3>Hello World!</h3>")

def job_details(request, id):
    # return HttpResponse(f"<h1>This is the job detail page {id}</h1>")
    site = "http://google.com"

    return HttpResponse(f"Visit <a href={site}> Google here </a>")
