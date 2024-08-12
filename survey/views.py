from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from survey.forms import EmojiSurveyForm
from .models import Survey


# Create your views here.

def emoji_survey_view(request):
    if request.method == 'POST':
        form = EmojiSurveyForm(request.POST)
        if form.is_valid():
            selected_emoji = form.cleaned_data['emoji']
            feedback, created = Survey.objects.get_or_create(emoji=selected_emoji)
            feedback.count += 1
            feedback.save()
            messages.success(request, ' !نظر شما با موفقیت ثبت شد ')
    if request.method == 'GET':
        form = EmojiSurveyForm()

    return render(request, 'emoji_survey.html', {'form': form})


@staff_member_required
def survey_results_view(request):
    feedbacks = Survey.objects.all()
    return render(request, 'survey_results.html', {'feedbacks': feedbacks})
