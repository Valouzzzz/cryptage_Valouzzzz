# Chiffrement personnaliser
def nombre_vers_lettre(n):
    if n == 27:
        return "_"
    if n == 28:
        return "."
    if n == 29:
        return "?"
    if n == 30:
        return "!"
    if n == 31:
        return " "
    if n == 32:
        return ","
    elif 1 <= n <= 26:
        return chr(n + ord('a') - 1)
    else:
        return "?"

def decrypter_approx(texte_chiffre, cle, taille_bloc):
    texte_dechiffre = []
    index = 0

    for i in range(0, len(texte_chiffre), taille_bloc):
        bloc = texte_chiffre[i:i+taille_bloc]
        bloc_lettres = []

        for valeur_chiffree in bloc:
            found = False
            for freq in range(1, 6):
                valeur_estimee = (valeur_chiffree // cle) - freq
                if 1 <= valeur_estimee <= 32:
                    lettre = nombre_vers_lettre(valeur_estimee)
                    bloc_lettres.append(lettre)
                    found = True
                    break
            if not found:
                bloc_lettres.append("?")

        texte_dechiffre.extend(bloc_lettres)

    return ''.join(texte_dechiffre)

# Paramettre 
texte_chiffre = [174, 84, 168, 174]
cesar = 8
cle = 6
taille_bloc = 2

texte_estime = decrypter_approx(texte_chiffre, cle, taille_bloc)
print("Texte déchiffré approximatif :", texte_estime)

# Decalage Cesar 
texte = texte_estime
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,!? ")

texte = texte.upper()
MessageDecrypte = ""

for char in texte:
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index - cesar) % len(alphabet)
        MessageDecrypte += alphabet[new_index]
    else:
        MessageDecrypte += char

print("Message déchiffré :", MessageDecrypte)
