from django.db import models

class Backlog(models.Model):
    name = models.TextField()

class Issue(models.Model):
    label = models.TextField()
    description = models.TextField()

    issue_type = models.TextField()

    backlog = models.ForeignKey(Backlog, on_delete=models.CASCADE)
