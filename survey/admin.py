from django.contrib import admin
from .models import Survey


@admin.register(Survey)
class EmojiFeedbackAdmin(admin.ModelAdmin):
    list_display = ('emoji_display', 'count',)

    def emoji_display(self, obj):
        emoji_text_map = {
            'Love': 'خیلی خوب - 😍',
            'Happy': 'خوب - 😃',
            'Neutral': 'خنثی - 😐',
            'Sad': 'بد - 😞',
            'Angry': 'خیلی بد - 😡',
        }
        return emoji_text_map.get(obj.emoji, obj.emoji)

    emoji_display.short_description = 'Emoji and Text'
