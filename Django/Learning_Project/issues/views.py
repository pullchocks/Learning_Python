from django.views.generic import ListView, DetailView
from issuetracker.models import Issue  # Importing the Issue model from issuetracker

class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'  # Path to the template for listing issues

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'  # Path to the template for showing issue details
