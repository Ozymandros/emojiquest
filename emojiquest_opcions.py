# emojiquest_opcions.py
from emojiquest_core import Opcio

class Opcions:
    class Cruilla:
        BOSC = Opcio(1, " 🌳 ", "Camí del bosc fosc")
        MUNTANYA = Opcio(2, " ⛰️ ", "Camí de la muntanya")
        RIU = Opcio(3, " 🌊 ", "Camí del riu")
        EXPLORAR = Opcio(4, " 🔍 ", "Explorar els voltants")

    class Bosc:
        LLUITAR = Opcio(1, " ⚔️ ", "Lluitar contra el llop")
        FUGIR = Opcio(2, " 🏃 ", "Fugir ràpidament")
        ESTRATEGIA = Opcio(3, " 🧠 ", "Pensar una estratègia")
        AMIC_LLOP = Opcio(4, " 🤝 ", "Intentar fer-te amic")
        TORNAR_CRUILLA = Opcio(5, " 🔄 ", "Tornar a la cruïlla inicial")

    class Muntanya:
        TRENCAR_ROCA = Opcio(1, " ⚔️ ", "Intentar trencar la roca")
        BUSCAR_CAMI = Opcio(2, " 🏃 ", "Buscar un altre camí")
        PENSAR = Opcio(3, " 🧠 ", "Pensar com superar-la")
        DEMANAR_AJUDA = Opcio(4, " 🤝 ", "Demanar ajuda")
        TORNAR_CRUILLA = Opcio(5, " 🔄 ", "Tornar a la cruïlla inicial")

    class Riu:
        LLUITAR_CORRENT = Opcio(1, " ⚔️ ", "Intentar lluitar contra el corrent")
        BUSCAR_PONT = Opcio(2, " 🏃 ", "Buscar un pont")
        PENSAR_SOLUCIO = Opcio(3, " 🧠 ", "Pensar una solució")
        AMIC_CORRENT = Opcio(4, " 🤝 ", "Fer-te un amb el corrent")
        TORNAR_CRUILLA = Opcio(5, " 🔄 ", "Tornar a la cruïlla inicial")

    class Castell:
        TINC_CLAU = Opcio(1, " ✅ ", "Sí, tinc la clau")
        NO_TINC_CLAU = Opcio(2, " ❌ ", "No tinc la clau")
        EXPLORAR = Opcio(3, " 🔍 ", "Explorar els voltants")
        TORNAR_CRUILLA = Opcio(4, " 🔄 ", "Tornar a la cruïlla inicial")

    class CastellInterior:
        AGAFAR_TRESOR = Opcio(1, " 💎 ", "Agafar el tresor")
        EXPLORAR_PASSADIS = Opcio(2, " 🕳️ ", "Explorar el passadís")
        PASSAR_SILENCI = Opcio(3, " 💤 ", "Intentar passar silenciosament")
        SORTIR_CASTELL = Opcio(4, " 🔙 ", "Sortir del castell")

    class Biblioteca:
        PREGUNTAR_GUARDIA = Opcio(1, " 🧌 ", "Preguntar a un guardià")
        EXPLORAR = Opcio(2, " 🔍 ", "Explorar els voltants")
        TORNAR_ENTRADA = Opcio(3, " 🔙 ", "Tornar a l'entrada del castell")

    class CastellTresor:
        AGAFAR_TRESOR_FINAL = Opcio(1, " 💎 ", "Agafar el tresor")
        EXPLORAR_TRESOR = Opcio(2, " 🔍 ", "Explorar els voltants")
        TORNAR_ENTRADA_TRESOR = Opcio(3, " 🔙 ", "Tornar a l'entrada del castell")