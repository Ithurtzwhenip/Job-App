from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First Job description",
    "Second Job description"
]


def hello(request):
    return HttpResponse("<h3>Hello World!</h3>")


def job_details(request, id):
    print(type(id))

    if id ==0:
        return redirect('/')
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"

    return HttpResponse(return_html)

