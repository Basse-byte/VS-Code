# Ändra en strings innehåll: Viktigt med [1:] och [:3] osv för att hela stränen ska skrivas ut.

# str= "Hello"
# new_str = "h" + str[1:]
# print (new_str)


# str = "Python"
# new_str = str[:2] + "T" + str[3:]
# print (new_str)


# age = 30
# result = "I am " + str(age) + " years old"
# print (result)

# Snabbt göra om en lista:
# words = ["Hello", "World", "Python"]
# result = " ".join(words)
# print (result)

# Manipulera strängar VERALER eller gemener:
# str = " Hello World"
# print(str.upper()) # Bara VERSALER
# print(str.lower()) # Bara gemener
# print(str.capitalize()) # Första bokstaven VERSAL
# print(str.title()) # Första bokstaven i varje ord VERSAL
# print(str.strip()) # Mellanrum i texten försvinner
# print(str.lstrip()) # Fösta mellanrum försvinner
# print(str.rstrip()) # Sista mellanrum försvinner

# Separerar orden:
# str = "apple,banana,cherry"
# fruits = str.split(",")
# print (fruits)

# Seprarerar de 2 första "stegen" i stringen:
# str = "one,two,three,four"
# str = str.split(",", 2)
# print(str)

# Byta ut en del i strängen med något annat, "apples" med "melons". Ersätter alla förekomster av ordet i strängen.
# words = "I like apples"
# print(words.replace("apples", "melon"))

# Hitta en del eller ord i en sträng. Viktigt att skriva EXAKT vad du letar efter, t.ex. VERSAL i början av ordet osv.
# words = "Hello World"
# print(words.find("World"))

# Sätta in variabler/strängar i mitten av en mening:
# name = "Sebastian"
# age = 30
# print (f"My name is {name} and I am {age} years old")



# Listor [] #########################################################################################
#####################################################################################################

# Lägga flera saker i en lista och hämta ut ett värde/variabel ur listan:
# empty_list = []

# my_list = ["apple", 42, True, 3.14]

# print(my_list[1])



# Hämta senaste värdet/värdet längst bak med -1 (längst bak) -2 (näst längst bak)
# my_list = ["apple", 42, True, 3.14]
# print (my_list[-1])

# Ändra värde i lista:
# my_list = ["apple", 42, True, 3.14]
# my_list[3] = "melon"
# print(my_list)

# Ändra värden i en lista:
# numbers = [1,2,3,4,5]
# numbers[1:4] = [20,30,40]
# print(numbers)

# Utöka listan med 6 på slutet.
# numbers = [1,2,3,4,5]
# numbers.append(6)
# print(numbers)

# # Sätta in något i en lista:
# numbers = [1,2,3,4,5]
# numbers.insert(2, "hej")
# print(numbers)

# # Ta bort något i en lista
# fruits = ["apple", "banana", "melons", "cherry"]
# fruits.remove("melons")
# print(fruits)

# # Visa vad vi tagit bort i listan ovanför:
# deleted = fruits.pop(2)
# print(f"We removed {deleted} in our list:{fruits} ")

# # Tar bort något i listan om man inte skriver något inon () tar den sista värdet i listan
# fruits.pop()
# print(fruits)

# Tar bort hela listan: 
# del fruits
# Rensar innehållet i listan:
# fruits.clear()

# fruits = ["apple", "banana", "melons", "cherry", "pear"]

# Slicea listor: lista [start:stop:step]

# print(fruits[1:4]) # Börjar på plats 2 och stoppar med 4e
# print(fruits[:3]) # Går 3 steg från början
# print(fruits[2:]) # Börjar på nummer 3 i listan
# print(fruits[::2]) # Varannat värde
# print(fruits[::-1]) # Går listan bakifrån och hela listan åt fel håll

# fruits = ["apple", "pear", "banana", "melons", "cherry", "pear"]

# Räknar hur många gånger angivet värde finns i listan:
# print(fruits.count("pear"))

# Skriver listan i ordningen den är skriven i:
# fruits = ["apple", "pear", "banana", "melons", "cherry", "pear"]
# numbers = [2,7,4,5,1]
# numbers.sort()
# print (numbers)

# Skriver värdena i listan med dubbletter tillsammans:
# fruits = ["apple", "pear", "banana", "melons", "cherry", "pear"]
# fruits.sort(key=len)
# print(fruits)
# print(len(fruits))

# Summerar värdena i listan:
# numbers = [2,7,4,5,1]
# print(sum(numbers))



# Dictionaries {} ################################### Kan endast innheålla String, int, floats, INTE LISTOR
###########################################################################################################


# empty_dict = {}
# person={"name": "Basse", "age": 30, "city": "Visby"}

# print(person["name"])
# print(person["age"])

# person["age"] = 22
# print(person)

# person["profession"] = "Hacker"

# print(person)

# age = person.pop("age")
# print(age)
# print(person)

# person={"name": "Basse", "age": 30, "city": "Visby"}

# del person["name"]
# print(person)

# Ta bort det senast tillagda i dicten:
# person["profession"] = "Hacker"
# print(person)

# key, value = person.popitem()
# print(key, value)
# print(person)

# Rensar innehållet i dicten:
# person={"name": "Basse", "age": 30, "city": "Visby"}
# person.clear()
# print(person)

# person={"name": "Basse", "age": 30, "city": "Visby"}

# Visar Keys i dicten: (Keys = "age":)
# keys = person.keys()
# print(keys)

# Visar Values i dicten (Values = "30" eller innehållet i Keysen)
# values = person.values()
# print(values)

# tuples = person.items()
# print(tuples)



# Tuples (värde,) måste ha komma-tecken efter värde ##################### är imutable, går inte att ändra
#########################################################################################################


# empty_tuple = ()
# small_tuple = (5,)

# fruits = ("apple", "melon", "cherry")

# Behöver inte ha (), Python fattar ändå att det är en Tuple
# fruits = "apple", "melon", "cherry"
# print(fruits)
# print(type(fruits))

# fruits = ("apple", "melon", "cherry")
# print(fruits[0])
# print(fruits[-1])

# print(fruits[0:3])

# fruits = ("apple", "melon", "cherry")
# fruit1, fruit2, fruit3 = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(fruits)

# fruits = ("apple", "melon", "cherry", "banana", "grape")
# fruit1, fruit2, *rest = fruits
# print(fruit1)
# print(fruit2)
# print(rest)

# numbers= fruits.count("melon")
# print(numbers)

# Visar vilken plats i en Tuple en Variabel har:
# index = fruits.index("banana")
# print(index)




# Sets {} kan vara både imutable och mutable Frozensets. Går inte att ordna, är alltid i random ordning ###############
#######################################################################################################################


# empty_set = set()

# Skriver inte ut samma värde 2 gånger:
# fruits = {"apple", "banana", "cherry", "apple"}

# print(fruits)

# Lägger till i början av Setet:

# fruits.add("grape")
# print(fruits)

# Update = lägg till flera element:

# fruits.update(["orange", "mango"])
# fruits.remove("banana") # Ta bort något i Set. Måste specificera vad. Om man tar bort något som inte finns, krashar programmet
# print(fruits)

# fruits.discard("cherry") # Lägger bort något i ett Set
# print(fruits)


# Ta bort ett slumpmässigt element i Set, och få reda på vad:

# element = fruits.pop()
# print(element)
# print(fruits)

# fruits.clear() # Clearar hela Setet.


# Kombinera Set:

# set1 = {1,2,3}
# set2 = {3,4,5}

# union_set = set1 | set2 # Kombinerar Seten och tar bort dubletter.

# print(union_set)



# Kombinera men endast ta med saker som finns i båda seten

# intersection_set = set1 & set2
# print (intersection_set)


# Oklart vad????

# difference_set = set1 - set2
# print(difference_set)


# Visar inte vad som finns i båda seten

# symmetric = set1 ^ set2
# print(symmetric)


# Frozenset går inte att lägga till något i:

# frozen_fruits = frozenset(["apple", "orange", "grape"])
# print(frozen_fruits)

# frozen_fruits.add("banana")


# set1 = {1,2,3}
# set2 = {3,4,5}

