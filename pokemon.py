from rich.console import Console
from rich.table import Table

class Pokemon:
    def __init__(self, nom, prix, types, pv, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse, attaques):
        self.nom = nom
        self.prix = prix
        self.types = types
        self.pv = pv
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = attaques

    def attaquer(self, pokemon_cible, attaque_utilisee):
        degats = self.calculer_degats(attaque_utilisee, pokemon_cible)
        attaque_utilisee.pp -= 1
        pokemon_cible.pv -= degats

    def calculer_degats(self, attaque, pokemon_cible):
        coef_multiplicateur = self.calculer_coef_multiplicateur(attaque)
        degats = ((((self.niveau * 0.4 + 2) * self.attaque * attaque.puissance) / (pokemon_cible.defense * 50)) + 2) * coef_multiplicateur

        return degats

    def calculer_coef_multiplicateur(self, attaque):
        coef_stab = 1.5 if attaque.type_attaque in self.types else 1
        coef_precision = attaque.precision / 100
        coef_multiplicateur = coef_stab * coef_precision

        return coef_multiplicateur

    def est_ko(self):
        return self.pv <= 0

    def afficher_attaques(self):
        console = Console()

        table = Table(title=f"Attaques de [cyan]{self.nom}[/cyan]:")
        table.add_column("Numéro", style="cyan")
        table.add_column("Attaque", style="magenta")
        table.add_column("Puissance", style="green")
        table.add_column("PP", style="yellow")

        for i, attaque in enumerate(self.attaques, 1):
            pp_text = str(attaque.pp)
            if attaque.pp == 0:
                pp_text = f"[dim]{pp_text}[/dim]"
            table.add_row(str(i), attaque.nom, str(attaque.puissance), pp_text)

        console.print(table)

class Attaque:
    def __init__(self, nom, type_attaque, puissance, pp):
        self.nom = nom
        self.type_attaque = type_attaque
        self.puissance = puissance
        self.pp = pp

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type_attaque}")
        print(f"Puissance: {self.puissance}")
        print(f"Points de Puissance (PP): {self.pp}")
