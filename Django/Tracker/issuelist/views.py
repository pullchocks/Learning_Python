from django.shortcuts import render
from issuetracker.models import Issue

def home(request):
    issues = Issue.objects.all()  # Retrieve all issues
    return render(request, 'issuelist/home.html', {'issues': issues})
