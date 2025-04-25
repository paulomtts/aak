from django.db import models
from django.contrib.auth.models import User


class Label(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "owner")  # Prevent duplicate labels per user

    def __str__(self):
        return f"Label(name={self.name}, owner_name={self.owner.username})"


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return f"Task(title={self.title}, description={self.description}, is_completed={self.is_completed}, owner_name={self.owner.username}, labels={self.labels})"
