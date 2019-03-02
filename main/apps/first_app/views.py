from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "first_app/index.html", context)
    
