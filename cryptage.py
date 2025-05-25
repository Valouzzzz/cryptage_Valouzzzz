texte = input("Texte : ")
cesar =int(input("cesar : "))

# Decalage Cesar 
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,!? ")

acrypter = texte.upper()
MessageCrypte = ""

for char in acrypter:
    if char in alphabet:
        index = alphabet.index(char)
        new_index = (index + cesar) % len(alphabet)
        MessageCrypte += alphabet[new_index]
    else:
        MessageCrypte += char
        
print(MessageCrypte)

# Chiffrement personaliser
cle = int(input("Cle : "))
taille_bloc = int(input("Nb caractere avant reboot : ")) #maximum 6

def lettre_vers_nombre(c):
    c = c.lower()
    if c == "_":
        return 27
    if c == ".":
        return 28
    if c == "?":
        return 29
    if c == "!":
        return 30
    if c == " ":
        return 31
    if c == ",":
        return 32
    elif c.isalpha():
        return ord(c) - ord('a') + 1
    else:
        return None

lettres = [c for c in MessageCrypte if c.isalpha() or c == '_' or c == '.' or c == '?' or c == '!' or c == ' ' or c == ',']
chiffre = []

for i in range(0, len(lettres), taille_bloc):
    bloc = lettres[i:i+taille_bloc]
    
    compteur = {}
    for char in bloc:
        compteur[char] = compteur.get(char, 0) + 1

    for char in bloc:
        freq = compteur[char]
        valeur_de_base = lettre_vers_nombre(char)
        valeur_modifiee = (valeur_de_base + freq) * cle
        chiffre.append(valeur_modifiee)


print(lettres)
print(chiffre)
