from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username', 'email', 'phone_number', 'age', 'gender', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_club(sender, instance, created, **kwargs):
    print("User created")
    age = instance.age
    if age < 5:
        instance.club = 'Вы слишком малы для этого клуба'
    elif age >= 5 and age <= 10:
        instance.club = 'Детский клуб'
    elif age >= 11 and age <= 18:
        instance.club = 'Подростковый клуб'
    elif age >= 19 and age <= 45:
        instance.club = 'Взрослый клуб'
    else:
        instance.club = 'Ваш возраст состовляет больше 45 лет'
    instance.save()
