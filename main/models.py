from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5