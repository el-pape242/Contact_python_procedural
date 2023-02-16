contact =dict()

def main():

    def repertoire():
        #Mise en place du menu

        print("==== MENU CONTACT ==== ")

        print("1-Ajouter contact")

        print("2-Modifier contact")

        print("3-Supprimer contact")

        print("4-Afficher tout les contacts")

        print("5-Afficher un contact")

        print("6-Quitter")


        choix = input("Veillez choisir une valeur : ")


        # Fonction pour l'ajout de contact
        def ajout():

            # Demander à l'utilisateur combien de contact il souhaite ajouter
            nb_dicos = int(input("Combien de contact voulez-vous ajouter ? : "))

            # Boucler à travers chaque dictionnaire
            for i in range(nb_dicos):

                print(f"\nSaisie pour le contact n°{i+1}")

                dico = {}

                for j in range(1):

                    nom = input(f"saisir nom : ")

                    prenom = input(f"saisir prenom : ")

                    genre = input(f"saisir genre : ")

                    age = int(input(f"saisir age : "))

                    adresse = input(f"saisir addresse : ")

                    profession = input(f"saisir profession : ")

                    key = "Nom"
                    dico[key] = nom

                    key1 = "Prenom"
                    dico[key1] = prenom

                    key2 = "Genre"
                    dico[key2] = genre

                    key3 = "Age"
                    dico[key3] = age

                    key4 = "Adresse"
                    dico[key4] = adresse

                    key5 = "Profession"
                    dico[key5] = profession

                # Ajouter le dictionnaire au dictionnaire principal
                contact[f"dico_{i+1}"] = dico

            print(f" {contact}")


        # Fonction pour modification de contact
        def updates():

            # Demander à l'utilisateur de saisir la valeur à chercher
            print("Quel contact souhaitez-vous modifier dans l'annuaire ? : ")

            valeur_recherchee = input("Inserer le nom du contact : ")

            contact_trouve = False

            #Recherche du contact
            for user in contact.values():

                for ma_cle, valeurs in user.items():

                    #si contact trouvé
                    if valeurs == valeur_recherchee:

                        elt = input("Que souhaitez-vous modifier comme élement de ce contact ? :")

                        new_elt = elt.title()

                        if new_elt == "Age":
                            nouvelle_valeur = int(input(f"Entrez la nouvelle valeur pour {new_elt} : "))

                            user[new_elt] = nouvelle_valeur

                            print(f"L'Age' a été modifiée avec succès.")

                            print(contact)

                            contact_trouve = True

                        else:
                            nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {new_elt} : ")

                            user[new_elt] = nouvelle_valeur

                            print(f"La valeur de {new_elt} a été modifiée avec succès.")

                            print(contact)

                            contact_trouve = True

            #Contact non trouvé
            if not contact_trouve:

                print(f"Aucun contact trouvé avec le nom : {valeur_recherchee}.")


        #Fonction de suppression de contact
        def suppression():

            # Demander à l'utilisateur de saisir la valeur à chercher
            print("Qui souhaitez-vous supprimer de l'annuaire ? : ")

            sup = input("Saisir un nom: ")

            # Parcourir le dictionnaire pour trouver le nom correspondant
            dico_a_supprimer = None

            for k, x in contact.items():

                if sup in x.values():

                    dico_a_supprimer = k

                    break

            # Supprimer le dictionnaire correspondant, s'il existe
            if dico_a_supprimer is not None:

                del contact[dico_a_supprimer]

                print("Le contact correspondant a été supprimé avec succès.")

            else:

                print("Ce contact est introuvable.")

            print(contact) # affiche le dictionnaire mis à jour


        #Fonction d'affichage de tout les contacts
        def affichage_Allcontact():

            for employee in contact.values():

                for cle, valeur in employee.items():

                    print(f"{cle}: {valeur}")

                print("===============")


        #Fonction d'affichage detail d'un contact
        def affichage_contact():

            # Demander à l'utilisateur de saisir la valeur à rechercher
            print("Quel contact recherchez-vous ?")

            valeur_recherchee = input("Saisissez son nom: ")

            # Boucle à travers chaque dictionnaire dans le dictionnaire imbriqué
            for nom_dictionnaire, dictionnaire in contact.items():

                # Vérifier si la valeur est présente dans le dictionnaire actuel
                if valeur_recherchee in dictionnaire.values():

                    # Afficher le dictionnaire correspondant
                    print(f"Le detail correspondant au contact {valeur_recherchee} est {dictionnaire} ")

                    break
            else:

                # Si le contact n'est pas trouvée dans tous les dictionnaires
                print(f"Le nom {valeur_recherchee} n'a pas été trouvé dans l'annuaire .")


        #Choix d'ajout de contact
        if choix == "1":

            ajout()


        #Choix de Modification de contact
        elif choix == "2":

            updates()


        #Choix de suppression de contact
        elif choix == "3":

            suppression()


        #Choix d'afficher tout les contacts
        elif choix == "4":

            affichage_Allcontact()


        #Choix d'afficher un contact
        elif choix == "5":

            affichage_contact()


        #Quitter programme
        elif choix == "6":

            exit()

        #Erreur de saisie
        else:

            print("saisissez une valeur correct")


    def suite():

        while True:

            saisi = input("voulez-vous continuer ? o/n : ")

            if saisi.lower() not in ("o","n"):

                print("saisir 'o' ou 'n' ")

            elif saisi.lower()=="o":
                repertoire()

            else:

                print("Bye Bye")

                break


    #Execution des fonctions
    repertoire()

    suite()


if __name__ == "__main__":
    main()