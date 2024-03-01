from joueur import Joueur
from liste_pokemon import liste_pokemon


class Jeu:
    def __init__(self):
        self.joueurs = []

    def jouer(self):
        print("Bienvenue dans le jeu Pokemon!")
        # Inscription des joueurs
        for i in range(2):
            nom_joueur = input(f"Joueur {i+1}, veuillez entrer votre nom: ")
            argent_joueur = 1000  # Par exemple, vous pouvez donner 1000 unités d'argent à chaque joueur pour acheter des pokémons
            joueur = Joueur(nom_joueur, argent_joueur)
            self.joueurs.append(joueur)

        # Les joueurs choisissent leurs Pokémon tour à tour
        for joueur in self.joueurs:
            print(f"{joueur.nom}, c'est à votre tour de choisir vos Pokémons.")
            joueur.choisir_pokemon(liste_pokemon, {joueur.nom})

        print("Début du jeu!")

        # Trois rounds de combat
        for round_num in range(3):
            print(f"Round {round_num + 1}:")
            joueur1 = self.joueurs[0]
            joueur2 = self.joueurs[1]

            # Combat entre les pokemons de chaque joueur
            for i in range(3):
                pokemon_joueur1 = joueur1.recuperer_pokemon(i + 1)
                pokemon_joueur2 = joueur2.recuperer_pokemon(i + 1)

                while not pokemon_joueur1.est_ko() and not pokemon_joueur2.est_ko():
                    attaque_joueur1 = joueur1.choisir_attaque(pokemon_joueur1)
                    attaque_joueur2 = joueur2.choisir_attaque(pokemon_joueur2)

                    # Déterminer qui attaque en premier en fonction de la vitesse
                    if pokemon_joueur1.vitesse > pokemon_joueur2.vitesse:
                        pokemon_joueur1.attaquer(pokemon_joueur2, attaque_joueur1)
                        if not pokemon_joueur2.est_ko():
                            pokemon_joueur2.attaquer(pokemon_joueur1, attaque_joueur2)
                    else:
                        pokemon_joueur2.attaquer(pokemon_joueur1, attaque_joueur2)
                        if not pokemon_joueur1.est_ko():
                            pokemon_joueur1.attaquer(pokemon_joueur2, attaque_joueur1)

            # Afficher les résultats du round
            print("Résultats du round:")
            for i in range(3):
                pokemon_joueur1 = joueur1.recuperer_pokemon(i + 1)
                pokemon_joueur2 = joueur2.recuperer_pokemon(i + 1)
                if pokemon_joueur1.est_ko():
                    print(f"{joueur2.nom} remporte le combat avec {pokemon_joueur2.nom} !")
                    joueur2.manche_gagnee += 1
                elif pokemon_joueur2.est_ko():
                    print(f"{joueur1.nom} remporte le combat avec {pokemon_joueur1.nom} !")
                    joueur1.manche_gagnee += 1
                else:
                    print("Match nul !")

        # Déterminer le gagnant du jeu
        if joueur1.manche_gagnee >= 2:
            print(f"{joueur1.nom} remporte le jeu !")
        elif joueur2.manche_gagnee >= 2:
            print(f"{joueur2.nom} remporte le jeu !")
        else:
            print("Match nul !")

        # Demander aux joueurs s'ils veulent rejouer
        rejouer = input("Voulez-vous rejouer ? (o/n): ")
        if rejouer.lower() == 'o':
            self.jouer()
        else:
            print("Merci d'avoir joué !")

# Programme principal
jeu = Jeu()
jeu.jouer()
