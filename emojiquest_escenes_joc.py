from emojiquest_respostes_joc import *
from emojiquest_opcions import *

from emojiquest_core import Escena

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
            OPCIO_BOSC_LLUITAR,
            OPCIO_BOSC_FUGIR,
            OPCIO_BOSC_ESTRATEGIA,
            OPCIO_BOSC_AMIC_LLOP,
            OPCIO_BOSC_TORNAR_CRUILLA
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
            OPCIO_MUNTANYA_TRENCAR_ROCA,
            OPCIO_MUNTANYA_BUSCAR_CAMI,
            OPCIO_MUNTANYA_PENSAR,
            OPCIO_MUNTANYA_DEMANAR_AJUDA,
            OPCIO_MUNTANYA_TORNAR_CRUILLA_MUNTANYA
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
            OPCIO_RIU_LLUITAR_CORRENT,
            OPCIO_RIU_BUSCAR_PONT,
            OPCIO_RIU_PENSAR_SOLUCIO,
            OPCIO_RIU_AMIC_CORRENT,
            OPCIO_RIU_TORNAR_CRUILLA_RIU
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
        "descripcio": "🎉 Has arribat al castell misteriós! 🏰 La porta està tancada.\n🔑 Tens la clau per entrar?",
        "opcions": [
            OPCIO_CASTELL_TINC_CLAU,
            OPCIO_CASTELL_NO_TINC_CLAU,
            OPCIO_CASTELL_EXPLORAR,
            OPCIO_BOSC_TORNAR_CRUILLA
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
            OPCIO_CASTELL_INTERIOR_AGAFAR_TRESOR,
            OPCIO_CASTELL_INTERIOR_EXPLORAR_PASSADIS,
            OPCIO_CASTELL_INTERIOR_PASSAR_SILENCI,
            OPCIO_CASTELL_INTERIOR_SORTIR_CASTELL
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
            OPCIO_BIBLIOTECA_PREGUNTAR_GUARDIA,
            OPCIO_BIBLIOTECA_EXPLORAR_BIBLIOTECA,
            OPCIO_BIBLIOTECA_TORNAR_ENTRADA
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

    Escena.CASTELL_JARDI: {
        "descripcio": "🌿 Has entrat en un jardí secret ple de plantes màgiques! 🌸✨",
        "opcions": [
            Opcio(1, " 🌸 ", "Recollir una flor màgica"),
            Opcio(2, " 🔙 ", "Tornar al castell")
        ],
        "respostes": {
            1: {"text": "🌸 La flor brillant et dóna energia! +10 punts d'ànim. ✨", "seguent_escena": Escena.CASTELL_INTERIOR},
            2: {"text": "🚪 Tornes a l'interior del castell", "seguent_escena": Escena.CASTELL_INTERIOR}
        }
}


}