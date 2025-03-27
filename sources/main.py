#Projet : PyCareFinder
#Auteurs : Raphaël Rudolf, Simon Vieira Do Vale

# Importation des bibliothèques

import os
import math
import folium
from tkinter import *
import webbrowser as WB
from PIL import Image, ImageTk

# # # Définitions des fonctions principales # # #

# Pour le programme de recherche

def calcul_dis(coordA, coordB):
    """ Fonction qui calcule et retourne la distance en km entre 2 points (A et B) :
        - A -> point n°1 -> type str
        - B -> point n°2 -> type str
        - distanceAB -> valeur retournée -> type float """
    virgule = False
    for caractere in coordA:
        if caractere == ',':
            virgule = True
    if virgule == True:
        coordA = coordA.rstrip(' ').split(',')
        coordB = coordB.strip(' ').split(',')
    else:
        coordA = coordA.rstrip(' ').lstrip(' ').split(' ')
        coordB = coordB.rstrip(' ').lstrip(' ').split(' ')


    latA = float(coordA[0])
    longA = float(coordA[1])
    latB = float(coordB[0])
    longB = float(coordB[1])

    latA = math.radians(latA)
    latB = math.radians(latB)
    longA = math.radians(longA)
    longB = math.radians(longB)

    dV = longB - longA
    AB = math.acos(math.sin(latA) * math.sin(latB) + math.cos(latA) * math.cos(latB) * math.cos(dV))
    distanceAB = 6378.752*AB

    return distanceAB

def distance_min(pointA, liste_data):
    """ Fonction qui cherche le point le plus proche du point A, en scrutant successivement chaque
        éléments de la liste_data
        la fonction retourne : - la distance min de type float
                               - l'index de liste_data du point le plus proche de type int """
    dis_min = calcul_dis(pointA, liste_data[0])
    index_point_carte_proche = 0
    for i in range(len(liste_data)):
        if calcul_dis(pointA, liste_data[i]) < dis_min:
            dis_min = calcul_dis(pointA, liste_data[i])
            index_point_carte_proche = i
    return dis_min, index_point_carte_proche

# Pour la fenêtre tkinter

# Création des fonctions
def aucunbtn():
    """on crée une fonction pour supprimer tout les autres cases cocher des ch buttons """
    if aucunvar.get() == 1 :
        esh_var.set(0)
        ash_var.set(0)
        pa_var.set(0)
        san_var.set(0)

def esh_btn():
    """on crée une fonction pour supprimer tout les autres cases cocher des ch buttons """
    if esh_var.get() == 1 :
        aucunvar.set(0)
        ash_var.set(0)
        pa_var.set(0)
        san_var.set(0)

def ash_btn():
    """on crée une fonction pour supprimer tout les autres cases cocher des ch buttons """
    if ash_var.get() == 1 :
        esh_var.set(0)
        aucunvar.set(0)
        pa_var.set(0)
        san_var.set(0)

def pa_btn():
    """on crée une fonction pour supprimer tout les autres cases cocher des ch buttons """
    if pa_var.get() == 1 :
        esh_var.set(0)
        ash_var.set(0)
        aucunvar.set(0)
        san_var.set(0)

def san_btn():
    """on crée une fonction pour supprimer tout les autres cases cocher des ch buttons """
    if san_var.get() == 1 :
        esh_var.set(0)
        ash_var.set(0)
        pa_var.set(0)
        aucunvar.set(0)

def exitbtn():
    """On crée une fonction afin de quitter l'application"""
    mainwindow.destroy()

def exitbtn2():
    """Fonction pour fermer la derniere fenetre"""
    lastwindow.destroy()

def homebtn():
    """On crée une fonction afin de retourner à la fenètre initiale"""
    secondframe.pack_forget()
    chframe.pack_forget()
    locframe.pack_forget()
    tutoframe.pack_forget()
    firstframe.pack(expand = YES)
    mainwindow.config(background = "#83B5DF")
def findbtn():
    """On crée une fonction afin d'aller dans la fenètre de recherche"""
    firstframe.pack_forget()
    chframe.pack_forget()
    locframe.pack_forget()
    tutoframe.pack_forget()
    secondframe.pack(expand = YES)
    mainwindow.config(background = "#009C98")

def locbtn():
    """On crée une fonction afin d'aller à la fenètre de localisation """
    firstframe.pack_forget()
    secondframe.pack_forget()
    tutoframe.pack_forget()
    chframe.pack_forget()
    if chuvar.get() == 1:
        chframe.pack(expand=YES)
        mainwindow.config(background = "#6879D0")
    else:
        locframe.pack(expand = YES)
        mainwindow.config(background = "#8093F1")

def chbtn():
    """On crée une fonction afin d'aller à la fenetre de localisation depuis ch frame"""
    firstframe.pack_forget()
    secondframe.pack_forget()
    chframe.pack_forget()
    tutoframe.pack_forget()
    locframe.pack(expand = YES)
    mainwindow.config(background = "#8093F1")

def osmbtn():
    """On crée une fonction de redirection vers Open Street Map"""
    WB.open_new("https://www.openstreetmap.org/#map=6/46.45/2.21")

def tutobtn():
    """On crée une fonction qui redirige vers un tutoriel pour osm"""
    firstframe.pack_forget()
    secondframe.pack_forget()
    chframe.pack_forget()
    locframe.pack_forget()
    tutoframe.pack(expand = YES)
    mainwindow.config(background = "#8093F1")

def launchbtn():
    """On crée une fonction qui détruit la fenêtre pour ensuite lancer la seconde phase (recherche)"""
    try:
        x = locvar.get().strip(' ').split(',') # x est une variable temporaire
        float(x[0])
        float(x[1])
        mainwindow.destroy()
    except:
        locvar.set("")
        errorlabel.grid(row = 5)

# On déclare les variables coordonnées user

coord_user_a = "0"
coord_user_b = "0"
coord_user = "0, 0"

# Création de la fenètre principale


logo_ICO = os.sep.join(["..", "data", "logo.ico"])
mainwindow = Tk()
mainwindow.geometry("1440x900")
mainwindow.minsize(500,500)
mainwindow.title("PyCareFinder")
mainwindow.iconbitmap(logo_ICO)
mainwindow.config(background = "#83B5DF")

#Création des frames

firstframe = Frame(mainwindow, bg = "#83B5DF")
firstframe.pack(expand = YES)

secondframe = Frame(mainwindow, bg = "#009C98")

chframe = Frame(mainwindow, bg = "#6879D0")

locframe = Frame(mainwindow, bg = "#8093F1")

tutoframe = Frame(mainwindow, bg = "#8093F1" )

#Création des textes

introlabel = Label(firstframe ,
    text="Bienvenue dans PyCareFinder !,\nun programme de recherche d'établissement(s) de santé le(s) plus proche(s).\n\nComme son nom l'indique ce programme a pour objectif de déterminer les établissements de santé les plus proches\n selon vos critères.\n\n(Ce programme se base sur diverses bases de données contenant des informations qui peuvent être incomplètes.)",
    font =("Helvetica",20),
    bg = "#83B5DF",
    fg = "white")
introlabel.pack()

secondlabel = Label(secondframe,
    text = "Veuillez sélectionner le(s) établissement(s) de santé que vous rechercher :",
    font =("Helvetica",20),
    bg = "#009C98",
    fg = "white")
secondlabel.grid(row = 0)

chlabel = Label(chframe,
    text = "Veuillez sélectionner le service particulier que vous rechercher pour les CHU / CH :",
    font =("Helvetica",20),
    bg = "#6879D0",
    fg = "white")
chlabel.grid(row = 0)

loclabel = Label(locframe,
    text = "Veuillez entrer vos coordonnées en les copiant depuis OpenStreetMap :",
    font =("Helvetica",20),
    bg = "#8093F1",
    fg = "white")
loclabel.grid(row = 0)

locentrylabel = Label(locframe,
    text = "Veuillez coller vos coordonnées ici:",
    font =("Helvetica",20),
    bg = "#8093F1",
    fg = "white")
locentrylabel.grid(row = 3)

errorlabel = Label(locframe,
    text = "Format non respecté",
    font =("Helvetica",20),
    bg = "#8093F1",
    fg = "red")

#Création des boutons

startbutton = Button(firstframe, bg = "#83B5DF", text = "Commencer la recherche", font=("Helvetica", 20), fg="white" , command= findbtn)
startbutton.pack(pady="15")

secondtothirdbutton = Button(secondframe, bg = "#009C98", text = "Poursuivre la recherche ", font=("Helvetica", 20),fg="black", command = locbtn)
secondtothirdbutton.grid(row = 5, pady = 100  )

chbutton = Button(chframe, bg = "#6879D0", text = "Poursuivre la recherche ", font=("Helvetica", 20), fg="white" , command= chbtn)
chbutton.grid(row = 6, pady = 100)

osmbutton = Button(locframe, bg = "#8093F1", text = "Open Street Map ", font=("Helvetica", 20), fg="white" , command= osmbtn)
osmbutton.grid(row = 1)

tutobutton = Button(locframe, bg = "#8093F1", text = "Tuto utilisation d'OpenStreetMap ", font=("Helvetica", 20), fg="white" , command= tutobtn)
tutobutton.grid(row = 2,pady=15)

launchbutton = Button(locframe, bg = "#8093F1", text = "Lancer le programme de recherche ", font=("Helvetica", 20), fg="white" , command= launchbtn)
launchbutton.grid(row = 6,pady=15)

returnbutton = Button(tutoframe, bg = "#8093F1", text = "Retour", font=("Helvetica", 20), fg="white" , command= chbtn)
returnbutton.grid(row = 1,pady=60)
#Création d'un champ de texte
locvar = StringVar()
locentry = Entry(locframe,bg = "#8093F1", font=("Helvetica", 20), fg="white", textvariable = locvar)
locentry.grid(row = 4)

#Création des images
tuto1_png = os.sep.join(["..", "data", "tuto1.png"])
tuto1 = ImageTk.PhotoImage(Image.open(tuto1_png))
tuto1label = Label(tutoframe, image = tuto1)
tuto1label.grid(column = 0, padx=15, row=0)

tuto2_png = os.sep.join(["..", "data", "tuto2.png"])
tuto2 = ImageTk.PhotoImage(Image.open(tuto2_png))
tuto2label = Label(tutoframe, image = tuto2)
tuto2label.grid(column = 3,padx=15, row=0)

#Création des checkbuttons second frame
#checkbuttons variables
chuvar = IntVar()
helistationvar = IntVar()
pharmacievar = IntVar()
ehpadvar = IntVar()

#checkbuttons
chucheckbutton = Checkbutton(secondframe, offvalue = 0, onvalue = 1, variable = chuvar,  bg ="#009C98" , text = "CH / CHU", font=("Helvetica", 20),fg="black" , activeforeground = "#009C98", activebackground = "white" , relief = GROOVE,)
chucheckbutton.grid(pady=7,row = 1)

helistationcheckbutton = Checkbutton(secondframe, offvalue = 0, onvalue = 1 , variable = helistationvar, bg ="#009C98" , text = "Hélistations hospitalières" , font=("Helvetica", 20) , fg="black" ,activeforeground = "#009C98", activebackground = "white", relief = GROOVE)
helistationcheckbutton.grid(pady=7,row = 2)

pharmaciecheckbutton = Checkbutton(secondframe, offvalue = 0, onvalue = 1 , variable = pharmacievar, bg ="#009C98" , text = "Pharmacies", font=("Helvetica", 20) , fg="black" ,activeforeground = "#009C98", activebackground = "white", relief = GROOVE)
pharmaciecheckbutton.grid(pady=7,row = 3)

ehpadbutton = Checkbutton(secondframe, offvalue = 0, onvalue = 1 , variable = ehpadvar, bg ="#009C98" , text = "EHPAD", font=("Helvetica", 20) , fg="black" ,activeforeground = "#009C98", activebackground = "white", relief = GROOVE )
ehpadbutton.grid(pady=7,row = 4)

#Création des checkbuttons ch frame
#Checkbuttons variables
esh_var = IntVar()
ash_var = IntVar()
pa_var = IntVar()
san_var = IntVar()
aucunvar = IntVar()
aucunvar.set(1)

#Checkbuttons
aucuncheckbutton = Checkbutton(chframe,offvalue =0, onvalue =1, variable = aucunvar,  bg ="#6879D0" , text = "Aucun", font=("Helvetica", 20),fg="black" , activeforeground = "#6879D0", activebackground = "white" , relief = GROOVE, command = aucunbtn )
aucuncheckbutton.grid(pady=7,row = 1)

eshcheckbutton = Checkbutton(chframe,offvalue =0, onvalue =1, variable = esh_var,  bg ="#6879D0" , text = "Équipement social ou médico-social pour enfants en situation de handicap", font=("Helvetica", 20),fg="black" , activeforeground = "#6879D0", activebackground = "white" , relief = GROOVE, command = esh_btn)
eshcheckbutton.grid(pady=7,row = 2)

ashcheckbutton = Checkbutton(chframe,offvalue =0, onvalue =1, variable = ash_var,  bg ="#6879D0" , text = "Équipement social ou médico-social pour adultes en situation de handicap", font=("Helvetica", 20),fg="black" , activeforeground = "#6879D0", activebackground = "white" , relief = GROOVE, command = ash_btn)
ashcheckbutton.grid(pady=7,row = 3)

pacheckbutton = Checkbutton(chframe,offvalue =0, onvalue =1, variable = pa_var,  bg ="#6879D0" , text = "Équipement social ou médico-social pour personnes âgées", font=("Helvetica", 20),fg="black" , activeforeground = "#6879D0", activebackground = "white" , relief = GROOVE, command = pa_btn)
pacheckbutton.grid(pady=7,row = 4)

sancheckbutton = Checkbutton(chframe,offvalue =0, onvalue =1, variable = san_var,  bg ="#6879D0" , text = "Activité sanitaire mise en œuvre", font=("Helvetica", 20),fg="black" , activeforeground = "#6879D0", activebackground = "white" , relief = GROOVE, command = san_btn)
sancheckbutton.grid(pady=7,row = 5)


#Création de la barre de menu
menubar = Menu(mainwindow  )
menubar.add_command(label= "Quitter", command = exitbtn )
menubar.add_command(label= "Page d'accueil", command = homebtn )
menubar.add_command(label= "Établissements à rechercher", command = findbtn )
menubar.add_command(label= "Votre localisation", command = chbtn )
menubar.add_command(label= "OpenStreetMap", command = osmbtn )

# # # Traitement base de données # # #

# Hélistations hospitalières

helistations = os.sep.join(["..", "data", "helistations.csv"])

data = []

with open(helistations, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        valeur = line.rstrip("\n").split(",")
        data.append(valeur)

liste_coord_helistations = []
for i in range(1, len(data)):
    coord_heli = data[i][6]+','+data[i][7]
    liste_coord_helistations.append(coord_heli)

# Établissements de soins (pharmacie, chu/ch, ehpad)

t_finess2 = os.sep.join(["..", "data", "t-finess2.csv"])

data_etab = []

with open(t_finess2, 'r', encoding='UTF-8') as g:
    lines = g.readlines()
    for line in lines:
        valeur = line.rstrip("\n").split(",")
        data_etab.append(valeur)

#Activation et configuration de la fenêtre
mainwindow.config(menu= menubar)
mainwindow.mainloop()

# # # Création liste CHU / CH / Pharmacie / EHPAD # # #

# création variable services

servicevar = 0
if esh_var.get() == 1:
    servicevar = 50

if ash_var.get() == 1:
    servicevar = 51

if pa_var.get() == 1:
    servicevar = 52

if san_var.get() == 1:
    servicevar = 53

if aucunvar.get() == 1:
    servicevar = 0

# Traitement données

liste_pharmacie = []
liste_coord_pharmacie = []

liste_ehpad = []
liste_coord_ehpad = []

liste_ch = []
liste_coord_ch = []

for i in range(1, len(data_etab)):
    liste_nom_etab = data_etab[i][6].strip('"').split(' ')
    validite = data_etab[i][4].strip('"')
    typ = data_etab[i][7].strip('"')
    if 'PHARMACIE' in liste_nom_etab and validite == 'ACTUEL' and typ == 'ET':
        liste_pharmacie.append(data_etab[i])
        liste_coord_pharmacie.append((data_etab[i][-1].strip('"'))+', '+(data_etab[i][-2].strip('"')))

    if 'EHPAD' in liste_nom_etab and validite == 'ACTUEL' and typ == 'ET':
        liste_ehpad.append(data_etab[i])
        liste_coord_ehpad.append((data_etab[i][-1].strip('"'))+', '+(data_etab[i][-2].strip('"')))

    if servicevar != 0:
        service_oui_non = data_etab[i][servicevar].strip('"')
        if ('CH' in liste_nom_etab or 'CHU' in liste_nom_etab) and validite == 'ACTUEL' and typ == 'ET' and service_oui_non == 'OUI':
            liste_ch.append(data_etab[i])
            liste_coord_ch.append((data_etab[i][-1].strip('"'))+', '+(data_etab[i][-2].strip('"')))
    elif ('CH' in liste_nom_etab or 'CHU' in liste_nom_etab) and validite == 'ACTUEL' and typ == 'ET':
        liste_ch.append(data_etab[i])
        liste_coord_ch.append((data_etab[i][-1].strip('"'))+', '+(data_etab[i][-2].strip('"')))

# Coordonées user

coord_user = locvar.get()

coord_user_liste = coord_user.split(',') # split coordonnées user pour la carte folium

coord_user_a = float(coord_user_liste[0].strip(' '))
coord_user_b = float(coord_user_liste[1].strip(' '))

# # # Analyse distances + ajout sur la carte folium + génération fichier txt (informations établissements de soins) # # #

# Création carte folium et fichier info.txt

carte_data = folium.Map(location=[coord_user_a,coord_user_b],zoom_start=15)
folium.Marker([coord_user_a,coord_user_b],popup='Votre position').add_to(carte_data)
info_txt = os.sep.join(['..', 'data', 'info.txt'])
fsource = open(info_txt, 'w', encoding='latin-1')

# Hélistations

if helistationvar.get() == 1:
    dis_min_heli = distance_min(coord_user, liste_coord_helistations)
    km_heli_rac = str(dis_min_heli[0])[:5].rstrip('.')
    heli_a_b = liste_coord_helistations[dis_min_heli[1]].split(',')
    heli_a = float(heli_a_b[0])
    heli_b = float(heli_a_b[1])

    folium.Marker([heli_a,heli_b],popup='Hélistation hospitalière').add_to(carte_data)
    folium.PolyLine(locations=[(coord_user_a, coord_user_b), (heli_a, heli_b)], color="#FF0000", weight=5, tooltip=f"Distance : {km_heli_rac} km").add_to(carte_data)

    fsource.write(f"Hélistation hospitalière :\nVille : {data[(dis_min_heli[1])+1][4]}\nPays : France\nDistance à vol d'oiseau : {km_heli_rac} km\n\n")

# Pharmacie

if pharmacievar.get() == 1:
    dis_min_pharmacie = distance_min(coord_user, liste_coord_pharmacie)
    km_pharmacie_rac = str(dis_min_pharmacie[0])[:5].rstrip('.')
    ville_pharmacie_proche = liste_pharmacie[(dis_min_pharmacie[1])][23].strip('"')
    nom_pharmacie_proche = liste_pharmacie[(dis_min_pharmacie[1])][6].strip('"')
    notel = liste_pharmacie[(dis_min_pharmacie[1])][24].strip('"')

    pharmacie_a = float(liste_pharmacie[dis_min_pharmacie[1]][-1].strip('"'))
    pharmacie_b = float(liste_pharmacie[dis_min_pharmacie[1]][-2].strip('"'))

    folium.Marker([pharmacie_a,pharmacie_b],popup='Pharmacie').add_to(carte_data)
    folium.PolyLine(locations=[(coord_user_a, coord_user_b), (pharmacie_a, pharmacie_b)], color="#FF0000", weight=5, tooltip=f"Distance : {km_pharmacie_rac} km").add_to(carte_data)

    fsource.write(f"Pharmacie :\nNom : {nom_pharmacie_proche}\nVille : {ville_pharmacie_proche}\nPays : France\nDistance à vol d'oiseau : {km_pharmacie_rac} km\nN° de tel : {notel}\n\n")

# CHU / CH

if chuvar.get() == 1:
    dis_min_ch = distance_min(coord_user, liste_coord_ch)
    km_ch_rac = str(dis_min_ch[0])[:5].rstrip('.')
    ville_ch_proche = liste_ch[(dis_min_ch[1])][23].strip('"')
    nom_ch_proche = liste_ch[(dis_min_ch[1])][6].strip('"')
    notel = liste_ch[(dis_min_ch[1])][24].strip('"')

    ch_a = float(liste_ch[dis_min_ch[1]][-1].strip('"'))
    ch_b = float(liste_ch[dis_min_ch[1]][-2].strip('"'))

    folium.Marker([ch_a,ch_b],popup='CHU / CH').add_to(carte_data)
    folium.PolyLine(locations=[(coord_user_a, coord_user_b), (ch_a, ch_b)], color="#FF0000", weight=5, tooltip=f"Distance : {km_ch_rac} km").add_to(carte_data)

    fsource.write(f"CHU / CH :\nNom : {nom_ch_proche}\nVille : {ville_ch_proche}\nPays : France\nDistance à vol d'oiseau : {km_ch_rac} km\nN° de tel : {notel}\n\n")

# EHPAD

if ehpadvar.get() == 1:
    dis_min_ehpad = distance_min(coord_user, liste_coord_ehpad)
    km_ehpad_rac = str(dis_min_ehpad[0])[:5].rstrip('.')
    ville_ehpad_proche = liste_ehpad[(dis_min_ehpad[1])][23].strip('"')
    nom_ehpad_proche = liste_ehpad[(dis_min_ehpad[1])][6].strip('"')
    notel = liste_ehpad[(dis_min_ehpad[1])][24].strip('"')

    ehpad_a = float(liste_ehpad[dis_min_ehpad[1]][-1].strip('"'))
    ehpad_b = float(liste_ehpad[dis_min_ehpad[1]][-2].strip('"'))

    folium.Marker([ehpad_a,ehpad_b],popup='EHPAD').add_to(carte_data)
    folium.PolyLine(locations=[(coord_user_a, coord_user_b), (ehpad_a, ehpad_b)], color="#FF0000", weight=5, tooltip=f"Distance : {km_ehpad_rac} km").add_to(carte_data)

    fsource.write(f"EHPAD :\nNom : {nom_ehpad_proche}\nVille : {ville_ehpad_proche}\nPays : France\nDistance à vol d'oiseau : {km_ehpad_rac} km\nN° de tel : {notel}\n\n")

# Enregistrement de la carte et du fichier txt

map = os.sep.join(['..', 'data', 'map.html'])
carte_data.save(map)

fsource.close()

WB.open_new('index.html')
