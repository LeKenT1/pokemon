from pickle import NONE
from pokemon import Pokemon
from typing import List

class Joueur:
    def __init__(self, nom, argent, adversaire=NONE):
        self.nom = nom
        self.manche_gagnee = 0
        self.argent = argent
        self.adversaire = adversaire 
        self.pokemons = []

    # def choisir_pokemon(self, liste_pokemon: List[Pokemon]):
    #     print(f"{self.nom}, choisissez vos 3 Pokémons:")
    #     for i, pokemon in enumerate(liste_pokemon, 1):
    #         print(f"{i}. {pokemon.nom}")
    #     choix_pokemons = input("Entrez les numéros des Pokémons séparés par des virgules: ")
    #     choix_indices = [int(x) - 1 for x in choix_pokemons.split(',')]
    #     for indice in choix_indices:
    #         if 0 <= indice < len(liste_pokemon):
    #             self.ajouter_pokemon(liste_pokemon[indice])
    #         else:
    #             print("Choix invalide.")
    
    def choisir_pokemon(self, liste_pokemon: List[Pokemon], joueur_nom):
        pokemons_disponibles = liste_pokemon[:]  

        for _ in range(3):  
            print(f"Pokémons disponibles :")
            for i, pokemon in enumerate(pokemons_disponibles, 1):
                print(f"{i}. {pokemon.nom}")
                    
            choix_pokemon = int(input(f"{joueur_nom}, entrez le numéro du Pokémon que vous souhaitez choisir : "))
                
            if 1 <= choix_pokemon <= len(pokemons_disponibles):
                pokemon_choisi = pokemons_disponibles.pop(choix_pokemon - 1)  
                self.ajouter_pokemon(pokemon_choisi)
                print(f"{joueur_nom} a choisi {pokemon_choisi.nom}.")
            else:
                print("Choix invalide. Veuillez choisir un numéro valide.")

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon):
        print(f"{self.nom}, choisissez une attaque pour {pokemon.nom}:")
        for i, attaque in enumerate(pokemon.attaques, 1):
            print(f"{i}. {attaque.nom} (Puissance: {attaque.puissance})")
        choix_attaque = input("Entrez le numéro de l'attaque: ")
        indice_attaque = int(choix_attaque) - 1
        attaque = pokemon.attaques[indice_attaque]
        return attaque

    def recuperer_pokemon(self, numero):
        if 1 <= numero <= len(self.pokemons):
            return self.pokemons[numero - 1]
        else:
            print("Numéro de Pokémon invalide.")
            return None

    def afficher_pokemons(self):
        print(f"Liste des Pokémons de {self.nom}:")
        for pokemon in self.pokemons:
            print(f"Nom: {pokemon.nom}, PV: {pokemon.pv}, Attaques: {', '.join(pokemon.attaques.keys())}")

    def afficher(self):
        print(f"Nom: {self.nom}, Manches gagnées: {self.manche_gagnee}, Argent: {self.argent}")
