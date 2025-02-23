from django.shortcuts import render

# Create your views here.

def subscribe(request):
    email_error = ""
    if request.POST:
        email = request.POST['email']
        print("Post Request: ",email)
        if email =="":
            email_error = "Please enter a valid email address"
    context = {"email_error": email_error}
    return render(request, 'subscribe/subscribe.html', context)