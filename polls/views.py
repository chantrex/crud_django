from django.shortcuts import render
from .models import Guest

# Index view
def index(request):
    return render(request, "polls/index.html")

# Registration view
def registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstnameHtml']
        lastname = request.POST['lastnameHtml']
        grade = request.POST['gradeHtml']
        email = request.POST['emailHtml']

        guest = Guest(firstname=firstname, lastname=lastname, grade=grade, email=email)
        guest.save()
        print(f'\n------- DataBase Successfully Registered -------\n')
        print(f'Firstname: {firstname}')
        print(f'Lastname: {lastname}')
        print(f'Grade: {grade}')
        print(f'Email: {email}')

        #return render(request, 'success.html')  # Redirect to a success page after saving
        return render(request, "polls/registration.html")
    return render(request, "polls/index.html")

