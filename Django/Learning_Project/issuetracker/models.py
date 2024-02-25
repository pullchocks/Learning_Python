from django.db import models
from django.conf import settings

ISSUE_STATUS_CHOICES = (
    ('new', 'New'),
    ('accepted', 'Accepted'),
    ('reviewed', 'Reviewed'),
    ('started', 'Started'),
    ('closed', 'Closed'),
)

class Issue(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=25, choices=ISSUE_STATUS_CHOICES, default='new')
    summary = models.TextField()
    opened_on = models.DateTimeField('date opened', auto_now_add=True)
    modified_on = models.DateTimeField('date modified', auto_now=True)

    def name(self):
        return self.summary.split('\n', 1)[0]
