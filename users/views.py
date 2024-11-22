from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView
from . import forms, models, middlewares


class RgistrationsView(CreateView):
    from_class = forms.CustomRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        age = form.cleaned_data('age')
        if age < 5:
            self.object.club = 'Извените вы слишком молоды'
        elif 5 <= age <= 10:
            self.object.club = 'Детский клуб'
        elif 11 <= age <= 18:
            self.object.club = 'Подростковый клуб'
        elif 19 <= age <= 45:
            self.object.club = 'Взрослый клуб'
        else:
            self.object.club = 'Клуб не определен'
        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'users/user_list.html'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
