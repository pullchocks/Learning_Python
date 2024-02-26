from django.urls import path
from .views import IssueListView, IssueDetailView

urlpatterns = [
    path('', IssueListView.as_view(), name='issue-list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),
]