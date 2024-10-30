# Uppgift 1 ######################################################################################################
# namn1 = " aNnA kaRlSsOn "
# namn2 = namn1.strip()
# # Mellanslag borta

# namn3 = namn2.title()
# # Första bokstaven i varje namn är nu VERSAL, resten gemener

# namn4 = namn3.replace(" ", "-")
# # Ersätter mellanrum i variablen med bindesstreck
# print(namn4)


# Uppgift 2 ######################################################################################################
# order = "bröd", "mjölk", "ägg", "smör", "ost", "yoghurt",
# Tuple med varorna i beställningen

# print (order[0:3:])
# # Skrev ut 3 första varorna

# print (order[4:6])
# # Skrev ut 2 sista varorna

# print(order[::2])
# # Skrev ut varannan vara i ordern


# Uppgift 3 Manuellt ######################################################################################################
# filmer = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
# # Skapar en lista som heter "filmer"

# filmer.append("Memento")
# # Lägger till filmen Memento i slutet på listan

# print(filmer)
# # Kollar hur listan ser ut för att veta vilken plats alla variabler har
# filmer[1] = "The Lord of the Rings"
# # Ändrar variabeln med plats 1 till annan film
# print(filmer)
# # Kollar nya innehållet i listan

# filmer.pop(3)
# # Tar bort filmen på plats 3
# print(filmer)
# # Kollar innehållet i listan

# filmer.insert(2, "The Dark Knight")
# # Sätter in filmen på plats 2 (egentligen plats 3) i listan
# print(filmer)
# # Kollar innheållet i listan.


# Uppgift 3 Script IF och for-Loop ######################################################################################################

# filmer = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
# print(filmer)

# if "Momento" not in filmer:
#     filmer.append("Momento")
#     print(filmer)
#     if "Momento" in filmer[4]:
#         filmer[1] = "The Lord of the Rings"
#         print(filmer)
#         for i in range(len(filmer)):
#             if filmer[i] == "The Lord of the Rings":
#                 filmer.remove("The Prestige")
#                 print(filmer)
#                 break
# for i in range(len(filmer)):
#     if filmer[i] != "The Dark Knight":
#         filmer.insert(2, "The Dark Knight")
#         break

# print(filmer)