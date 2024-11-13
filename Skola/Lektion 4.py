# x = 20 
# if x > 10:
#     print ("Above 10")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# x = 7
# y = 10
# if x > 5 and y < 15:
#     print("Both conditions are true")

# x = 7
# y = 20
# if x > 5 and y < 15:
#     print("Both conditions are true")

# # INTE BRA, Oklart och svårt att följa    
# x = 10
# parity = "even" if x % 2 == 0 else "odd"
# print("Nummer är {parity}")

# a = b = c = 10

# if a == b == c:
#     print ("Alla är lika")
    
## if och else "pass"
# x = 10
# if x > 0 :
#     print ("x is positive")
# else:
#     pass


# Error Handling:
# number = input("Type a number ")
# if number.isdigit():
#     number = int(number)
#     print(f"You typed a number: {number}")
# else:
#     print("That's not a number")

## Inte ett bra sätt att skriva på, blir otydligt
# x = 5
# y = 10
# z = 15

# if (x < y and y < z) or x == z:
#     print("True")


# # Funktion:
# def max_value(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# biggest = max_value(10, 20)
# print(f"The biggest value is {biggest}")

## For -loopar: for VARIABELNAMN in VALFRITT OBJEKT
# for variabel in iterable:

# fruits = ["apple", "banana", "cherry"]
# # for varje FRUKT i FRUKTER körs print(fruit)
# for fruit in fruits:
#     print(fruit)



# person = ("Alice,", 30, "Stockholm")
# name, age, city = person
# print(name)
# print(age)
# print(city)


# # Hämta ut innehåll från Tuples/listor
# people = [("Alice", 30, "Stockholm"), ("Bob", 25, "Göteborg"), ("Charlie", 43, "Malmö")]
# for name, age, city in people:
#     print(f"Namn: {name}, Age: {age}, stad: {city}")

# # Dictionary "person" innehåller (name = key) och (Alice = value).
# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for key, value in person.items():
#     print(f"{key}: {value}")


# # For varje bokstav i text, printa ut bokstav. 
# text = "Hello"
# for bokstav in text:
#     print(bokstav)

# # Samma sak men på en Sets
# frukter = {"äpple", "banan", "Körsbär"}
# for frukt in frukter:
#     print(frukt)

# # Hämta ut keys ur en dict, går även att göra med values istället för keys.
# person = {"name": "Alice", "age": "30", "city": "Stockholm"}
# for key in person.keys():
#     print(key)


# # Range har ett [start:stop:step]. loopar 5 gånger: 0,1,2,3,4.
# for siffra in range(5):
#     print(siffra)

# for i in range (2, 10, 2):
#     print(i)

# Nestlad loop:
# for i in range (3):
#     for j in range (2):
#         print(f"i: {i}, j: {j}")

# Kan använda break och continue

# BREAK När i gjort 5 gånger stoppar den. Går inte till 10.
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# # CONTINUE. Om talet är delbart med 2, fortsätt upp till 10.
# for i in range (10):
#     if i % 2 == 0:
#         continue
#     print(i)

# x = 0
# while x < 5:
#     print (x)
#     x += 1 # += 1 betyder för varje plus 1, körs 5 gånger.


# while True:
#     print ("This is running forever")
#     break # Nej det gör det inte för vi har en BREAK
