import hashlib
import json


def exercice_mdp(mdp):   
    mdp=str(input('veuillez entrer votre mot de passe : '))
    valide=False
    alphabet_maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_min=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chiffre=['1','2','3','4','5','6','7','8','9']
    carac_spe=['!','@','#','$','%','^','&','*']
    if len(mdp)>=8:
        for i in range(len(mdp)):
            for n in range(len(alphabet_maj)):
                if mdp[i]==alphabet_maj[n]:
                    for a in range(len(mdp)):
                        for b in range(len(alphabet_min)):
                            if mdp[a]==alphabet_min[b]:
                                for c in range(len(mdp)):
                                    for d in range(len(chiffre)):
                                        if mdp[c]==chiffre[d]:
                                            for e in range(len(mdp)):
                                                for f in range(len(carac_spe)):
                                                    if mdp[e]==carac_spe[f]:
                                                        valide=True
    if valide:
        print('c bon')
        mdp_crypte = hashlib.sha256(mdp.encode()).hexdigest()
        print("Mot de passe crypté: ", mdp_crypte)
        print('mot de passe enregistré')
    else:
        print ('erreur')
        return exercice_mdp(mdp)


def afficher_mdp(mdp_hash):
    for website, data in mdp_hash.items():
        print("Mot de passe:", data['mdp'])
        print("\n")


def enregistrer_mdp(mdp):
    with open("mdp.json", "w") as f:
        json.dump(mdp, f)


def charger_mdp():
    try:
        with open("mdp.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def main():
    mdp = charger_mdp()
    while True:
        choice = input("Que voulez-vous faire? [a]jouter un mot de passe, [v]oir les mots de passe, [q]uitter: ")
        if choice == "a":
            exercice_mdp(mdp)
        elif choice == "v":
            afficher_mdp(mdp)
        elif choice == "q":
            enregistrer_mdp(mdp)
            break
        else:
            print("Choix invalide !")


if __name__ == "__main__":
    main()