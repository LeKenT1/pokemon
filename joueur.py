from pickle import NONE
from pokemon import Pokemon
from rich.table import Table
from rich.console import Console
from rich.text import Text
from typing import List

class Joueur:
    def __init__(self, nom, argent, adversaire=NONE):
        self.nom = nom
        self.manche_gagnee = 0
        self.argent = argent
        self.adversaire = adversaire 
        self.pokemons = []

    def choisir_pokemon(self, liste_pokemon: List[Pokemon]):
        console = Console()
        while True:
            console.print(f"[cyan]{self.nom}[/cyan], choisissez vos [yellow]3[/yellow] [red]Pokémons[/red], vous avez [green]{self.argent} ¤:[/green]")
            console.print(f"Entrez les [yellow]numéros[/yellow] des [red]Pokémons[/red] séparés par des virgules (ex: 1,2,3): ")
            choix_pokemons = input()
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
        console = Console()

        while True:
            pokemon.afficher_attaques()

            console.print("Entrez le [cyan]numéro[/cyan] de l'[magenta]attaque[/magenta] (1 ou 2):")
            choix_attaque = input()

            if choix_attaque.isdigit():
                indice_attaque = int(choix_attaque) - 1
                if 0 <= indice_attaque < len(pokemon.attaques):
                    return pokemon.attaques[indice_attaque]

            print("Choix invalide. Veuillez taper 1 ou 2.")

    def afficher_combat(self, pokemon1, pokemon2):
        console = Console()

        table = Table(title="[bold]Résultat du combat[/bold]")
        table.add_column("Pokémon", style="bold cyan", justify="center")
        table.add_column("PV restants", style="bold green", justify="center")

        table.add_row(pokemon1.nom, f"{round(pokemon1.pv, 1)}")
        table.add_row(pokemon2.nom, f"{round(pokemon2.pv, 1)}")

        console.print(table)

    def recuperer_pokemon(self, numero):
        if 1 <= numero <= len(self.pokemons):
            return self.pokemons[numero - 1]
        else:
            print("Numéro de Pokémon invalide.")
            return None

    def afficher_pokemons(self):
        print(f"Liste des Pokémons de {self.nom}:")
        for pokemon in self.pokemons:
            print(f"Nom: {pokemon.nom}, PV: {pokemon.pv}, Type(s): {pokemon.types}, Niveau: {pokemon.niveau}, Attaques: {', '.join(pokemon.attaques.keys())}")

    def afficher(self):
        print(f"Nom: {self.nom}, Manches gagnées: {self.manche_gagnee}, Argent: {self.argent}")
