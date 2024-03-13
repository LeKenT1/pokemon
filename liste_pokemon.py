from pokemon import Pokemon
from attaque import Attaque

# Attaques pour Bulbizarre
attaque_charge = Attaque("Charge", "Normal", "physique", 100, 40, 5)
attaque_tranchHerbe = Attaque("Tranch'Herbe", "Plante", "physique", 95, 45, 1)

# Attaques pour Salamèche
attaque_griffe = Attaque("Griffe", "Normal", "physique", 100, 40, 5)
attaque_flammeche = Attaque("Flammeche", "Feu", "spéciale", 100, 40, 1)

# Attaques pour Carapuce
attaque_charge = Attaque("Charge", "Normal", "physique", 100, 40, 5)
attaque_pistoletO = Attaque("Pistolet à O", "Eau", "spéciale", 100, 40, 1)

# Attaques pour Pikachu
attaque_ruse = Attaque("Ruse", "Normal", "physique", 100, 30, 5)
attaque_tonnerre = Attaque("Tonnerre", "Electrique", "spéciale", 100, 60, 1)

# Attaques pour Ectoplasma
attaque_choc_venin = Attaque("Choc Venin", "Poison", "spéciale", 100, 65, 5)
attaque_ball_ombre = Attaque("Ball'Ombre", "Spectre", "spéciale", 100, 80, 1)

# Attaques pour Arcanin
attaque_morsure = Attaque("Morsure", "Tenebres", "physique", 100, 60, 5)
attaque_crocs_feu = Attaque("Crocs Feu", "Feu", "physique", 95, 65, 1)

# Attaques pour Mewtwo
attaque_meteores= Attaque("Météores", "Normal", "spéciale", 100, 60, 5)
attaque_psyko = Attaque("Psyko", "Psy", "spéciale", 100, 90, 1)

# Attaques pour Sulfura
attaque_lame_air = Attaque("Lame d'Air", "Vol", "spéciale", 95, 75, 5)
attaque_flamme_ultime = Attaque("Flamme Ultime", "Feu", "spéciale", 100, 135, 1)

# Attaques pour Artikodin
attaque_vent_violent = Attaque("Vent Violent", "Vol", "speciale", 100, 110, 5)
attaque_blizzard = Attaque("Blizzard", "Glace", "speciale", 70, 110, 1)

# Attaques pour Dracaufeu
attaque_draco_griffe = Attaque("Draco-Griffe", "Dragon", "physique", 100, 80, 5)
attaque_boutefeu = Attaque("Boutefeu", "Feu", "spéciale", 100, 120, 1)

liste_pokemon = [
    Pokemon("Bulbizarre", 1, ["Plante", "Poison"], 10, 45, 60, 65, 40, 60, 45, [attaque_charge, attaque_tranchHerbe]),
    Pokemon("Salamèche", 1, ["Feu"], 10, 60, 40, 50, 65, 40, 50, [attaque_charge, attaque_flammeche]),
    Pokemon("Carapuce", 1, ["Eau"], 10, 50, 55, 50, 45, 55, 40, [attaque_charge, attaque_pistoletO]),
    Pokemon("Pikachu", 2, ["Électrique"], 30, 50, 40, 40, 90, 40, 50, [attaque_ruse, attaque_tonnerre]),
    Pokemon("Ectoplasma", 3, ["Spectre", "Poison"], 50, 60, 65, 60, 130, 75, 110, [attaque_choc_venin, attaque_ball_ombre]),
    Pokemon("Arcanin", 3, ["Feu"], 50, 90, 110, 80, 100, 80, 95, [attaque_morsure, attaque_crocs_feu]),
    Pokemon("Mewtwo", 4, ["Psy"], 70, 80, 70, 90, 100, 70, 80, [attaque_meteores, attaque_psyko]),
    Pokemon("Sulfura", 5, ["Eau", "Vol"], 90, 90, 100, 90, 125, 85, 90, [attaque_lame_air, attaque_flamme_ultime]),
    Pokemon("Artikodin", 5, ["Glace", "Vol"], 90, 80, 85, 100, 95, 125, 85, [attaque_vent_violent, attaque_blizzard]),
    Pokemon("Dracaufeu", 6, ["Feu", "Vol"], 100, 70, 65, 70, 80, 80, 70, [attaque_draco_griffe, attaque_boutefeu])
]