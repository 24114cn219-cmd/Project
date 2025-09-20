from django.shortcuts import render, redirect
from django.http import HttpResponse
from sihapp.models import Great, Candidate, Internship
from datetime import datetime
from django.contrib import messages
from sihapp.matching import match_candidates  # keep this


def index(request):
    return render(request, "index.html")

def matches(request):
    return render(request, "matches.html")

def about(request):
    return render(request, "about.html")

def registration(request):
    return render(request, "registration.html") 
        
def features(request):
    return render(request, "features.html")

def contact(request):
    return render(request, "contact.html")

def internship(request):
    return render(request, "internship.html")

def quicklinks(request):
    return render(request, "quicklinks.html")

def great(request):
    if request.method == "POST":
        role = request.POST.get("role")  # student / company / admin
        full_name = request.POST.get("full_name")
        company_name = request.POST.get("company_name")
        email = request.POST.get("email")
        mobile_number = request.POST.get("mobile_number")
        password = request.POST.get("password")
        skills = request.POST.get("skills")
        internship_location = request.POST.get("internship_location")
        resume = request.FILES.get("resume")
        website = request.POST.get("website")
        location = request.POST.get("location")
        number_of_interns_required = request.POST.get("number_of_interns_required")

        if Great.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('great')  # Make sure your URL name is 'great'

        # Save in Great table
        Great.objects.create(
            role=role,
            full_name=full_name if role in ["student","admin"] else None,
            company_name=company_name if role=="company" else None,
            email=email,
            mobile_number=mobile_number,
            password=password,
            skills=skills,
            internship_location=internship_location,
            resume=resume,
            website=website,
            number_of_interns_required=number_of_interns_required if number_of_interns_required else None,
            date=datetime.today()
        )

        # Save in AI-specific tables
        if role == "student":
            Candidate.objects.create(
                name=full_name,
                email=email,
                skills=skills,
                internship_location=internship_location,
                resume=resume,
                past_participation=0
            )
        elif role == "company":
            Internship.objects.create(
                title=f"{company_name} Internship",
                company_name=company_name,
                skills_required=skills,
                location=internship_location,  # ✅ guaranteed not null
                capacity=int(number_of_interns_required) if number_of_interns_required else 1
            )

    return render(request,"great.html")

def show_matches(request):
    matches = match_candidates()  # ✅ this now calls your AI-based scoring
    return render(request, "matches.html", {'matches': matches})



