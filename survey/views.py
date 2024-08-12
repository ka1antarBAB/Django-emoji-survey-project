from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from survey.forms import EmojiSurveyForm
from .models import EmojiFeedback


# Create your views here.

def emoji_survey_view(request):
    if request.method == 'POST':
        form = EmojiSurveyForm(request.POST)
        if form.is_valid():
            selected_emoji = form.cleaned_data['emoji']
            feedback, created = EmojiFeedback.objects.get_or_create(emoji=selected_emoji)
            feedback.count += 1
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
    if request.method == 'GET':
        form = EmojiSurveyForm()

    return render(request, 'emoji_survey.html', {'form': form})


@staff_member_required
def survey_results_view(request):
    feedbacks = EmojiFeedback.objects.all()
    return render(request, 'survey_results.html', {'feedbacks': feedbacks})
