<h1>Projet Trophées NSI</h1>
<br>
<h1>Rudolf - Vieira Do Vale</h1>
<br>
<br>
ATTENTION : dans le dossier data, un fichier t-finess.csv est censé être présent, pour des raisons de tailles volumineuses, le fichier peut être téléchargé ici : https://www.data.gouv.fr/fr/datasets/referentiel-finess-t-finess/<br>
Pour des raisons de bon fonctionnement vous êtes priés d'utiliser la version mise à jour le 17 janvier 2025. Si vous souhaitez avoir cette version (si elle n'est plus disponible à l'avenir) demandez sur GitHub (github.com/maulyo/pycarefinder), par exemple!<br>
<br>
Pour lancer le programme : il faut lancer main.py présent dans le dossier sources.<br>
<br>
PyCareFinder<br>
L'utilisateur renseigne ses coordonnées sur une fenêtre tkinter ainsi que les établissements de soins qu'il désire trouver.<br>
La page HTML renvoie des informations liées aux étabissements de soins renseignés.<br>
<br>
A ce stade, le projet est considéré comme terminé mais des modifications peuvent être apportées :<br>
    • créer une application pour téléphone<br>
    • rendre la page HTML responsive (en lien avec l’exécution du programme python sur téléphone)<br>
    • améliorer le design de la fenêtre tkinter et de la page HTML<br>
    • mettre un rayon minimal dans lequel il faut être (en France) sans quoi le programme prévient l’utilisateur qu’il n’est pas en France (incluant les outre-mers)<br>
    • récupérer la localisation à partir de l'IP afin de faire une saisie automatique des coordonnées<br>
    • cibler une pathologie pour les CHU / CH (en plus des services déjà possibles)<br>
    • possibilité de contacter l’établissement de soin directement : on appuie sur un bouton qui ouvre le clavier téléphone avec le numéro<br>
    • interroger directement la base de données pour permettre à l’utilisateur d’accéder à des données actuelles sans avoir à télécharger les fichiers csv sur son ordinateur<br>
<br><br>
Projet développé en Python 3.7.6 : différentes bibliothèques utilisées :<br>
    • os<br>
    • math<br>
    • folium<br>
    • tkinter<br>
    • webbrowser<br>
    • PIL<br>
Après de nombreux tests, le fichier requirements.txt contient : folium pillow<br>
les autres bibliothèques sont normalement déjà présentes dans la version python.<br>
<br>
Pour l'utilisation : respectez l'architecture présente (data, docs, sources) telle qu'elle est présente entre vos mains. Respectez les bons noms de fichiers et placez t-finess2.csv (version du 17 janvier 2025) dans le dossier data.<br>
<br>
Aucun bug actuellement connu.<br>
<br>
Licence libre : GPL v3+
<br>
