# prediction_prix_maison_ML
Ce projet est basé sur un dataset de 21 162 données portant sur les ventes de maisons dans le comté de King dans l'État de Washington aux États-Unis entre 2014 et 2015.

Objectifs

L'objectif principal de ce projet est de développer un algorithme de machine learning performant à partir du coefficient de détermination r2 pour aider les utilisateurs à faire une estimation de prix sur leur logement. Pour atteindre cet objectif, nous avons étudié les corrélations entre chaque variable et le prix.

Algorithme choisi

Après avoir étudié les différentes possibilités, nous avons choisi l'algorithme KNNRegressor qui permet de se baser sur un nombre de voisins issus du dataset ayant les caractéristiques les plus proches. Nous avons constaté que l'utilisation de cet algorithme permettait d'obtenir le meilleur score de "prédiction" en fonction du coefficient de détermination r2 et d'une metrique "distance" qui pondére le poids des voisins selon leur distance avec les critères définis.
  
  
Utilisation du questionnaire

Le dataset portait sur des prix en dollards et une mesure de surface en pieds carré, nous avons converti le modéle d'estimation afin qu'un utilisateur  européen puisse avoir une estimation de prix en euros et une mesure de surface en metre carré.

Implémentation

Nous avons implémenté l'algorithme KNNRegressor via pickle dans Django, afin de créer un site web qui permet d'estimer le prix d'un logement à partir de 7 variables que les utilisateurs complètent sur la page d'estimation du site.

Conclusion

Ce projet a permis de développer un algorithme de machine learning performant pour aider les utilisateurs à estimer le prix de leur logement. Le site web développé offre une interface pour saisir les données nécessaires à l'estimation, ainsi qu'une page qui leur offre la possibilité d'accéder à leurs anciennes estimations de logement.
Nous espérons que ce projet sera utile aux utilisateurs qui cherchent à estimer le prix de leur logement dans le comté de King, dans l'État de Washington.
