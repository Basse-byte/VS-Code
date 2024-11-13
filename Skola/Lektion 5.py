## While loopar########################################################################################

# x = 0
# while x <= 5:
#     print (x)
#     x += 1

## Break:

# x = 0
# while x <= 5:
#     print (x)
#     if x == 5:
#         break
#     x += 1

# # Continue

# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0: # Printar alla ojämna tal.
#         continue
#     print(x)
    
# # Else-sats

# x = 0
# while x < 5:
#     print (x)
#     x +=1
#     # Break här kommer göra att programmet hoppar över Else.
# else:
#     print("Loopen avslutades")

#¤ Input:

# user_input = input("Ange ett kommando ")
# print(user_input)

# while True:
#     user_input = input("Ange ett kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev rätt!")
#         break
#     else:
#         print("Fel input, försök igen")

# Logiska operatörer, AND OR NOT.

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)
# print(not b)

# Man kan chaina jämförelseoperatörer.

# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10)

# age = int(input("Ange din ålder: ")) # Gör om string input till int direkt.
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")


## Files ##############################################################################################
## a+ Läsning och append o skapar ny fil om den inte finns.
## r läsning o filen måste existera.
## w skrivning o skapar en ny fil eller skriver över en befintlig.
## a append o skriver data till slitet av en fil om den redan finns.
## r+ läsning och skrivning o filen måste existera innan.
## w+ läsning och skrivning o skapar ny fil eller skriver över befintlig.

# file = open("textfil.txt", "r")
# line = file.readline() # Läsen en rad i taget på filen.
# while line:
#     print(line), end = "" # gör att det inte blir mellanrum, eller ny rad.
#     line = file.readline()
# file.close()

# file = open("textfil.txt", "r")
# lines = file.readlines() # Notera s på slutet av readlines. Läser in varje line till en lista.
# for line in lines:
#     print(line, end="")
# file.close()

# file = open("textfil.txt", "r")
# lines = file.read().splitlines() # Slitlines tar bort radbrytningen.
# print(lines)

## user_input = input("\n Input: ") # \n för att ställa markören på en ny rad.

# file = open("textfil.txt", "w")
# file.write("Hej detta är ett test \n")
# file.write("Nästa rad")
# file.close()

## with - stänger filen automatiskt. när vi kommer utanför indenteringen.

# with open("textfil.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("textfil.txt", "w") as file:
#     file.write("Lite text \n")
#     file.write("Lite mer text")
    

## List comprehension, sparar bara plats. Gör inte saker mer effektivt #########################################################################################

# [expression for item in iterable]

## På vanligt sätt:
# numbers = [1,2,3,4,5] # Lista med nummer
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

## Med List Comprehension:
# numbers = [1,2,3,4,5]
# squares = [num ** 2 for num in numbers]
# print(squares)

## Med if sats:
# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

## Med list comprehension
# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

## Med sets, eliminerar dubbeletter:
# numbers = [1,2,3,4,4,5]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)

# Dict comprehension. Skapar ett set med frukter och omvandlar till dict.
# fruits = ["apple", "cherry", "grape"]
# fruit_lengths = {fruit: len(fruit) for fruit in fruits}
# print(fruit_lengths)


## Enumerate ############################################################################################

# fruits = ["apple", "cherry", "grape"]
# for index, fruits in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruits}")


## Tuple:

# fruits = ("apple", "cherry", "grape")
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruits}")


# matrix = [
#     [1,2,3]
#     [4,5,6]
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumerate(row):
#         print(f"Matrix[{i}{j}] = {value}")


## zip, zlippar ihop flera listor ##################################################################################################

# name = ["Alice", "Bobbo", "Stefan"]
# age = [24,37,19]
# for name, age in zip(name, age):
#     print(f"Namn: {name}, Ålder: {age}")

## Input ###############################################################################################

# name = input("Ange ditt namn: ")
# print("Ditt namn är:", name)


## Funktioner #########################################################################################

# def function_name(parametrar): # () kan vara tom också.
#     # kod
#     return

# def greet(name):
#     return f"Hello, {name}"

# print("Test")
# print(greet("Bobbo"))


# def add (a, b):
#     return a + b

# result = add(10, 25)
# print(result)


# def greet(name="World"):
#     return f"Hello {name}"

# print(greet())
# print(greet("Bobbo"))


# def add(a, b):
#     return a + b

# def add_and_square(a, b):
#     sum = add(a,b)
#     return sum * sum

# print(add_and_square(5, 2))



## Logik och funktioner ################################################################################

# def categorize_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20:
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Retiree"
    
# print(categorize_age(10))
# print(categorize_age(15))
# print(categorize_age(35))
# print(categorize_age(88))


## Packa upp en Tuple med *
# def add(a, b):
#     return a + b

# pair = (3, 5)
# result = add(*pair)
# print(result)

## Funktioner i funktioner:
# def make_power(exponent):
#     def power(x):
#         return x ** exponent
#     return power

# result = make_power(3)

# print(result(4))


