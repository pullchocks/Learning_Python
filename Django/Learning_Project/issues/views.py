from django.views.generic import ListView, DetailView
from issuetracker.models import Issue  # Importing the Issue model from issuetracker

class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)  # Print the queryset to the console
        return queryset
