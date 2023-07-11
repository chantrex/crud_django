from django.shortcuts import render


# Index view
def index(request):
    return render(request, "polls/index.html")

# Registration view
def registration(request):
    return render(request, "polls/registration.html")
