# Estat global (context) del joc
from enum import Enum, auto

context = {
    "amic_llop": False,   # Inicia amb el llop com a enemic
    "te_clau": False      # Inicia sense la clau
}

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