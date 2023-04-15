# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:29:25 2023
@author: aubru
"""

import hashlib
import json


try:
    with open('passwords.json', 'r') as f:
        passwords = json.load(f)
except FileNotFoundError:
    passwords = {}
    with open('passwords.json', 'w') as f:
        json.dump(passwords, f)


def check_password(password):
    """ Vérifie si le mot de passe répond aux exigences de sécurité """
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*" for c in password):
        return False
    return True

def hash_password(password):
    """ Hache le mot de passe en utilisant l'algorithme SHA-256 """
    return hashlib.sha256(password.encode()).hexdigest()

def add_password():
    """ Ajoute un nouveau mot de passe haché dans le fichier """
    password = input("Choisissez un mot de passe : ")
    while not check_password(password):
        print("Le mot de passe ne respecte pas les exigences de sécurité.")
        password = input("Choisissez un nouveau mot de passe : ")
    hashed_password = hash_password(password)
    with open("passwords.json", "r") as f:
        data = json.load(f)
    if hashed_password in data.values():
        print("Ce mot de passe est déjà enregistré.")
        return
    username = input("Entrez un nom d'utilisateur pour ce mot de passe : ")
    data[username] = hashed_password
    with open("passwords.json", "w") as f:
        json.dump(data, f)
    print("Le mot de passe a été enregistré avec succès.")

def view_passwords():
    """ Affiche tous les mots de passe enregistrés dans le fichier """
    with open("passwords.json", "r") as f:
        data = json.load(f)
    if not data:
        print("Il n'y a aucun mot de passe enregistré.")
    else:
        print("Voici la liste des mots de passe enregistrés :")
        for username, hashed_password in data.items():
            print(f"{username} : {hashed_password}")


while True:
    action = input("Que voulez-vous faire ? (ajouter / afficher / quitter) : ")
    if action == "ajouter":
        add_password()
    elif action == "afficher":
        view_passwords()
    elif action == "quitter":
        break
    else:
        print("Action invalide.")
