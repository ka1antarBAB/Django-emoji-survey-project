from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from core.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('email', 'username',)
