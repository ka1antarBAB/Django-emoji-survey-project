from django import forms
from .models import Survey


class SurveyForm(forms.Form):
    emoji = forms.ChoiceField(
        choices=Survey.EMOJI_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )


