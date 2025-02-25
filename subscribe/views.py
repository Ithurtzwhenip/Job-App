from django.shortcuts import render
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("Valid form")
    context = {"form": subscribe_form, "email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)
