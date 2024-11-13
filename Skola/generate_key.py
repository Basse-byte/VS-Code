# Plaintext: ursprunglig olåst info som kan läsas av människor.

# Ciphertext: den krypterade versionen av Plaintext, ser ut som en slumpmässig följd av tecken.

# Nyckel: en sekvens av tecken eller siffor som används för att kryptera och dekryptera data. 
# Längden och komplexiteten avgör styrkan på krypteringen.

# Krypteringalgoritm (Chiffer): en matematisk funktion som används för att omvandla plaintext till ciphertext
# baserat på given nyckel.

# Dekryptering: omvändingen av krypterin där chiphertext konverteras tillbaka till den ursprungliga platintexten
# med hjälp av nyckeln.

# Symmetrisk kryptering - Använder en nyckel för både kryptering och dekryptering.
# Asymmetrisk kryptering - Använder 2 nycklar: en publik för kryptering och en privat för dekryptering.


from cryptography.fernet import Fernet

key = Fernet.generate_key() # Genererar en nyckel i binär data
print(f"Genererad nyckel: {key.decode()}") # key.decode() formaterar om nyckeln till vanliga tecken.

with open("secret.key", "wb") as file: # filnamn.key för att filen ska bli en binär nyckel. "wb" skapar i binärt format.
    file.write(key) # Skriver in key i filen.
