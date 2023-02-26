from django.shortcuts import render, redirect
from.forms import ContactUsForm, Ask_logement
#from . import encore.csv 
import pandas as pd
from urllib.parse import urlencode
import csv


# dof=pd.read_csv("encore.csv")



def home (request):
    return render (request, 'immo_prix/home.html')




from django.core.mail import send_mail
...

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],     #  form.cleaned_data :un dict //contient données du formulaire qd il a subi process de validation
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            message=form.cleaned_data['message']
            return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            "immo_prix/contact.html",
            {'form': form, 'msg':message})

def estimer(request):
    if request.method == 'POST':
        file = pd.read_csv("static/encore.csv")
        form = Ask_logement(request.POST)

        if form.is_valid():
            
            code_postal=form.cleaned_data['code_postal'],     #  form.cleaned_data :un dict //contient données du formulaire qd il a subi process de validation
            vue_sur_mer=form.cleaned_data['vue_sur_mer'],
            vue=form.cleaned_data['vue'],
            surface_habitable=form.cleaned_data['surface_habitable'],
            surface_terrain=form.cleaned_data['surface_terrain'],
            surface_terrain_15=form.cleaned_data['surface_terrain_15'],
            salle_de_bain=form.cleaned_data['salle_de_bain'],
            notation=form.cleaned_data['notation'],
            
    
            infos= {'code_postal':code_postal, 'vue_sur_mer':vue_sur_mer, 'vue':vue, 'surface_habitable':surface_habitable, 'surface_terrain':surface_terrain,'surface_terrain_15':surface_terrain_15,'salle_de_bain':salle_de_bain,'notation':notation}
            return redirect('rslt_estimation' + infos)


    return render (request, 'immo_prix/estimer.html')

def rslt_estimation (request):
    return render (request, 'rslt_estimation.html')
# def contact(request):

#   # add these print statements so we can take a look at `request.method` and `request.POST`
#   print('The request method is:', request.method)
#   print('The POST data is:', request.POST)

# #   form = ContactUsForm()
 # return render (request, "immo_prix/contact.html")

# def contact(request):                                                    #si c'est une requête GET (= champs pas remplis/ pas de bouton d'envoi>>affiche formu vierge
#   form = ContactUsForm()  # ajout d’un nouveau formulaire ici            #si c'est une requête "post"= formu est rempli + bouton envoyer >>> voi que c'est une requête post!!
#   print('The request method is:', request.method)
#   print('The POST data is:', request.POST)
  
  
#   return render(request,
#           "immo_prix/contact.html",
#           {'form': form})



