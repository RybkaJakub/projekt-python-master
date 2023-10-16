'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81  # m/s^2
MOON_GRAVITY = 1.62  # m/s^2
SPEED_OF_LIGHT = 299792458  # m/s
SPEED_OF_SOUND = 343  # m/s (při teplotě 20 °C v suchém vzduchu)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def free_fall_time(distance):
    """Vypočítá dobu pádu volného tělesa na Zemi."""
    time = (2 * distance / EARTH_GRAVITY)**0.5
    return time

def moon_free_fall_time(distance):
    """Vypočítá dobu pádu volného tělesa na Měsícě."""
    time = (2 * distance / MOON_GRAVITY)**0.5
    return time