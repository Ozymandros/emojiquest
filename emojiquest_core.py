from enum import Enum, auto

# Definim un Enum per a les diferents escenes del joc
class Escena(Enum):
    CRUILLA = auto()
    BOSC_LLOP = auto()
    MUNTANYA_ROCA = auto()
    RIU_CORRENT = auto()
    CASTELL = auto()
    CASTELL_INTERIOR = auto()
    CASTELL_BIBLIOTECA = auto()
    CASTELL_TRESOR = auto()

# Classe per emmagatzemar l'índex, l'emoji, la validesa i si ha de terminar el bucle
class Opcio:
    def __init__(self, valor_int: int, emoji: str, text: str):
        self.valor_int = valor_int
        self.emoji = emoji
        self.text = text

class Context:
    def __init__(self, amic_llop = False, te_clau = False, escena_actual = Escena.CRUILLA, escenes_anteriors: list[Escena] = []):
        self.amic_llop = amic_llop  # Inicia amb el llop com a enemic
        self.te_clau = te_clau    # Inicia sense la clau
        self.escena_actual = escena_actual # Inicia amb la crulla
        self.escenes_anteriors = escenes_anteriors # Inicialitza la llista d'escenes anteriors
        self.opcions = [] # Inicialitza la llista d'opcions disponibles

    def afegir_opcio(self, opcio: Opcio):
        self.opcions.append(opcio)

context = Context()  # Inicialitzem el context del joc