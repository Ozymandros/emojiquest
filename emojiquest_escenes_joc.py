from emojiquest_respostes_joc import *
from emojiquest_opcions import *

from emojiquest_core import Escena
from dataclasses import dataclass
from typing import Callable, Dict, List, Union

@dataclass
class EscenaData:
    descripcio: str
    opcions: List[Opcio]
    respostes: Dict[int, Callable[[], Resposta] | Resposta]

escenes: Dict[Escena, EscenaData] = {
    Escena.CRUILLA: EscenaData(
        descripcio="🏞️  T'has trobat davant de tres camins. Quin camí tries?",
        opcions=[
            Opcions.Cruilla.BOSC,
            Opcions.Cruilla.MUNTANYA,
            Opcions.Cruilla.RIU,
            Opcions.Cruilla.EXPLORAR
        ],
        respostes={
            1: resposta_cruilla_bosc,
            2: resposta_cruilla_muntanya,
            3: resposta_cruilla_riu,
            4: lambda : resposta_explorar(Escena.CRUILLA)
        }
    ),
    Escena.BOSC_LLOP: EscenaData(
        descripcio="⚠️ Mentre avances pel bosc espès i silenciós 🌳, notes uns ulls brillants entre els matolls... Un llop famolenc 🐺 t’observa atentament, amb les dents ensenyades i una postura amenaçadora 😱. Sents la tensió a l’aire. \n¿Com vols reaccionar?",
        opcions=[
            Opcions.Bosc.LLUITAR,
            Opcions.Bosc.FUGIR,
            Opcions.Bosc.ESTRATEGIA,
            Opcions.Bosc.AMIC_LLOP,
            Opcions.Bosc.TORNAR_CRUILLA
        ],
        respostes={
            1: resposta_bosc_llop_lluita,
            2: resposta_bosc_llop_fugir,
            3: resposta_bosc_llop_estrategia,
            4: resposta_bosc_llop_amic,
            5: resposta_bosc_llop_tornar_cruilla
        }
    ),
    Escena.MUNTANYA_ROCA: EscenaData(
        descripcio="⚠️ Després d’una llarga pujada per un sender costerut ⛰️, t’adones que una roca enorme 🪨 ha caigut recentment i bloqueja completament el pas 🤔. No sembla fàcil de moure ni d’esquivar. El vent bufa fort i la llum comença a minvar. \n¿Com vols reaccionar?",        
        opcions=[
            Opcions.Muntanya.TRENCAR_ROCA,
            Opcions.Muntanya.BUSCAR_CAMI,
            Opcions.Muntanya.PENSAR,
            Opcions.Muntanya.DEMANAR_AJUDA,
            Opcions.Muntanya.TORNAR_CRUILLA
        ],
        respostes={
            1: resposta_muntanya_roca_trencar,
            2: resposta_muntanya_roca_buscar_cami,
            3: resposta_muntanya_roca_pensar,
            4: resposta_muntanya_roca_ajuda,
            5: resposta_muntanya_roca_tornar_cruilla
        }
    ),
    Escena.RIU_CORRENT: EscenaData(
        descripcio="⚠️ Arribes a un riu de corrent intens 🌊, les aigües bramen i esquitxen amb força contra les roques 😨. No hi ha cap pont a la vista i el corrent sembla massa fort per travessar-lo sense precaució. El temps corre i has de prendre una decisió. \n¿Com vols reaccionar?",
        opcions=[
            Opcions.Riu.LLUITAR_CORRENT,
            Opcions.Riu.BUSCAR_PONT,
            Opcions.Riu.PENSAR_SOLUCIO,
            Opcions.Riu.AMIC_CORRENT,
            Opcions.Riu.TORNAR_CRUILLA
        ],
        respostes={
            1: resposta_riu_corrent_lluitar,
            2: resposta_riu_corrent_buscar_pont,
            3: resposta_riu_corrent_pensar,
            4: resposta_riu_corrent_amic,
            5: tornar_a_cruilla
        }
    ),
    Escena.CASTELL: EscenaData(
        descripcio=("🎉 Has arribat al castell misteriós! 🏰 La porta està tancada.\n"
                    "🔑 Tens la clau per entrar?"),
        opcions=[
            Opcions.Castell.TINC_CLAU,
            Opcions.Castell.NO_TINC_CLAU,
            Opcions.Castell.EXPLORAR,
            Opcions.Bosc.TORNAR_CRUILLA
        ],
        respostes={
            1: resposta_castell_si_clau,
            2: resposta_castell_no_clau,
            3: resposta_castell_explorar,
            4: tornar_a_cruilla
        }
    ),
    Escena.CASTELL_INTERIOR: EscenaData(
        descripcio=(
            "🏰 Dins del castell hi ha:\n"
            "+-----------------------+\n"
            "| 💎 Un tresor brillant |\n"
            "| 🕳️ Un passadís secret |\n"
            "| 😴 Un guardià dormit  |\n"
            "+-----------------------+\n"
            "¿Com vols reaccionar?\n"
        ),
        opcions=[
            Opcions.CastellInterior.AGAFAR_TRESOR,
            Opcions.CastellInterior.EXPLORAR_PASSADIS,
            Opcions.CastellInterior.PASSAR_SILENCI,
            Opcions.CastellInterior.SORTIR_CASTELL
        ],
        respostes={
            1: resposta_castell_interior_tresor,
            2: resposta_castell_interior_passadis,
            3: resposta_castell_interior_guardia,
            4: resposta_castell_interior_sortir
        }
    ),
    Escena.CASTELL_BIBLIOTECA: EscenaData(
        descripcio="📜 La biblioteca està plena de pergamins màgics! 🧙 Com vols reaccionar?",
        opcions=[
            Opcions.Biblioteca.PREGUNTAR_GUARDIA,
            Opcions.Biblioteca.EXPLORAR,
            Opcions.Biblioteca.TORNAR_ENTRADA
        ],
        respostes={
            1: resposta_castell_biblioteca_guardia,
            2: resposta_castell_biblioteca_explorar,
            3: resposta_castell_biblioteca_tornar
        }
    ),
    Escena.CASTELL_TRESOR: EscenaData(
        descripcio="📚 El tresor està ple 💎 i encara no té res... 🤔 Com vols reaccionar?",
        opcions=[
            Opcions.CastellTresor.AGAFAR_TRESOR_FINAL,
            Opcions.CastellTresor.EXPLORAR_TRESOR,
            Opcions.CastellTresor.TORNAR_ENTRADA_TRESOR
        ],
        respostes={
            1: resposta_castell_tresor_agafar,
            2: resposta_castell_tresor_explorar,
            3: resposta_castell_tresor_tornar
        }
    ),
    Escena.CASTELL_JARDI: EscenaData(
        descripcio="🌿 Has entrat en un jardí secret ple de plantes màgiques! 🌸✨",
        opcions=[
            Opcio(1, " 🌸 ", "Recollir una flor màgica"),
            Opcio(2, " 🔙 ", "Tornar al castell")
        ],
        respostes={
            1: {
                "text": "🌸 La flor brillant et dóna energia! +10 punts d'ànim. ✨",
                "seguent_escena": Escena.CASTELL_INTERIOR
            },
            2: {
                "text": "🚪 Tornes a l'interior del castell",
                "seguent_escena": Escena.CASTELL_INTERIOR
            }
        }
    )
}