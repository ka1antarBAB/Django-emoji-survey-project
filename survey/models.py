from django.db import models


class Survey(models.Model):
    EMOJI_CHOICES = [
        ('Angry', '😡'),
        ('Sad', '😞'),
        ('Neutral', '😐'),
        ('Happy', '😃'),
        ('Love', '😍'),
    ]
    emoji = models.CharField(max_length=10, choices=EMOJI_CHOICES)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.emoji} - {self.count}'
