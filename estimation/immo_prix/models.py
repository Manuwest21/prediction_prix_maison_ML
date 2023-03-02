from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
vue= (
        
   ( 1, 'pas de vue particulière'),
     
        (2, 'vue passable'),
        (3, 'belle vue'),
        (4, 'trés belle vue'))


vue_mer= (
        
        (0, 'pas de vue sur mer'),
     
        (1, 'vue sur mer'))



postal_choix = (
        
        (98178, '98178'),
     
        (98125, '98125'),
        (98028, '98028'),
        (98136, '98136'),
       ( 98074, '98074'),
        (98053, '98053'),
        (98003, '98003'),
        (98198, '98198'),
        (98146, '98146'),
        
        (98038, '98038'),
        (98007, '98007'),
        (98115, '98115'),
        (98107, '98107'),
        (98126, '98126'),
        (98019, '98019'),
        (98103, '98103'),
        (98002, '98002'),
        (98133, '98133'),
        
        (98040, '98040'),
        (98092, '98092'),
        (98030, '98030'),
        (98119, '98119'),
        (98112, '98112'),
        (98052, '98052'),
        (98027, '98027'),
       ( 98117, '98117'),
       (98058, '98058'),
        
        (98001, '98001'),
        (98056, '98056'),
        (98166, '98166'),
       (98023, '98023'),
        (98070, '98070'),
        (98148, '98148'),
        (98105, '98105'),
        (98042, '98042'),
        (98008, '98008'),
        
        (98059, '98059'),
        (98122, '98122'),
        (98144, '98144'),
        (98004, '98004'),
        (98005, '98005'),
        (98034, '98034'),
        (98075, '98075'),
        (98116, '98116'),
        (98010, '98010'),
        
        (98118, '98118'), 
        (98199, '98199'),
        (98032, '98032'),
        (98045, '98045'),
        (98102, '98102'),
        (98077, '98077'),
        (98108, '98108'),
        (98168, '98168'),
        (98177, '98177'),
        (98065, '98065'),
        (98029, '98029'),
        (98006, '98066'),
        (98109, '98109'),
        (98022, '98022'),
        (98033, '98033'),
        (98155, '98155'),
        (98024, '98024'),
        (98011, '98011'),
        (98031, '98031'),
        (98106, '98106'),
        (98072, '98072'),
        (98188, '98188'),
        (98014, '98014'),
        (98055, '98055'),
        (98039, '98039'))
        
class Formu(models.Model):
    # client = models.ForeignKey(max_length=100,
    #     on_delete=models.CASCADE,
    #     null=True)
    title = models.CharField(max_length=100)
    tit = models.CharField(max_length=100)
    content = models.TextField(default='Notes client:')
    creation_date = models.DateTimeField(auto_now_add=True)
    
    
class Champs(models.Model):
   code_postal = models.IntegerField(choices=postal_choix)
   vue_sur_mer= models.IntegerField(choices=vue_mer)
   vue =  models.IntegerField(choices=vue)
    #    validators=[MaxValueValidator(100),
            # MinValueValidator(1)
        
   surface_habitable = models.IntegerField(validators=[MaxValueValidator(5000),
            MinValueValidator(30)
        ])
   surface_terrain= models.IntegerField(validators=[MaxValueValidator(1000),
            MinValueValidator(1)
        ])
   surface_terrain_15 = models.IntegerField(validators=[MaxValueValidator(1000),
            MinValueValidator(10)
        ])
   salle_de_bain = models.IntegerField(validators=[MaxValueValidator(10),
            MinValueValidator(1)
        ])
   notation = models.IntegerField(validators=[MaxValueValidator(13),
            MinValueValidator(1)
        ])
   estimation_prix=models.IntegerField(validators=[MaxValueValidator(500000000),
            MinValueValidator(30)], blank=True, null=True)
        
   
   
   
#    surface_terrain= models.IntegerField(validators=validators=[
# required=false, min_value= 0 max_value=x st


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