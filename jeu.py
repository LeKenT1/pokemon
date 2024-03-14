from joueur import Joueur
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from liste_pokemon import liste_pokemon

class Jeu:
    def __init__(self):
        self.joueurs = []
        
    def afficher_liste_pokemon(self):
        table = Table(title="Liste des Pokémons")

        table.add_column("", justify="center", style="white", no_wrap=True)

        for pokemon in liste_pokemon:
            table.add_column(pokemon.nom, justify="center", style="yellow", no_wrap=True)
            
        num_pokemon_row = ["Numéro:"]
        for i in range(1, len(liste_pokemon) + 1):
            num_pokemon_row.append(str(i))

        prix_row = ["Prix:"]
        for pokemon in liste_pokemon:
            prix_row.append("[green]" + str(pokemon.prix) + " ¤")

        table.add_row(*num_pokemon_row)
        table.add_row(*prix_row)

        console = Console()
        console.print(table)
        
    def jouer(self):
        console = Console()
        print("Bienvenue dans le jeu Pokemon!")

        for i in range(2):
            console.print(f"Joueur {i+1}, veuillez entrer votre [cyan]nom[/cyan] :")
            nom_joueur = input()
            argent_joueur = 10
            joueur = Joueur(nom_joueur, argent_joueur)
            self.joueurs.append(joueur)
            
        for joueur in self.joueurs:
            console.print(f"[cyan]{joueur.nom}[/cyan], c'est à votre tour de choisir vos [red]Pokémons[/red].")
            self.afficher_liste_pokemon()
            joueur.choisir_pokemon(liste_pokemon)

        print("Début du jeu!")

        joueur1 = self.joueurs[0]
        joueur2 = self.joueurs[1]

        for i in range(3):
            
            round_text = f"""
            ╔══════════════════════════╗
            ║         Round {i + 1}          ║
            ╚══════════════════════════╝
            """
            print(round_text)
            
            pokemon_joueur1 = joueur1.recuperer_pokemon(i + 1)
            pokemon_joueur2 = joueur2.recuperer_pokemon(i + 1)

            while not pokemon_joueur1.est_ko() and not pokemon_joueur2.est_ko():
                attaque_joueur1 = joueur1.choisir_attaque(pokemon_joueur1)
                attaque_joueur2 = joueur2.choisir_attaque(pokemon_joueur2)

                if pokemon_joueur1.vitesse > pokemon_joueur2.vitesse:
                    pokemon_joueur1.attaquer(pokemon_joueur2, attaque_joueur1)
                    if not pokemon_joueur2.est_ko():
                        pokemon_joueur2.attaquer(pokemon_joueur1, attaque_joueur2)
                else:
                    pokemon_joueur2.attaquer(pokemon_joueur1, attaque_joueur2)
                    if not pokemon_joueur1.est_ko():
                        pokemon_joueur1.attaquer(pokemon_joueur2, attaque_joueur1)

                joueur.afficher_combat(pokemon_joueur1,pokemon_joueur2)
                    
        console.print("[bold]Résumé du combat :[/bold]", style="yellow")
        for i in range(3):
            pokemon_joueur1 = joueur1.recuperer_pokemon(i + 1)
            pokemon_joueur2 = joueur2.recuperer_pokemon(i + 1)
            if pokemon_joueur1.est_ko():
                console.print(f"[cyan]{joueur2.nom}[/cyan] remporte le combat avec [red]{pokemon_joueur2.nom}[/red] !")
                joueur2.manche_gagnee += 1
            elif pokemon_joueur2.est_ko():
                console.print(f"[cyan]{joueur1.nom}[/cyan] remporte le combat avec [red]{pokemon_joueur1.nom}[/red] !")
                joueur1.manche_gagnee += 1
            else:
                console.print("Match nul !", style="cyan")

        if joueur1.manche_gagnee >= 2:
            round_text = f"""
            ⭕️═════════════════════════════════════════════════⭕️
                          {joueur1.nom} remporte le jeu !          
            ⭕️═════════════════════════════════════════════════⭕️
            """
            print(round_text)
        elif joueur2.manche_gagnee >= 2:
            round_text = f"""
            ⭕️═════════════════════════════════════════════════⭕️
                          {joueur2.nom} remporte le jeu !          
            ⭕️═════════════════════════════════════════════════⭕️
            """
            print(round_text)
        else:
            round_text = f"""
            ⭕️═════════════════════════════════════════════════⭕️
                                 Match null !          
            ⭕️═════════════════════════════════════════════════⭕️
            """
            print(round_text)
            
        for joueur in self.joueurs:
            joueur.argent = 10

        console.print(f"Voulez-vous [yellow]rejouer[/yellow] ? (o/n): ")
        rejouer = input()
        if rejouer.lower() == 'o':
            self.jouer()
        else:
            print("Merci d'avoir joué !")
            return

jeu = Jeu()
jeu.jouer()
