from django.shortcuts import render
from django.core.mail import send_mail
from .models import Skill, Project, Contact

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    success = False

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        send_mail(
            subject=f"Portfolio Message from {name}",
            message=message,
            from_email=email,
            recipient_list=['YOUR_EMAIL@gmail.com'],
            fail_silently=False,
        )

        success = True

    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
        'success': success
    })
