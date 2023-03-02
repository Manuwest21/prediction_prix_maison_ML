from django.shortcuts import render, redirect
from.forms import ContactUsForm, Ask_logement
#from . import encore.csv 
import pandas as pd
from urllib.parse import urlencode
import pickle
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.storage import staticfiles_storage
# dof=pd.read_csv("encore.csv")
# import joblib
from django.views import View
import joblib
from joblib import load
import pickle
import os
from .models import Champs
# model=load('./models/modeli.pkl')
# model=pickle.load(open('/home/apprenant/Documents/estimation_projet/prediction_prix_maison_ML/estimation/immo_prix/models/modeli.pkl', 'rb'))
 


with open ('immo_prix/final.pkl','rb') as file:
     model=pickle.load(file)


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
    # ceci doit être une requête POST, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request,
            "immo_prix/contact.html",
            {'form': form, 'msg':message})

def estimer(request):
    
    if request.method == 'POST':
        form = Ask_logement(request.POST)
        # file = pd.read_csv("static/encore.csv")
        # form = Ask_logement(request.POST)

        if form.is_valid():
            hugo=form.save(commit=False)
            code_postal=form.cleaned_data['code_postal'],     #  form.cleaned_data :un dict //contient données du formulaire qd il a subi process de validation
            vue_sur_mer=form.cleaned_data['vue_sur_mer'],
            vue=form.cleaned_data['vue'],
            surface_habitable=form.cleaned_data['surface_habitable'],
            surface_terrain=form.cleaned_data['surface_terrain'],
            surface_terrain_15=form.cleaned_data['surface_terrain_15'],
            salle_de_bain=form.cleaned_data['salle_de_bain'],
            notation=form.cleaned_data['notation'],
            url = staticfiles_storage.url('immo_prix/encore.csv')

            infos= {'code_postal':code_postal, 'vue_sur_mer':vue_sur_mer, 'vue':vue, 'surface_habitable':surface_habitable, 'surface_terrain':surface_terrain,'surface_terrain_15':surface_terrain_15,'salle_de_bain':salle_de_bain,'notation':notation}
            form.save()
            return redirect('rslt_estimation')#+ infos)
    else:
        form = Ask_logement()
        infos='x'
        #infos='x'


    return render (request, 'immo_prix/estimer.html', {'form':form, 'infos':infos})#, "infos":infos})


    # file_path = staticfiles_storage.path('encore.csv')
    # with open(file_path, 'r') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    # for row in reader:
        # print(row)
# class ResultView(View):
#     def POST(self, request):
        
# def estimer(request):
    
#     if request.method == 'POST':
#         form = Ask_logement(request.POST)
#         # file = pd.read_csv("static/encore.csv")
#         # form = Ask_logement(request.POST)

#         if form.is_valid():
#             # hugo=form.save(commit=False)
#             # code_postal=form.cleaned_data['code_postal'],     #  form.cleaned_data :un dict //contient données du formulaire qd il a subi process de validation
#             # vue_sur_mer=form.cleaned_data['vue_sur_mer'],
#             # vue=form.cleaned_data['vue'],
#             # surface_habitable=form.cleaned_data['surface_habitable'],
#             # surface_terrain=form.cleaned_data['surface_terrain'],
#             # surface_terrain_15=form.cleaned_data['surface_terrain_15'],
#             # salle_de_bain=form.cleaned_data['salle_de_bain'],
#             # notation=form.cleaned_data['notation'],
#             # url = staticfiles_storage.url('immo_prix/encore.csv')
#             data= form.cleaned_data
#             df= pd.DataFrame(data,index=[0])
#             #infos= {'code_postal':code_postal, 'vue_sur_mer':vue_sur_mer, 'vue':vue, 'surface_habitable':surface_habitable, 'surface_terrain':surface_terrain,'surface_terrain_15':surface_terrain_15,'salle_de_bain':salle_de_bain,'notation':notation}
#             form.save()
#             #return redirect('rslt_estimation')#+ infos)
#         with open ('predict/models/model.pkl', 'rb') as f:
#             print(f)
#             knn_model= joblib.load(f)
#             prediction=knn_model.predict(df)
#         context= {
#             'prediction': round (prediction[0], 2)
            
#         }
#         return render (request, 'rslt_estimation.html', context)
#     else:
#         form = Ask_logement()
#         #infos='x'


#      return render (request, 'immo_prix/estimer.html', {'form':form})#, "infos":infos})


# def rslt_estimation (request,infos):
#     df=pd.Dataframe.from_dict(infos)
#     username=request.POST['code_postal']
#     #pickled_model=pickle.load(open('modeli.pkl', 'rb'))
#     #rslt=pickled_model.predict([[infos['code_postal'],infos['vue'],infos['vue_sur_mer'],infos['surface_habitable'],infos['surface_terrain'],infos['surface_terrain15'],infos['salle_de_bain'],infos['notation']]])
#     return render (request, 'immo_prix/rslt_estimation.html', {'rslt':username})


def questionnaire (request):
    
    
    return render (request, 'immo_prix/questionnaire.html')
    
def infos_form(request):
    form=Ask_logement(request.POST)
    form.save(commit=False)
    zipcode = int(request.POST['code_postal'])
    view = int(request.POST['vue'])
    waterfront =int( request.POST['vue_sur_mer'])
    surface = int(request.POST['surface_habitable'])
    surface_15 = int(request.POST['surface_terrain_15'])
    grade = int(request.POST['notation'])
    bathrooms = int(request.POST['salle_de_bain'])
    # id= int(request.POST[
    objet=form.save()
    id= objet.id
    data = {'zipcode': [zipcode],
        'view': [view],
        'waterfront': [waterfront],
        'surface': [surface],
        'surface_15': [surface_15],
        'grade': [grade],
        'bathrooms': [bathrooms]}
    # with open('chemin/vers/fichier.pickle', 'rb') as f:
    #         mon_objet = pickle.load(f) 
    # with open(model, "rb") as f:
    #     modeli = pickle.load(f)
    # print (data)
    # bathrooms","surface", "surface_15","zipcode","grade","waterfront","view"
    # data_2=[[bathrooms,surface, surface_15,zipcode,grade,waterfront,view]]
        # bathrooms","surface", "surface_15","zipcode","grade","waterfront","view"
        
    df = pd.DataFrame(data, index=[0])
    
    
    with open ('immo_prix/modelok.pkl','rb') as file:
        model=pickle.load(file)
    
    y_pred=model.predict(df)
    y_predi=y_pred.round()
    y_pred = int(y_pred[0])
    y_pred_str = str(y_pred).replace('[','').replace(']','').replace('.','')
    
    cham = Champs.objects.get(id=id)
    cham.estimation_prix=y_pred
    cham.save()
    
    # print(y_pred)
    return render (request, 'immo_prix/infos_form.html', {'rslt':y_predi})


def rslt_estimation (request):
    
    rslt= Champs.objects.all()
    
    
    return render (request, 'immo_prix/rslt_estimation.html', {'rslt':rslt})
 
        # nom = request.POST('username')
        # email = request.POST.POST('email')
    # username=request.POST['code_postal']
    #pickled_model=pickle.load(open('modeli.pkl', 'rb'))
    #rslt=pickled_model.predict([[infos['code_postal'],infos['vue'],infos['vue_sur_mer'],infos['surface_habitable'],infos['surface_terrain'],infos['surface_terrain15'],infos['salle_de_bain'],infos['notation']]])
  
#   else: 
#       nom='rien'
        #return render (request, 'immo_prix/rslt_estimation.html', {'rslt':rslt})
# def contact(request):

#   # add these print statements so we can take a look at `request.method` and `request.POST`
#   print('The request method is:', request.method)
#   print('The POST data is:', request.POST)

# #   form = ContactUsForm()
 # return render (request, "immo_prix/contact.html")

# def contact(request):                                                    #si c'est une requête POST (= champs pas remplis/ pas de bouton d'envoi>>affiche formu vierge
#   form = ContactUsForm()  # ajout d’un nouveau formulaire ici            #si c'est une requête "post"= formu est rempli + bouton envoyer >>> voi que c'est une requête post!!
#   print('The request method is:', request.method)
#   print('The POST data is:', request.POST)
  
  
#   return render(request,
#           "immo_prix/contact.html",
#           {'form': form})



class HomeView(View):
    def POST(self, request):
        username=request.POST['username']
        return render(request, 'home.html')

class HomeView(View):
    def POST(self, request):
        username=request.POST['username']
        return render(request, 'home.html')
# class PredictView(View):
#     def post(self, request):
#         # code pour réaliser la prédiction
#         # ...
#         return render(request, 'result.html', {'prediction': prediction})




class ResultView(View):
    def POST(self, request):
        return render(request, 'rslt_estimation.html')
    def post(self,request):
        if request.method == 'POST':
            form = Ask_logement(request.POST)
            # Récupérer les données du formulaire
            if form.is_valid():
                # zipcode = form.cleaned_data['zipcode']
                # view = form.cleaned_data['view']
                # grade = form.cleaned_data['grade']
                # sqft_living = form.cleaned_data['sqft_living']
                # bathrooms = form.cleaned_data['bathrooms']
                # waterfront = form.cleaned_data['waterfront']
                # sqft_above = form.cleaned_data['sqft_above']
                # sqft_basement = form.cleaned_data['sqft_basement']
                # sqft_living15 = form.cleaned_data['sqft_living15']
                # days_since_reference_date = form.cleaned_data['days_since_reference_date']
                data = form.cleaned_data
                df = pd.DataFrame(data,index=[0])

                print(df)
            # Charger le modèle KNN entraîné
            with open('immo_prix/models/model.pkl', 'rb') as f:
                print(f)
                knn_model = joblib.load(f)
                prediction = knn_model.predict(df)
            context = {
                'prediction': round(prediction[0], 2)
            }
            return render(request, 'rslt_estimation.html', context)

        else:
            form = Ask_logement()
            return render(request, 'estimer.html')