import re
import os

with open("index.html", "r", encoding="utf8", errors="ignore") as f:
    text = f.read()

# Replace all mojibake
text = text.replace("ǟǟ", "çã")
text = text.replace("ǟ", "é")
text = text.replace("ǽ'??", "—")
text = text.replace("SERVIOS", "SERVIÇOS")
text = text.replace("SOBRE N\"S", "SOBRE NÓS")
text = text.replace("SOLU ES", "SOLUÇÕES")
text = text.replace("Instalaǜo", "Instalação")
text = text.replace("Impermeabilizaǜo", "Impermeabilização")
text = text.replace("construǜo", "construção")
text = text.replace("tǸcnica", "técnica")
text = text.replace("tǸcnicos", "técnicos")
text = text.replace("Tǟcnica", "Técnica")
text = text.replace("Construǟǟo", "Construção")
text = text.replace("Impermeabilizaǟǟo", "Impermeabilização")
text = text.replace("impermeabilizaǟǟo", "impermeabilização")
text = text.replace("construǟǟo", "construção")
text = text.replace("tǟcnica", "técnica")
text = text.replace("tǟcnicos", "técnicos")
text = text.replace("ǟ'Ń?Tǟ?s'os", "ços")
text = text.replace("ǟ'Ń?Tǟ?s'rios", "ários")

# General fixes
text = text.replace("ÃƒÂ§ÃƒÂ£o", "ção")
text = text.replace("ÃƒÂ©", "é")

with open("index.html", "w", encoding="utf8") as f:
    f.write(text)

print("Fixed index.html encoding.")
