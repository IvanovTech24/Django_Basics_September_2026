from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=50,
    )
    text = models.TextField()

    is_completed = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.title} - {self.text} - is completed: {self.is_completed}"
