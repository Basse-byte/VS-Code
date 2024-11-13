# 2. Åldrar på vänner
# Skapa en dictionary där nycklarna är dina vänners namn och värdena är deras åldrar.
# Skriv en loop som skriver ut varje väns namn och ålder.

# friends = {"Basse": 30, "Sandro": 28, "Isac": 32, "Sarai": 31, "Sygryda": 29}

# for friend, age in friends.items():
#     print(f"{friend}: {age}")

###################################################################################################################

# 3. Multiplicera tal i en lista
# Du har en lista `numbers = [2, 4, 6, 8, 10]`.
# Skriv kod som multiplicerar varje tal med 2 och uppdaterar listan med de nya värdena.

numbers = [2, 4, 6, 8, 10]

for number in numbers:
    new_number = number * 2
    numbers.append(new_number)
print(numbers)