from emojiquest_respostes_joc import (
    resposta_bosc_llop_amic,
    resposta_bosc_llop_lluita,
    resposta_bosc_llop_fugir,
    resposta_bosc_llop_estrategia,
    resposta_bosc_llop_tornar_cruilla,
    resposta_muntanya_roca_trencar,
    resposta_muntanya_roca_buscar_cami,
    resposta_muntanya_roca_pensar,
    resposta_muntanya_roca_tornar_cruilla,
    resposta_riu_corrent_lluitar,
    resposta_riu_corrent_buscar_pont,
    resposta_riu_corrent_pensar,
    resposta_riu_corrent_amic,
    resposta_castell_si_clau,
    resposta_castell_no_clau,
    resposta_cruilla_bosc,
    resposta_cruilla_muntanya,
    resposta_cruilla_riu,
    resposta_muntanya_roca_ajuda,
    resposta_riu_corrent_tornar_cruilla
)

import time
from typing import Optional, Dict, List, Any

from emojiquest_core import Escena, Opcio, context
from emojiquest_escenes_joc import escenes

# Funció per obtenir una decisió de l'usuari (retorna l'objecte Opcio seleccionat)
def triar_accio(opcions: List[Opcio]) -> Optional[Opcio]:
    while True:
        try:
            # Mostrem només els emojis de les opcions que són vàlides
            opcions_valides = [opcio for opcio in opcions]
            if not opcions_valides:
                print("No hi ha opcions vàlides disponibles. El joc ha acabat.")
                return None

            entrada = input(f"Tria una opció (per índex o emoji {', '.join([opcio.emoji for opcio in opcions_valides])}): ")

            # Comprovem si s'ha introduït un emoji vàlid
            for opcio in opcions_valides:
                if entrada == opcio.emoji:
                    return opcio

            # Comprovem si s'ha introduït un índex vàlid
            try:
                num = int(entrada)
                for opcio in opcions_valides:
                    if opcio.valor_int == num:
                        return opcio
            except ValueError:
                pass

            print("Opció no vàlida o no disponible. Torna a intentar.")
        except Exception as e:
            print(f"Error: {e}. Torna a intentar.")

# Funció per mostrar les opcions disponibles
def mostrar_opcions(opcions: List[Opcio]) -> None:
    for opcio in opcions:
        print(f"{opcio.valor_int}️⃣ {opcio.emoji} {opcio.text}")
    print()

# Funció per gestionar una escena
def gestionar_escena(escena_id: Escena, context: Dict[str, Any] = {}) -> Optional[Escena]:
    if escena_id not in escenes:
        print(f"Error: L'escena {escena_id} no existeix.")
        return None

    escena = escenes[escena_id]
    print(escena["descripcio"])

    # Mostrar opcions amb la funció refactoritzada
    mostrar_opcions(escena["opcions"])

    # Processar la selecció
    opcio_seleccionada = triar_accio(escena["opcions"])
    if opcio_seleccionada is None:
        return None

    # Executar la funció de resposta si existeix
    if "respostes" in escena and opcio_seleccionada.valor_int in escena["respostes"]:
        resposta = escena["respostes"][opcio_seleccionada.valor_int]
        if isinstance(resposta, str):
            print(resposta, '\n')
            return escena.get("seguent_escena")
        elif callable(resposta):
            resposta = resposta()
            if isinstance(resposta, dict):
                print(resposta["text"], '\n')
                return resposta.get("seguent_escena")

    print()
    print('\n')
    # Si no hi ha resposta específica, retornem la següent escena genèrica
    return escena.get("seguent_escena")

# Funció principal del joc
def aventura_emojiquest():
    print("🌲 Benvingut a EmojiQuest! Preparat per l'aventura? 🏰\n")
    time.sleep(1)

    escena_actual = Escena.CRUILLA
    context = {}  # Un diccionari per emmagatzemar l'estat del joc

    while escena_actual:
        escena_actual = gestionar_escena(escena_actual, context)

    tornar = input("\nVols tornar a jugar? (s/n): ").strip().lower()
    if tornar == "s":
        aventura_emojiquest()
    else:
        print("Gràcies per jugar a EmojiQuest! 🎮🌟")

# Iniciar el joc
if __name__ == "__main__":
    aventura_emojiquest()
    # Si el joc es tanca, es pot afegir un missatge de comiat aquí
    #print("Gràcies per jugar a EmojiQuest! 🎮🌟")