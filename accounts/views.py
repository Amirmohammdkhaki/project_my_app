from django.shortcuts import render
from django.views .generic import CreateView
from .forms import CustomUserChangeForm , CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpview(CreateView):
    form_class=CustomUserCreationForm
    template_name='registration/signup.html'
    success_url=reverse_lazy('login')