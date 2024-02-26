from django.views.generic import ListView, DetailView
from issuetracker.models import Issue

class IssueListView(ListView):
    model = Issue
    template_name = 'issues/issue_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)  # This line is for debugging purposes. You can remove it later.
        return queryset

class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
