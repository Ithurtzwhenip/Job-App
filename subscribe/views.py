from django.shortcuts import render, redirect
from django.urls import reverse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
    context = {"form": subscribe_form, "email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
