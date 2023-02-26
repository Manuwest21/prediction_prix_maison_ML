from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

postal_choix = (
        (59200, '59200'),
        (59100, '59100'),
)

class Formu(models.Model):
    # client = models.ForeignKey(max_length=100,
    #     on_delete=models.CASCADE,
    #     null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='Notes client:')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    
class Champs(models.Model):
   code_postal = models.CharField(max_length=100,choices=postal_choix)
   vue_sur_mer= models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)
        ])
   vue = models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)
        ])
   surface_habitable = models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)
        ])
   surface_terrain= models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)
        ])
   surface_terrain_15 = models.IntegerField(validators=[MaxValueValidator(100),
            MinValueValidator(1)
        ])
   salle_de_bain = models.URLField()
   notation = models.IntegerField(validators=[MaxValueValidator(13),
            MinValueValidator(1)
        ])
#    surface_terrain= models.IntegerField(validators=validators=[
          


#models.URLField(required=False)
# class Band(models.Model):

#     class Genre(models.TextChoices):
#         HIP_HOP = 'HH'
#         SYNTH_POP = 'SP'
#         ALTERNATIVE_ROCK = 'AR'

#     ...
#     genre = models.fields.CharField(choices=Genre.choices, max_length=5)
#    >>>> va fficher liste déroulantes des genres

# pr afficher ds admin, le champ "nom" de l'objet plutôt que "object_id"!

# class Band(models.Model):
#    …
#    def __str__(self):
#     return f'{self.name}'

# year_formed = models.fields.IntegerField(
#     validators=[MinValueValidator(1900),
#            MaxValueValidator(2021)]


#    if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la bdd
            #band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            #return redirect('band-detail', band.id)) >>> ds url y aura bandetail/<int:chiffre>/
            # = rediriger vers la page détaillée (et les champs choisis ds html ) du formu créé
