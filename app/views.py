from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First Job description",
    "Second Job description",
    "Third Job description"
]


# def hello(request):
#     return HttpResponse("<h3>Hello World!</h3>")

def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse('job_detail', args=(job_id,))
        list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)


def job_details(request, id):
    print(type(id))

    if id == 0:
        return redirect(reverse('job_home'))
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"

    return HttpResponse(return_html)
