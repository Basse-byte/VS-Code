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



## Avancerad uppgift #############################################################################################

data = {
"studenter": [
("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv": True}),],
"kurser": {
"Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
"Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
"Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
}
}


aktiva_studenter = [] # Skapar en tom lista att lagra aktiva studenter i.
for student in data["studenter"]: # Vi går igenom varje student.
    if student[1]["aktiv"]: # Om studenten är aktiv lägger vi till den i listan.
        aktiva_studenter.append(student[0])

aktiva_studenter = tuple[aktiva_studenter] # Vi gör om listan till en Tuple.

# print(aktiva_studenter)

# Lista för att lagra alla ämnen från aktiva studenter
alla_amnen = []

# Gå igenom varje student
for student in data["studenter"]:
    if student[1]["aktiv"]:
        # Lägg till alla ämnen för den aktuella studenten till listan
        alla_amnen.extend(student[1]["ämnen"])

# Skapa ett set för att få unika ämnen
unika_amnen = set(alla_amnen)

# print(unika_amnen)


