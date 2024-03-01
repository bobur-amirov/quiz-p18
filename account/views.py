from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from .forms import SignUpForm

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = '/'
