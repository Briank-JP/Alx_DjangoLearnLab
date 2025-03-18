from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout

# Create your views here.
class RegisterVeiw(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name ='blog/register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)