from django.shortcuts import render
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


# Create your views here.

def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        first_name = request.POST['firstname']
        last_name = request.POST['firstname']
        email = request.POST['email']
        print("Post Request: ",email)
        if email =="":
            email_error = "Please enter a valid email address"

        subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        subscribe.save()

    context = {"form":subscribe_form,"email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)