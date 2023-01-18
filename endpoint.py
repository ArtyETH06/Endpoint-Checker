#Les imports
import os
import requests
from colorama import init, Fore, Style
import pyfiglet
from math import *

#Initialisation
init()

#Clear auto du terminal (trop usefull)
os.system('cls||clear')

#Définition des variables
i = 0
t = 0
accept_tab = []
error = "<Response [404]>"
accept  ="<Response [200]>"
endpoint = pyfiglet.figlet_format("Endpoint Checker", font = "big")

print(Fore.GREEN + Style.BRIGHT+ "============================================================================================================================================================================================================================================\n\n\n")
print(endpoint,"\n\nCoded By Arty06, open source code\n Github --> github.com/ArtyETH06")
print(Fore.GREEN + Style.BRIGHT +  "============================================================================================================================================================================================================================================\n\n")

#On travail avec le fichier contenannt les endpoint
list = open('list.txt', 'r+')

#La variable fichier contient tous les mots
contenu = list.readlines()
#Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

print(Fore.RED + Style.BRIGHT +"Par défault,la liste des endpoints est une petite liste random, si vous voulez modifier ces valeurs,vous avez juste à modifier le fichier `list.txt` !\n")


#URL à tester
base_URL = input(Fore.CYAN + Style.BRIGHT + "Quelle est l'URL que vous souhaitez tester ?\n")
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
user_agent = user_agent[0]
headers = {'user-Agent':user_agent}

#Boucle pour aller chercher tout les mots + regarder si l'URL existe
#Pour avor la bonne longueur
for i in range(0,len(contenu)):
    line = contenu[i]
    line = line.replace("\n","")
    modify_URL = base_URL + line
    print("Trying ",modify_URL)
    
    r = requests.get(modify_URL, headers=headers)
    print(r)
    print(Fore.GREEN + Style.BRIGHT + "URL testée: ",modify_URL,"\n","Status:", r)

    #Faire la barre de progression
    total = len(contenu)
    percentage = i * 100 / total
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")



    if r.status_code == 200 and modify_URL != base_URL:
        accept_tab.append(modify_URL)
    print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")

print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")



#---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
print("Les endpoints valides sont les suivants:\n\n")
for t in range(0,len(accept_tab)):
    print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

save = input(Fore.CYAN + Style.BRIGHT + "\n\n\nVoulez vous enregister les endpoints dans un fichier ? (Note: les endpoints seront ajoutés,si il en existe déjà dans le fichier,ils seront stockés dans: `endpoints.txt) (y/n)")

#Nom avec site checked (base URl)

name = "\n\n========================================================================== " + base_URL + " ==========================================================================\n\n"

if save == "y":
    with open("endpoints.txt", "a") as file:
        #Délimitation pour l'URL analysée (checked)
        file.write(name) 
        for t in range(0,len(accept_tab)):
            file.write(accept_tab[t])
            file.write("\n")
        file.close()
    print(Fore.RED + Style.BRIGHT + "\nLes résultats ont été enregistrés dans le fichier `endpoints.txt' !")
    


#On close le fichier
list.close()