import random
from armas import armas

roll = random.randint(0, len(armas) - 1)

arma_que_salio = armas[roll]


print(arma_que_salio)

jugador = {
    "ataque_jugador": 13,
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


ataque_jugador_con_bonus = jugador['ataque_jugador'] + jugador['bonus_atk']
defensa_jugador_con_bonus = jugador['defensa_jugador'] + jugador['bonus_def']

defensa_enemigo = 0

ataque_enemigo = 33

daño_turno = ataque_jugador_con_bonus - defensa_enemigo
daño_recibido = ataque_enemigo - defensa_jugador_con_bonus

print(daño_recibido)



