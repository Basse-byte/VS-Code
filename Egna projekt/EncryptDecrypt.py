import random
import string

# Använder moduler för bokstäver, siffror och tecken.
chars = " " + string.punctuation + string.digits + string.ascii_letters
# Gör om alla tecken till en lista.
chars = list(chars)
# Kopierar listan som genererats in i variabeln "key"
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#Encrypt
plain_text = input("Enter a message to encrypt:")
cipher_text = ""

# För varje bokstav/element i variablen plain_text.
for letter in plain_text:
    # Index variabeln är: listan med chars indexerad, alltså positionen av bokstaven.
    index = chars.index(letter)
    cipher_text += key[index]

try: # För att se om det blir fel.
    # Lägger till det krypterade meddelandet och nyckeln för att lösa krypteringen.
    with open("Encrypted messages.txt", "a") as file:
        file.write("Encrypted message:" + cipher_text + "\n")
        file.write("Actual string of characters below:" + "\n")
        file.write(str(chars) + "\n")
        file.write(str(key) + "\n")
        file.write("Cypher key above:" + "\n")
        file.write("\n")
        file.write("==============================================================================\n")
        file.write("\n")
        print("The cipher text and key were saved to textfile \n")
except IOError as e: # För att se om det blir fel.
    print(f"An error occurred while writing to the file: {e}")

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

######################################################################################################
#Decrypt:
cipher_text = input("Enter a message to decrypt:")
plain_text = ""

# För varje bokstav/element i variablen cipher_text.
for letter in cipher_text:
    # Precis tvärt emot det vi gjorde i Encrypt-delen
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message {cipher_text}")
print(f"Decrypted message: {plain_text}")