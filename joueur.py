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

    def choisir_pokemon(self, liste_pokemon: List[Pokemon]):
        while True:
            print(f"{self.nom}, choisissez vos 3 Pokémons, vous avez {self.argent} ¤:")
            choix_pokemons = input("Entrez les numéros des Pokémons séparés par des virgules (ex: 1,2,3): ")
            choix_indices = [int(x) - 1 for x in choix_pokemons.split(',') if x.isdigit()]
            if len(choix_indices) == 3:
                prix_total = sum(liste_pokemon[indice].prix for indice in choix_indices)
                if prix_total <= self.argent:
                    break
                else:
                    print("Vous n'avez pas assez d'argent pour acheter ces Pokémon.")
            else:
                print("Vous devez choisir exactement 3 Pokémon.")
        for indice in choix_indices:
            self.ajouter_pokemon(liste_pokemon[indice])
            self.argent -= liste_pokemon[indice].prix

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon):
        while True:
            print(f"{self.nom}, choisissez une attaque pour {pokemon.nom}:")
            for i, attaque in enumerate(pokemon.attaques, 1):
                print(f"{i}. {attaque.nom} (Puissance: {attaque.puissance})")
            choix_attaque = input("Entrez le numéro de l'attaque (1 ou 2): ")
            
            if choix_attaque.isdigit():
                indice_attaque = int(choix_attaque) - 1
                if 0 <= indice_attaque < len(pokemon.attaques):
                    return pokemon.attaques[indice_attaque]
            
            print("Choix invalide. Veuillez taper 1 ou 2.")



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
