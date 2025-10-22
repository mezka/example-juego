import random
from armas import armas

roll = random.randint(0, len(armas) - 1)

arma_que_salio = armas[roll]


print(arma_que_salio)

jugador = {
    "ataque_jugador": 11,
    "defensa_jugador": 12,
    "has_arma_equipped": False,
    "bonus_atk": 0,
    "bonus_def": 0
}

def equipar_arma(arma):

    if not jugador['has_arma_equipped']:
        jugador['bonus_atk'] = ataque_arma
        jugador['bonus_def'] = defensa_arma
        jugador['has_arma_equipped'] = True


ataque_jugador = jugador['ataque_jugador'] + jugador['bonus_atk']

daño_turno = ataque_jugador - defensa_enemigo