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


choice = int(input(Fore.CYAN + Style.BRIGHT + "Wich mode would you like to choose ?\n1-Many endpoints on 1 website\n2-1 endpoint on many websites\n"))



if choice == 1:

#===================================================================================Mode 1===========================================================================================




    #On travail avec le fichier contenannt les endpoint
    list = open('list1.txt', 'r+')

    #La variable fichier contient tous les mots
    contenu = list.readlines()
    #Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

    print(Fore.RED + Style.BRIGHT +"By default, the list of endpoints is a small random list, if you want to modify these values, you just have to modify the `list.txt` file!\n")
        

    #URL à tester
    base_URL = input(Fore.CYAN + Style.BRIGHT + "Wich URL would you like to test ?\n")
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
    user_agent = user_agent[0]
    headers = {'user-Agent':user_agent}

    #Boucle pour aller chercher tout les mots + regarder si l'URL existe
    #Pour avor la bonne longueur
    for i in range(0,len(contenu)):
        line = contenu[i]
        line = line.replace("\n","")
        modify_URL = base_URL + line

        
        r = requests.get(modify_URL, headers=headers)
        #print(r)
#---------------------------------------------Endpoint valide--------------------------------------------------------
        if r.status_code == 200 and modify_URL != base_URL:
            print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
            print("Trying ",modify_URL)
            print(Fore.GREEN + Style.BRIGHT + "URL tested: ",modify_URL,"\n","Status:", r)

            #Faire la barre de progression
            total = len(contenu)
            percentage = i * 100 / total
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

            accept_tab.append(modify_URL)
            print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


#-----------------------------------------------Endpoint non valide-------------------------------------------------------------------

        else:
            print(Fore.RED + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")
            print(Fore.RED + Style.BRIGHT + "URL tested: ",modify_URL,"\n","Status:", r,"\nNot valid endpoint")
            #Faire la barre de progression
            total = len(contenu)
            percentage = i * 100 / total
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")



            accept_tab.append(modify_URL)
            print(Fore.RED+ Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


    #Fin du scan
    print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")



    #---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
    print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
    print("The valid endpoints are:\n\n")
    for t in range(0,len(accept_tab)):
        print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

    save = input(Fore.CYAN + Style.BRIGHT + "\n\n\nDo you want to save endpoints to a file? (Note: endpoints will be added, if any already exist in the file, they will be stored in: `endpoints.txt) (y/n)")

    #Nom avec site checked (base URl)

    name = "\n\n========================================================================== " + base_URL + " ==========================================================================\n\n"

    if save == "y":
        with open("endpoints_mode1.txt", "a") as file:
            #Délimitation pour l'URL analysée (checked)
            file.write(name) 
            for t in range(0,len(accept_tab)):
                file.write(accept_tab[t])
                file.write("\n")
            file.close()
        print(Fore.RED + Style.BRIGHT + "\nThe results have been saved into `endpoints_mode1.txt' !")
        


    #On close le fichier
    list.close()

#===============================================================================================================================================================================








#===================================================================================Mode 2==========================================================================================

elif choice == 2:
        #On travail avec le fichier contenannt les endpoint
    list = open('list2.txt', 'r+')

    #La variable fichier contient tous les mots
    contenu = list.readlines()
    #Un tableau s'est créé,|0 = première ligne,1 = 2e ligne...

    print(Fore.RED + Style.BRIGHT +"By default, the list of endpoints is a small random list, if you want to modify these values, you just have to modify the `list.txt` file!\n")
        

    #URL à tester
    base_endpoint = input(Fore.CYAN + Style.BRIGHT + "Quelle est l'endpoint que vous souhaitez tester ?\n")
    user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/109.0.0.0 Safari/537.36"]
    user_agent = user_agent[0]
    headers = {'user-Agent':user_agent}

    #Boucle pour aller chercher tout les mots + regarder si l'URL existe
    #Pour avor la bonne longueur
    for i in range(0,len(contenu)):
        line = contenu[i]
        line = line.replace("\n","")
        modify_endpoint =  line + base_endpoint
        print("Trying ",modify_endpoint)
        
        r = requests.get(modify_endpoint, headers=headers)
        print(r)

#-----------------------------------------------------Endpoint valide------------------------------------------------------

        if r.status_code == 200 and modify_endpoint != base_endpoint:
            print(Fore.GREEN + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r)

            #Faire la barre de progression
            total = len(contenu)
            percentage = i * 100 / total
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

            accept_tab.append(modify_endpoint)
            print(Fore.GREEN + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")


#-----------------------------------------------------------Endpoint non valide--------------------------------------------------------------
        else:
            print(Fore.RED + Style.BRIGHT + "URL testée: ",modify_endpoint,"\n","Status:", r,"\nNot valid endpoint")

            #Faire la barre de progression
            total = len(contenu)
            percentage = i * 100 / total
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n",percentage,"%")

            accept_tab.append(modify_endpoint)
            print(Fore.RED + Style.BRIGHT + "=======================================================================================================================================================================================\n\n")

    print(Fore.RED + Style.BRIGHT + "SCAN COMPLETED")



    #---------------------------------------------------------------------------------------RECAP-----------------------------------------------------------------------------
    print(Fore.GREEN + Style.BRIGHT + "\n\n==============================================================================================RECAP===========================================================================================\n\n")
    print("Les endpoints valides sont les suivants:\n\n")
    for t in range(0,len(accept_tab)):
        print(Fore.RED + Style.BRIGHT + accept_tab[t],"")

    save = input(Fore.CYAN + Style.BRIGHT + "\n\n\nDo you want to save endpoints to a file? (Note: endpoints will be added, if any already exist in the file, they will be stored in: `endpoints.txt) (y/n)")

    #Nom avec site checked (base URl)
    name = "\n\n========================================================================== " + base_endpoint + " ==========================================================================\n\n"

    if save == "y":
        with open("endpoints_mode2.txt", "a") as file:
            #Délimitation pour l'URL analysée (checked)
            file.write(name) 
            for t in range(0,len(accept_tab)):
                file.write(accept_tab[t])
                file.write("\n")
            file.close()
        print(Fore.RED + Style.BRIGHT + "\nResults have been save into `endpoints_mode2.txt' !")
        


    #On close le fichier
    list.close()
