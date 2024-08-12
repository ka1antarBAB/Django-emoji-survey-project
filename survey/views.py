from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from survey.forms import SurveyForm
from .models import Survey


def emoji_survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            selected_emoji = form.cleaned_data['emoji']
            survey, created = Survey.objects.get_or_create(emoji=selected_emoji)
            survey.count += 1
            survey.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد!')
            return redirect("survey:emoji_survey")
    else:
        form = SurveyForm()

    return render(request, 'emoji_survey.html', {'form': form})

