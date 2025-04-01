from emojiquest_respostes_joc import *
from emojiquest_opcions import *

from emojiquest_core import Escena, context

escenes = {
    Escena.CRUILLA: {
        "descripcio": "🏞️  T'has trobat davant de tres camins. Quin camí tries?",
        "opcions": [
            OPCIO_BOSC,
            OPCIO_MUNTANYA,
            OPCIO_RIU,
            OPCIO_EXPLORAR
        ],
        "respostes": {
            1: resposta_cruilla_bosc,
            2: resposta_cruilla_muntanya,
            3: resposta_cruilla_riu,
            4: lambda: resposta_explorar(Escena.CRUILLA) 
        }
    },

    Escena.BOSC_LLOP: {
        "descripcio": "⚠️ Et trobes amb un llop famolenc 🐺! Com vols reaccionar?",
        "opcions": [
            OPCIO_LLUITAR,
            OPCIO_FUGIR,
            OPCIO_ESTRATEGIA,
            OPCIO_FER_AMIC,
            OPCIO_TORNAR_CRUILLA
        ],
        "respostes": {
            1: resposta_bosc_llop_lluita,
            2: resposta_bosc_llop_fugir,
            3: resposta_bosc_llop_estrategia,
            4: resposta_bosc_llop_amic,
            5: resposta_bosc_llop_tornar_cruilla
        }
    },

    Escena.MUNTANYA_ROCA: {
        "descripcio": "⚠️ Hi ha una roca enorme 🪨 bloquejant el camí! Com vols reaccionar?",
        "opcions": [
            OPCIO_TRENCAR_ROCA,
            OPCIO_BUSCAR_CAMI,
            OPCIO_PENSAR,
            OPCIO_DEMANAR_AJUDA,
            OPCIO_TORNAR_CRUILLA_MUNTANYA
        ],
        "respostes": {
            1: resposta_muntanya_roca_trencar,
            2: resposta_muntanya_roca_buscar_cami,
            3: resposta_muntanya_roca_pensar,
            4: resposta_muntanya_roca_ajuda,
            5: resposta_muntanya_roca_tornar_cruilla
        }
    },

    Escena.RIU_CORRENT: {
        "descripcio": "⚠️ El corrent del riu és molt fort! 🌊 Com vols reaccionar?",
        "opcions": [
            OPCIO_LLUITAR_CORRENT,
            OPCIO_BUSCAR_PONT,
            OPCIO_PENSAR_SOLUCIO,
            OPCIO_UNIR_CORRENT,
            OPCIO_TORNAR_CRUILLA_RIU
        ],
        "respostes": {
            1: resposta_riu_corrent_lluitar,
            2: resposta_riu_corrent_buscar_pont,
            3: resposta_riu_corrent_pensar,
            4: resposta_riu_corrent_amic,
            5: tornar_a_cruilla
        }
    },

    Escena.CASTELL: {
        "descripcio": "\n🎉 Has arribat al castell misteriós! 🏰 La porta està tancada.\n🔑 Tens la clau per entrar?",
        "opcions": [
            OPCIO_TINC_CLAU,
            OPCIO_NO_TINC_CLAU,
            OPCIO_EXPLORAR_VOLTANTS,
            OPCIO_TORNAR_CRUILLA
        ],
        "respostes": {
            1: resposta_castell_si_clau,
            2: resposta_castell_no_clau,
            3: resposta_castell_explorar,
            4: tornar_a_cruilla
        }
    },

    Escena.CASTELL_INTERIOR: {
        "descripcio": f"""🏰 Dins del castell hi ha:
+-----------------------+
| 💎 Un tresor brillant |
| 🕳️ Un passadís secret |
| 💤 Un guardià dormit  |
+-----------------------+
¿Com vols reaccionar?
""",
        "opcions": [
            OPCIO_AGAFAR_TRESOR,
            OPCIO_EXPLORAR_PASSADIS,
            OPCIO_PASSAR_SILENCI,
            OPCIO_SORTIR_CASTELL
        ],
        "respostes": {
            1: resposta_castell_interior_tresor,
            2: resposta_castell_interior_passadis,
            3: resposta_castell_interior_guardia,
            4: resposta_castell_interior_sortir
        }
    },

    Escena.CASTELL_BIBLIOTECA: {
        "descripcio": "📜 La biblioteca està plena de pergamins màgics! 🧙 Com vols reaccionar?",
        "opcions": [
            OPCIO_PREGUNTAR_GUARDIA,
            OPCIO_EXPLORAR_BIBLIOTECA,
            OPCIO_TORNAR_ENTRADA
        ],
        "respostes": {
            1: resposta_castell_biblioteca_guardia,
            2: resposta_castell_biblioteca_explorar,
            3: resposta_castell_biblioteca_tornar
        }
    },

    Escena.CASTELL_TRESOR: {
        "descripcio": "📚 El tresor està ple 💎 i encara no té res... 🤔 Com vols reaccionar?",
        "opcions": [
            OPCIO_AGAFAR_TRESOR_FINAL,
            OPCIO_EXPLORAR_TRESOR,
            OPCIO_TORNAR_ENTRADA_TRESOR
        ],
        "respostes": {
            1: resposta_castell_tresor_agafar,
            2: resposta_castell_tresor_explorar,
            3: resposta_castell_tresor_tornar
        }   
    },
}