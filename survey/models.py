from django.db import models


# Create your models here.
class EmojiFeedback(models.Model):
    EMOJI_CHOICES = [
        ('Happy', '😃'),
        ('Neutral', '😐'),
        ('Sad', '😞'),
        ('Love', '😍'),
        ('Angry', '😡'),
    ]

    emoji = models.CharField(max_length=10, choices=EMOJI_CHOICES)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.emoji} - {self.count}'
