from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ### pr "if request method == POST
    # 
    # une vue: l'endroit ou l'utilisateur envoei des requetes http au serveur (eemple cliquer lien ou envoie formulaie
    # cf= method= submit!>>> post)
    # >>> celui ci (le serveur)verifie si c'est une methode get  (recuperation de données) ou autre 5POST, DEL etc)
    #rappel: POST: pour envoyer des données au serveur!
    # 
    
    # request.method >> dde au serveur quelle méthode a été utilisée pour envoyer une vue/// détermine quelle méthode a été faite pr faire la requête serveur!
    # ou une méthode "POST" >>> pour alimenter en données"
    
    #  if request.method == 'POST': >>> vérifie qu'on est en face d'une requête post!