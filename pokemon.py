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
        # Logique pour déterminer les dégâts infligés à pokemon_cible avec attaque_utilisee
        pass

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
