# Skapa en ordbok som representerar en telefonkatalog med namn som nycklar och telefonnummer som värden.

# telefonkatalog = {"Sebastian": "0735953976", "Maiko": "0737691911", "Tommy": "0705741998"}
# telefonkatalog["Linda"] = "0703579222"
# print(telefonkatalog)


with open("log.txt", "r") as f:
    for line in f:
        if "Failed" in line:
            print(line)
            