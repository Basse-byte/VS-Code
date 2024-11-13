# 1. Multiplikationstabellen
#   Skapa ett program som genererar och skriver ut en multiplikationstabell för ett tal
#  som användaren matar in.
#  Krav:
#  ● En funktion för att skapa en multiplikationstabell.
#  ● Programmet ska fråga användaren vilket tal som ska multipliceras och till
#  vilket maxvärde.
#  ● En funktion för att kontrollera om den inmatade strängen bara innehåller
#  siffror. Använd funktionen isdigit()
#  ● Skriv ut tabellen
####################################################################################################

# print("Skriv ett tal som du vill se multiplikationstabellen för: ")
# in_tal = input()

# for tal in in_tal:
#     if tal % in_tal == 0:
#         print(tal)

x = input("What multiplication chart would you like to se?: ")
# y = input("Type another number: ")
z = input("What's the highest multiplication chart you want to see?: ")

tal1 = int(x)
# # tal2 = int(y)
max_tal = int(z)

# while result <= max_tal:
#     for i in range(0, max_tal+1, tal1):
#         i = tal1 * i
#         for j in range(0,max_tal+1, tal1):
#             print(i*j)
#             break 

print(f"The multiplication chart for {tal1} up to {tal1} * {max_tal} is:")
for i in range(0, max_tal + 1):
    print(f"{tal1} x {i} = {tal1 * i}")

##################################################################################################################

