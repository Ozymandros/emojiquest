import time
from typing import Optional, Dict, List, Union, Callable, Any

from emojiquest_core import Context, Escena, Opcio, context
from emojiquest_escenes_joc import escenes

# Constants
DEFAULT_DELAY = 1
PROMPT_OPCIONS = "Tria una opció (per índex o emoji {0}): "
MISSATGE_NO_OPCIONS = "No hi ha opcions vàlides disponibles. El joc ha acabat."
MISSATGE_OPCIO_INVALIDA = "Opció no vàlida o no disponible. Torna a intentar."
MISSATGE_CONTINUACIO = "Segueixes el teu camí..."
MISSATGE_LLOP_ALIAT = "El teu aliat llop et fa companyia. 🐺❤️"
MISSATGE_BENVINGUDA = "🌲 Benvingut a EmojiQuest! Preparat per l'aventura? 🏰"
MISSATGE_TORNAR_JUGAR = "Vols tornar a jugar? (s/n): "
MISSATGE_COMIAT = "Gràcies per jugar a EmojiQuest! 🎮🌟"

class EmojiQuestGame:
    def __init__(self, delay: int = DEFAULT_DELAY):
        self.delay = delay
        self.context = Context()

    def triar_accio(self, opcions: List[Opcio]) -> Optional[Opcio]:
        """
        Permet a l'usuari triar una acció d'entre les opcions disponibles.
        Retorna l'opció seleccionada o None si no hi ha opcions vàlides.
        """
        opcions_valides = opcions
        if not opcions_valides:
            print(MISSATGE_NO_OPCIONS)
            return None

        emojis_text = ', '.join([opcio.emoji.strip() for opcio in opcions_valides])
        
        while True:
            try:
                entrada = input(PROMPT_OPCIONS.format(emojis_text)).strip()

                if entrada is None:
                    return None
                
                # Comprovar per emoji
                for opcio in opcions_valides:
                    if entrada == opcio.emoji.strip():
                        return opcio
                
                # Comprovar per índex
                try:
                    num = int(entrada)
                    for opcio in opcions_valides:
                        if opcio.valor_int == num:
                            return opcio
                except ValueError:
                    pass
                
                print(MISSATGE_OPCIO_INVALIDA)
            except Exception as e:
                print(f"Error: {e}. Torna a intentar.")

    def mostrar_opcions(self, opcions: List[Opcio]) -> None:
        """Mostra les opcions disponibles a l'usuari."""
        time.sleep(self.delay)
        for opcio in opcions:
            print(f"{opcio.valor_int}️ {opcio.emoji} {opcio.text}")
        print()

    def processa_resposta(self, escena: Any, opcio_seleccionada: Opcio) -> Union[Escena, str, None]:
        """Processa la resposta a una opció seleccionada i retorna la següent escena."""
        if escena.respostes and opcio_seleccionada.valor_int in escena.respostes:
            resposta = escena.respostes[opcio_seleccionada.valor_int]
            
            if isinstance(resposta, str):
                print(resposta)
                return resposta
            elif callable(resposta):
                resultat = resposta()
                if isinstance(resultat, dict):
                    nova_escena = resultat.get("seguent_escena", None)
                    print(resultat.get("text", ""))
                    
                    if isinstance(nova_escena, Escena):
                        if ((self.context.escena_actual == nova_escena or 
                            nova_escena in self.context.escenes_anteriors) and 
                            nova_escena != Escena.CRUILLA):
                            return Escena.CASTELL
                        return nova_escena
        return None

    def gestionar_escena(self) -> Optional[Union[Escena, str]]:
        """Gestiona una escena del joc, mostrant descripcions i processant opcions."""
        if self.context.escena_actual not in escenes:
            print(f"Error: L'escena {self.context.escena_actual} no existeix.")
            return None

        escena = escenes[self.context.escena_actual]

        # Mostrar missatges de context
        self._mostrar_context_escena()
        
        # Mostrar descripció
        print(escena.descripcio, "\n")

        # Mostrar opcions
        opcions = [opcio for opcio in escena.opcions if opcio is not None]
        self.mostrar_opcions(opcions)

        # Processar selecció
        opcio_seleccionada = self.triar_accio(opcions)
        if opcio_seleccionada is None:
            return None

        # Processar resposta i obtenir següent escena
        nova_escena = self.processa_resposta(escena, opcio_seleccionada)

        # Si no hi ha resposta específica, continuar amb l'escena actual
        if nova_escena is None:
            return None
        
        # Actualitzar l'escena actual i afegir-la a la història
        if isinstance(nova_escena, Escena):
            self.context.escena_actual = nova_escena
            self.context.escenes_anteriors.append(self.context.escena_actual)
            
        return nova_escena

    def _mostrar_context_escena(self):
        """Mostra missatges contextuals abans de l'escena actual."""
        if len(self.context.escenes_anteriors):
            if self.context.escena_actual != Escena.CRUILLA:
                time.sleep(self.delay)
                print("\n", MISSATGE_CONTINUACIO, "\n")
                time.sleep(self.delay)
            else:
                time.sleep(self.delay)
                print("")

        if self.context.amic_llop is True:
            print(f"{MISSATGE_LLOP_ALIAT}\n")

    def jugar(self):
        """Inicia i controla el flux principal del joc."""
        print(f"{MISSATGE_BENVINGUDA}\n")
        time.sleep(1)

        self.context.reiniciar()

        while True:
            if not self.gestionar_escena():
                break

        tornar = input(f"\n{MISSATGE_TORNAR_JUGAR}").strip().lower()
        if tornar == "s":
            self.jugar()
        else:
            print(MISSATGE_COMIAT)

# Funció principal
def aventura_emojiquest():
    joc = EmojiQuestGame()
    joc.jugar()

# Iniciar el joc
if __name__ == "__main__":
    aventura_emojiquest()