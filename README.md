###################################
###################################
##                               ##
##     Projet Trophées NSI       ##
##                               ##
##    Rudolf - Vieira Do Vale    ##
##                               ##
###################################
###################################

PyCareFinder
L'utilisateur renseigne ses coordonnées sur une fenêtre tkinter ainsi que les établissements de soins qu'il désire trouver.
La page HTML renvoie des informations liées aux étabissements de soins renseignés.

A ce stade, le projet est considéré comme terminé mais des modifications peuvent être apporter :
    • créer une application pour téléphone
    • rendre la page HTML responsive (en lien avec l’exécution du programme python sur téléphone)
    • améliorer le design de la fenêtre tkinter et de la page HTML
    • mettre un rayon minimal dans lequel il faut être (en France) sans quoi le programme prévient l’utilisateur qu’il n’est pas en France (incluant les outre-mers)
    • récupérer la localisation à partir de l'IP afin de faire une saisie automatique des coordonnées
    • cibler une pathologie 
    • possibilité de contacter l’établissement de soin directement : on appuie sur un bouton qui ouvre le clavier téléphone avec le numéro
    • interroger directement la base de données pour permettre à l’utilisateur d’accéder à des données actuelles sans avoir à télécharger les fichiers csv sur son ordinateur

Projet développé en Python 3.7.6 : différentes bibliothèques utilisées :
    • os
    • math
    • folium
    • tkinter
    • webbrowser
    • PIL
Après de nombreux tests, le fichier requirements.txt contient : folium pillow
les autres bibliothèques sont normalement déjà présentes.

Une instruction pour l’installation et l’utilisation.

Une liste des technologies utilisées et, le cas échéant, des liens vers d’autres informations sur ces technologies.

Bugs connus et corrections éventuelles apportées.

Licence libre : GPL v3+