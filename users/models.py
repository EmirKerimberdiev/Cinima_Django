from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=15, default='+996')
    age = models.PositiveIntegerField(default=8)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    club = models.CharField(max_length=50, default='Клуб не определен')


@receiver(post_save, sender=CustomUser)
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




