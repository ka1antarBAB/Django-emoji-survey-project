from django.views import generic
from django.urls import reverse_lazy

from . import forms


# Create your views here.

class SignupView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
