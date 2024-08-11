from django import forms
from .models import EmojiFeedback


class EmojiSurveyForm(forms.Form):
    emoji = forms.ChoiceField(choices=EmojiFeedback.EMOJI_CHOICES, widget=forms.RadioSelect)
