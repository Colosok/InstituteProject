from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import MyUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'password1', 'password2']
