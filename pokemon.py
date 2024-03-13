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
        # Calculer les dégâts
        degats = self.calculer_degats(attaque_utilisee, pokemon_cible)

        # Appliquer les dégâts à la cible
        pokemon_cible.pv -= degats

        # Afficher le résultat de l'attaque
        print(f"{self.nom} utilise {attaque_utilisee.nom} et inflige {round(degats, 1)} dégâts à {pokemon_cible.nom}!")

    def calculer_degats(self, attaque, pokemon_cible):
        # Calculer le coefficient multiplicateur (CM)
        coef_multiplicateur = self.calculer_coef_multiplicateur(attaque)

        # Calculer les dégâts selon la formule donnée
        degats = ((((self.niveau * 0.4 + 2) * self.attaque * attaque.puissance) / (pokemon_cible.defense * 50)) + 2) * coef_multiplicateur

        # Retourner les dégâts calculés
        return degats

    def calculer_coef_multiplicateur(self, attaque):
        # Calculer le coefficient STAB
        coef_stab = 1.5 if attaque.type_attaque in self.types else 1

        # Calculer le coefficient de précision
        coef_precision = attaque.precision / 100

        # Calculer le coefficient multiplicateur total
        coef_multiplicateur = coef_stab * coef_precision

        # Retourner le coefficient multiplicateur total
        return coef_multiplicateur

    def est_ko(self):
        return self.pv <= 0

    def afficher_attaques(self):
        print(f"Les attaques de {self.nom}:")
        for attaque in self.attaques:
            print(f"- {attaque.nom}")

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Types: {', '.join(self.types)}")
        print(f"PV: {self.pv}")
        print(f"Niveau: {self.niveau}")
        print(f"Attaque: {self.attaque}")
        print(f"Attaque Spéciale: {self.attaque_speciale}")
        print(f"Défense: {self.defense}")
        print(f"Défense Spéciale: {self.defense_speciale}")
        print(f"Vitesse: {self.vitesse}")

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
