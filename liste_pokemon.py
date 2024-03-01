from pokemon import Pokemon
from attaque import Attaque

attaque_eclair = Attaque("Éclair", "Électrique", "physique", 100, 50, 20)
attaque_queue_de_fer = Attaque("Queue de Fer", "Acier", "physique", 90, 60, 15)
attaque_vive_attaque = Attaque("Vive-Attaque", "Normal", "physique", 100, 40, 30)
attaque_canon_graine = Attaque("Canon Graine", "Plante", "physique", 100, 80, 10)
attaque_lance_flamme = Attaque("Lance-Flamme", "Feu", "spéciale", 90, 90, 15)
attaque_hydrocanon = Attaque("Hydrocanon", "Eau", "spéciale", 80, 110, 5)

liste_pokemon = [
    Pokemon("Pikachu", 100, ["Électrique"], 60, 50, 40, 40, 90, 40, 50, [attaque_eclair, attaque_vive_attaque]),
    Pokemon("Bulbizarre", 120, ["Plante", "Poison"], 55, 45, 60, 65, 40, 60, 45, [attaque_vive_attaque, attaque_canon_graine]),
    Pokemon("Salamèche", 110, ["Feu"], 50, 60, 40, 50, 65, 40, 50, [attaque_lance_flamme, attaque_eclair]),
    Pokemon("Carapuce", 130, ["Eau"], 40, 50, 55, 50, 45, 55, 40, [attaque_hydrocanon, attaque_vive_attaque]),
    Pokemon("Dracaufeu", 150, ["Feu", "Vol"], 80, 70, 65, 70, 80, 80, 70, [attaque_lance_flamme, attaque_hydrocanon]),
    Pokemon("Mewtwo", 180, ["Psy"], 90, 80, 70, 90, 100, 70, 80, [attaque_eclair, attaque_lance_flamme]),
    Pokemon("Articuno", 170, ["Glace", "Vol"], 80, 70, 80, 95, 85, 85, 80, [attaque_vive_attaque, attaque_queue_de_fer]),
    Pokemon("Zapdos", 160, ["Électrique", "Vol"], 75, 80, 70, 80, 100, 70, 80, [attaque_eclair, attaque_lance_flamme]),
    Pokemon("Moltres", 165, ["Feu", "Vol"], 90, 85, 70, 75, 90, 70, 85, [attaque_lance_flamme, attaque_vive_attaque]),
    Pokemon("Gyarados", 140, ["Eau", "Vol"], 80, 95, 100, 70, 85, 80, 95, [attaque_hydrocanon, attaque_queue_de_fer])
]
