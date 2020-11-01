'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9,807 # in m/s^2 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1,62 #in m/s^2 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #in m/s #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #in m/s #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''
def egikphs(eg):
    '''
    Převod gravitace Země z m/s^2 na km/h^2
    '''
    return eg * 12960

def mgikphs(mg):
    '''
    Převod gravitace měsíce z m/s^2 na km/h^2
    '''
    return mg * 12960

def solikph(sol):
    '''
    Převod rychlosti světla na km/h
    '''
    return sol * 3,6

def sosikph(sos):
    '''
    Převod rychlosti zvuku na km/h
    '''
    return sos * 3, 6

