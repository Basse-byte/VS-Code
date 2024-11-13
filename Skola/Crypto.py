from cryptography.fernet import Fernet

# with open("secret.key", "rb") as file:
#     key = file.read()

# # print(f"Nyckel laddad: {key}")

# ## Encrypt: ###############################################################################

# cipher_suite = Fernet(key)

# message = input("Skriv det du vill kryptera: ").encode()
# cipher_text = cipher_suite.encrypt(message)
# print(f"Cyphertext: {cipher_text}")

# with open("Encrypted_msg.enc", "wb") as file:
#     file.write(cipher_text)

# ## Decrypt:  ###############################################################################

# with open("Encrypted_msg.enc", "rb") as file:
#     encrypted_message = file.read()

#     plain_text = cipher_suite.decrypt(encrypted_message)
#     print(f"Det hemliga meddelandet är: {plain_text.decode()}")


## Läsa in binära filer ############################################################################

# with open("bild.png", "rb") as file:
#     data = file.read()


# with open("ny_bild.png", "wb") as new_file:
#     new_file.write(data)


## argparse. I terminal, skriv: python Crypto.py Basse 30 #############################################################

# import argparse

# parser = argparse.ArgumentParser(description="Exempel verktyg")

# parser.add_argument("name", help="Här anger du ditt namn")
# parser.add_argument("age", type=int, help="Ange din ålder här")

# parser.add_argument("-c", "--city", help="Ange din stad", default="Okänd stad")
# # parser.add_argument("-v", "--verbose", action="store_true", help="Visa detaljerad info")
# parser.add_argument("-m", "--mode", choices=["enkel", "detaljerad"], help="Välj läge")

# args = parser.parse_args()

# if args.mode == "detaljerad": # Crypto.py Basse 30 -m detaljerad -c Stockholm
#     print(f"Hej {args.name}. Du är {args.age} år gammal. Du bor i {args.city}")
# else:
#     print(f"Hej {args.name}")


## Undantashantering ########################################################################

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel: Division med noll är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally: # körs alltid oavsett
#     print("Slutet på try except")

