import time
from typing import Optional, Dict, List, Any

from emojiquest_core import Context, Escena, Opcio, context
from emojiquest_escenes_joc import escenes

delay=1

# Funció per obtenir una decisió de l'usuari (retorna l'objecte Opcio seleccionat)
def triar_accio(opcions: List[Opcio]) -> Optional[Opcio]:
    while True:
        try:
            # Mostrem només els emojis de les opcions que són vàlides
            opcions_valides = [opcio for opcio in opcions]
            if not opcions_valides:
                print("No hi ha opcions vàlides disponibles. El joc ha acabat.")
                return None

            entrada = input(f"Tria una opció (per índex o emoji {', '.join([opcio.emoji.lstrip().rstrip() for opcio in opcions_valides])}): ").lstrip().rstrip()

            # Comprovem si s'ha introduït un emoji vàlid
            for opcio in opcions_valides:
                if entrada == opcio.emoji.lstrip().rstrip():
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
    time.sleep(delay)
    for opcio in opcions:
        print(f"{opcio.valor_int}️ {opcio.emoji} {opcio.text}")
    print()

# Funció per gestionar una escena
def gestionar_escena() -> Optional[Escena] | str:
    if context.escena_actual not in escenes:
        print(f"Error: L'escena {context.escena_actual} no existeix.")
        return None

    escena = escenes[context.escena_actual]

    if len(context.escenes_anteriors) and context.escena_actual != Escena.CRUILLA:
        time.sleep(delay)
        print("\n", "Segueixes el teu camí...", "\n")
        time.sleep(delay)
    elif(len(context.escenes_anteriors) and context.escena_actual == Escena.CRUILLA):
        time.sleep(delay)
        print("")

    if(context.amic_llop is True):
        print("El teu aliat llop et fa companyia. 🐺❤️\n")
    print(escena.descripcio, "\n")

    opcions = [opcio for opcio in escena.opcions if opcio is not None]
    # Mostrar opcions amb la funció refactoritzada
    mostrar_opcions(opcions)

    # Processar la selecció
    opcio_seleccionada = triar_accio(opcions)
    if opcio_seleccionada is None:
        return None

    # Executar la funció de resposta si existeix
    if escena.respostes and opcio_seleccionada.valor_int in escena.respostes:
        resposta = escena.respostes[opcio_seleccionada.valor_int]
        # Si la resposta és un diccionari, actualitzem l'estat del joc
        if isinstance(resposta, str):
            print(resposta)
            return resposta
        # Si la resposta és una funció, l'executem
        elif callable(resposta):
            resposta = resposta()
            if isinstance(resposta, dict):
                nova_escena_actual = resposta.get("seguent_escena", "\n")
                print(resposta.get("text"))
                if isinstance(nova_escena_actual, Escena):
                    if (context.escena_actual == nova_escena_actual or nova_escena_actual in context.escenes_anteriors) and nova_escena_actual != Escena.CRUILLA:
                        print(nova_escena_actual)
                        nova_escena_actual = Escena.CASTELL
                else:
                    return None

    # Si no hi ha resposta específica, retornem la següent escena genèrica
    context.escena_actual = nova_escena_actual

    # Afegir l'escena actual a la llista d'escenes anteriors
    context.escenes_anteriors.append(context.escena_actual)

    return context.escena_actual

# Funció principal del joc
def aventura_emojiquest():
    print("🌲 Benvingut a EmojiQuest! Preparat per l'aventura? 🏰\n")
    time.sleep(1)

    init_context()

    #import pdb; pdb.set_trace()  # Aquí s'activa la depuració

    while True:
        if not gestionar_escena(): break

    tornar = input("\nVols tornar a jugar? (s/n): ").strip().lower()
    if tornar == "s":
        aventura_emojiquest()
    else:
        print("Gràcies per jugar a EmojiQuest! 🎮🌟")

def init_context():
    global context
    if context:
        context.reiniciar()  # Reiniciem el context del joc
    else:
        context = Context()

# Iniciar el joc
if __name__ == "__main__":
    aventura_emojiquest()
    # Si el joc es tanca, es pot afegir un missatge de comiat aquí
    #print("Gràcies per jugar a EmojiQuest! 🎮🌟")