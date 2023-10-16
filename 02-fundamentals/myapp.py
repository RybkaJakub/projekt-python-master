import physics

earth_time = physics.free_fall_time(100)  # Předpokládáme pád ze 100 metrů
moon_time = physics.moon_free_fall_time(100)  # Předpokládáme pád ze 100 metrů

print(f"Doba pádu na Zemi: {earth_time} sekund")
print(f"Doba pádu na Měsíci: {moon_time} sekund")
