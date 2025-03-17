from django.shortcuts import render, HttpResponse
from .models import Profile, About, ContactInfo, Project, Education, Skill


# Create your views here.
def home(request):
    profile = Profile.load()
    projects = Project.objects.all()
    return render(request, "home-v2.html", {
        'profile': profile,
        'projects': projects,
    })

def about(request):
    return render(request, "about-v2.html")

def contact(request):
    return render(request, "contact.html")

