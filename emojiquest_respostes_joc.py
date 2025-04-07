import random
from typing import Any, Dict, TypedDict, Optional
from emojiquest_core import Escena, context, Opcio

class Resposta(TypedDict):
    text: str
    seguent_escena: Optional[Escena]

def resposta_bosc_llop_amic() -> Resposta:
    context.amic_llop = True
    return {
        "text": "🤝 Intentes fer-te amic del llop! Sorprenentment, el llop accepta i es converteix en el teu aliat. ❤️",
        "seguent_escena": Escena.CASTELL
    }

def resposta_bosc_llop_lluita() -> Resposta:
    if random.random() < 0.5:
        return {
            "text": "⚔️ Lluites contra el llop! Guanyes!",
            "seguent_escena": Escena.RIU_CORRENT
        }
    else:
        return {
            "text": "🐺 El llop et supera! Hauràs de fugir... 🏃💨",
            "seguent_escena": Escena.CRUILLA
        }

def resposta_muntanya_roca_ajuda() -> Resposta:
    if random.random() < 0.5:
        return {
            "text": "🤝 Demanes ajuda i un grup de viatgers t'ajuda a moure la roca. Junts, aconseguiu passar! 💪",
            "seguent_escena": Escena.CASTELL
        }
    else:
        return {
            "text": "🤝 Demanes ajuda, però ningú apareix. Hauràs de buscar una altra manera de passar... ❔",
            "seguent_escena": Escena.MUNTANYA_ROCA
        }

def resposta_riu_corrent_amic() -> Resposta:
    if random.random() > 0.5:
        return {
            "text": "🤝 Et deixes portar pel corrent i et condueix a un lloc segur. ✨",
            "seguent_escena": Escena.CRUILLA
        }
    else:
        return {
            "text": "🌊 El corrent t’arrossega cap a una cascada! Tens sort i aconsegueixes agafar-te a una branca. 😨",
            "seguent_escena": Escena.MUNTANYA_ROCA
        }

def resposta_castell_no_clau() -> Resposta:
    if context.amic_llop:
        return {
            "text": "🤝 El llop et troba la clau! Ara pots entrar al castell amb ella! 🔑🎉",
            "seguent_escena": Escena.CASTELL_INTERIOR
        }
    else:
        return {
            "text": " ❌ No tens la clau. Et perds en el bosc per sempre... 🌫️👻",
            "seguent_escena": None
        }

def resposta_cruilla_bosc() -> Resposta:
    return {
        "text": "🦊 Has triat el camí del bosc fosc! 🌲",
        "seguent_escena": Escena.BOSC_LLOP
    }

def resposta_cruilla_muntanya() -> Resposta:
    return {
        "text": "⛰️ Has triat el camí de la muntanya!",
        "seguent_escena": Escena.MUNTANYA_ROCA
    }

def resposta_cruilla_riu() -> Resposta:
    return {
        "text": "🌊 Has triat el camí del riu!",
        "seguent_escena": Escena.RIU_CORRENT
    }

def resposta_bosc_llop_fugir() -> Resposta:
    return {
        "text": "🏃 Fugues ràpidament i et salves!",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_bosc_llop_estrategia() -> Resposta:
    return {
        "text": "🧠 Penses una estratègia i enganyes el llop per escapar!",
        "seguent_escena": Escena.RIU_CORRENT
    }

def resposta_bosc_llop_tornar_cruilla() -> Resposta:
    return {
        "text": "🔄 Tornant a la cruïlla inicial...",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_muntanya_roca_trencar() -> Resposta:
    return {
        "text": "⚔️ Lluites contra la roca... però no pots moure-la!",
        "seguent_escena": Escena.MUNTANYA_ROCA
    }

def resposta_muntanya_roca_buscar_cami() -> Resposta:
    return {
        "text": "🏃 Corres i trobes un camí secundari que et porta a un altre lloc!",
        "seguent_escena": Escena.RIU_CORRENT
    }

def resposta_muntanya_roca_pensar() -> Resposta:
    return {
        "text": "🧠 Penses en una manera d'escalatar la roca i passes! 🪜",
        "seguent_escena": Escena.RIU_CORRENT
    }

def resposta_muntanya_roca_tornar_cruilla() -> Resposta:
    return {
        "text": "🔄 Tornant a la cruïlla inicial...",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_riu_corrent_lluitar() -> Resposta:
    return {
        "text": "⚔️ Intentes lluitar contra el corrent 🌊💦... *splash!* És massa fort! Necessites una altra estratègia!",
        "seguent_escena": Escena.RIU_CORRENT
    }

def resposta_riu_corrent_buscar_pont() -> Resposta:
    return {
        "text": "🏃 Fugues cap a un pont a prop i el creues amb seguretat! ",
        "seguent_escena": Escena.MUNTANYA_ROCA
    }

def resposta_riu_corrent_pensar() -> Resposta:
    return {
        "text": "🧠 Utilitzes una corda per creuar el riu i salvar-te! 💡",
        "seguent_escena": Escena.CASTELL
    }

def resposta_riu_corrent_tornar_cruilla() -> Resposta:
    return {
        "text": "🔄 Tornant a la cruïlla inicial...",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_castell_si_clau() -> Resposta:
    return {
        "text": "✅ Has trobat la clau! Entras al castell.\n🎉 ",
        "seguent_escena": Escena.CASTELL_INTERIOR
    }

def resposta_castell_explorar() -> Resposta:
    return {
        "text": "✅ Has descobert un túnel secret! Entras al castell.\n🎉 ",
        "seguent_escena": Escena.CASTELL_INTERIOR
    }

def resposta_explorar(escena: Escena) -> Resposta:
    if context.te_clau is True:
        if random.random() > 0.5:
            return {
                "text": "Explores els voltants i trobes una flor rara! 🌸",
                "seguent_escena": escena
            }
        else:
            return {
                "text": "Explores els voltants i trobes alguns bolets comestibles! 🍄",
                "seguent_escena": escena
            }
    context.te_clau = True
    return {
        "text": "✅ Explores els voltants i trobes una clau misteriosa! 🔑",
        "seguent_escena": escena
    }

def tornar_a_cruilla() -> Resposta:
    return {
        "text": "Tornes a la cruïlla inicial... avui tens ganes de caminar. 🏃",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_castell_interior_tresor() -> Resposta:
    return {
        "text": "⚠️ Era una trampa! 😱 S'activa una trampa màgica que et transporta al començament 🪄",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_castell_interior_passadis() -> Resposta:
    return {
        "text": "🔦 Trobes una biblioteca secreta amb llibres extravagants! 📚",
        "seguent_escena": Escena.CASTELL_BIBLIOTECA
    }

def resposta_castell_interior_guardia() -> Resposta:
    return {
        "text": "👣 Passes amb èxit! Arribes al vertader tresor 🏆.\n🎉 Felicitats! Has trobat el tresor i et converteixes en una llegenda! 👑💰",
        "seguent_escena": None
    }

def resposta_castell_interior_sortir() -> Resposta:
    return {
        "text": "🚪 Tornes a l'entrada del castell",
        "seguent_escena": Escena.CASTELL
    }

def resposta_castell_biblioteca_guardia() -> Resposta:
    return {
        "text": "🧙  El guardià dorm com un tronc i no reacciona. 😔",
        "seguent_escena": Escena.CASTELL_BIBLIOTECA
    }

def resposta_castell_biblioteca_explorar() -> Resposta:
    return {
        "text": "🔍 Explores els voltants i trobes un llibre màgic! 📚",
        "seguent_escena": Escena.CASTELL_TRESOR
    }

def resposta_castell_biblioteca_tornar() -> Resposta:
    return {
        "text": "🚪 Tornes a l'entrada del castell",
        "seguent_escena": Escena.CASTELL_INTERIOR
    }

def resposta_castell_tresor_agafar() -> Resposta:
    return {
        "text": "⚠️ Era una trampa! 😱 S'activa una trampa màgica que et transporta al començament 🪄",
        "seguent_escena": Escena.CRUILLA
    }

def resposta_castell_tresor_explorar() -> Resposta:
    return {
        "text": "🔍 Explores els voltants i trobes un llibre màgic! 📚",
        "seguent_escena": Escena.CASTELL_TRESOR
    }

def resposta_castell_tresor_tornar() -> Resposta:
    return {
        "text": "🚪 Tornes a l'entrada del castell",
        "seguent_escena": Escena.CASTELL_INTERIOR
    }