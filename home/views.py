from django.shortcuts import render, HttpResponse, redirect
from .models import Profile, About, ContactInfo, Project, Education, Skill, TechStack, Experience
from .forms import ContactForm
from django.contrib import messages


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
    if request.method == 'POST':
        # If the form is being submitted
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid data to the database

            # Add a success message
            messages.success(request, 'Got it! I’ll get back to you soon — appreciate you reaching out.')

            # Redirect to the same page to prevent re-submission on refresh
            return redirect('contact')
    else:
        # If it's a GET request, just display a blank form
        form = ContactForm()
    contactInfo = ContactInfo.load()

    return render(request, "contact-v2.html", {
        'form': form,
        'contactInfo': contactInfo,
    })
