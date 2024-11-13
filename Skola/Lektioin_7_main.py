# ## Importera paket som vi själv skapat ##################################################

# import Lektion_7_Moduler

# print(Lektion_7_Moduler. greet("Basse"))
# print(Lektion_7_Moduler.add(10, 25))
# print(Lektion_7_Moduler.PI)


# ## Alternativt endast vissa moduler ####################################################

# from Lektion_7_Moduler import greet, add

# print(greet("Basse"))
# print(add(26, 33))


# ## Import från egna modulerna ur my_package. ##############################################

# from my_package import module1, module2

# print(module1.function1())
# print(module2.function2())


## Exempel på en bra grej: ###################################################################

def main():
    # Mitt program
    print("Hej då")


if __name__=="__main__":
    main()
