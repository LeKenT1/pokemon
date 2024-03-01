class Attaque:
    def __init__(self, nom, type_attaque, categorie_attaque, precision, puissance, pp):
        self.nom = nom
        self.type_attaque = type_attaque
        self.categorie_attaque = categorie_attaque
        self.precision = precision
        self.puissance = puissance
        self.pp = pp

    def calculer_degats(self, pokemon_attaquant, pokemon_attaque):
        # Calcul du coefficient multiplicateur en prenant en compte le STAB
        coef_stab = 1.5 if self.type_attaque in pokemon_attaquant.types else 1
        
        # Calcul du coefficient multiplicateur de précision
        coef_precision = self.precision / 100.0
        
        # Déterminer si c'est une attaque physique ou spéciale
        if self.categorie_attaque == "physique":
            # Calcul des dégâts pour une attaque physique
            degats = ((((pokemon_attaquant.niveau * 0.4 + 2) * pokemon_attaquant.attaque * self.puissance) / (pokemon_attaque.defense * 50)) + 2) * coef_stab * coef_precision
        elif self.categorie_attaque == "speciale":
            # Calcul des dégâts pour une attaque spéciale
            degats = ((((pokemon_attaquant.niveau * 0.4 + 2) * pokemon_attaquant.attaque_speciale * self.puissance) / (pokemon_attaque.defense_speciale * 50)) + 2) * coef_stab * coef_precision
        else:
            raise ValueError("Catégorie d'attaque invalide.")
        
        return degats

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Type: {self.type_attaque}")
        print(f"Catégorie: {self.categorie_attaque}")
        print(f"Précision: {self.precision}")
        print(f"Puissance: {self.puissance}")
        print(f"Points de Puissance (PP): {self.pp}")
