from django.shortcuts import render, HttpResponse
from .models import Profile, About, ContactInfo, Project, Education, Skill, TechStack, Experience


# Create your views here.
def home(request):
    profile = Profile.load()
    contactInfo = ContactInfo.load()
    projects = Project.objects.all()
    techStacks = TechStack.objects.all()
    experiences = Experience.objects.all()

    return render(request, "home-v2.html", {
        'profile': profile,
        'projects': projects,
        'contactInfo': contactInfo,
        'techStacks': techStacks,
        'experiences': experiences,
    })

def about(request):
    about = About.load()
    contactInfo = ContactInfo.load()
    skills = Skill.objects.all()
    education = Education.objects.all()
    return render(request, "about-v2.html", {
        'about': about,
        'skills': skills,
        'contactInfo': contactInfo,
        'education': education
    })

def contact(request):
    contactInfo = ContactInfo.load()
    return render(request, "contact-v2.html",  {
        'contactInfo': contactInfo,
    })

