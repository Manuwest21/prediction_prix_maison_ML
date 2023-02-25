from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
)
    # profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    account_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    username = None                          #précise qu'on en veut pas!
    profile_photo = models.ImageField()        #la photo de profil sera votre maison/apptmt: sous l'angle que vou souhaitez!

    EMAIL_FIELD ='email'                     # contient l'adresse mail ppal de l'utilisateur
    USERNAME_FIELD = 'account_number'                 # on précise quel champ va remplir le champ pr s'identifier  (peut être date de naissance ou autre) 
    #REQUIRED_FIELDS =                      sont les champs à préciser lors de l'use de la commande : python manage.py createsuperuser
