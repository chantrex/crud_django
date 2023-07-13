from django.shortcuts import render
from .models import Guest

# Index view
def index(request):
    return render(request, "polls/index.html")

# Registration view
def registration(request):
    success = 'Guest Added SUCCESSFULLY!'

    # Validation if the form is submitted with POST method
    if request.method == 'POST':
        firstname = request.POST['firstnameHtml']
        lastname = request.POST['lastnameHtml']
        grade = request.POST['gradeHtml']
        email = request.POST['emailHtml']

        # Registering a new data in the DB
        guest = Guest(firstname=firstname, lastname=lastname, grade=grade, email=email)
        guest.save()
        print(f'\n------- DataBase Successfully Registered -------\n')
        print(f'Firstname: {firstname}')
        print(f'Lastname: {lastname}')
        print(f'Grade: {grade}')
        print(f'Email: {email}')

        context = {
            'success': success,
        }

        #return render(request, 'success.html')  # Redirect to a success page after saving
        return render(request, "polls/index.html", context)
    return render(request, "polls/registration.html")

