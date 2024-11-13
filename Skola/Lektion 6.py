# *args **kwargs

# def fuction_name(*args):
#     for arg in args:
#         print(arg)

# function_name(1,2,3,4,5,6,7,8,9)

#Går att skicka in oändligt många parametrar/variablar i funktionen med args.

# def print_info(name, *args):
#     print (f"Name: {name}")
#     for arg in args:
#         print(arg)

# print_info("Alice", 30, "Stocholm", "frans", 1, 15)


# kwargs går att skicka in iterabler i. t.ex. flera listor, tuples osv.

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
        
# print_details(name="Alice", age=30, city="Stockholm")


# **kwargs och *args:

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# # print_all(1, 2, 3, name="Alice", age=30, city="Stockholm")
# print_all(1, 2, 3, name="Alice", age=30, city="Stockholm")


# Annat exempel med lista:

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key in kwargs.items():
#         print(key)
# print_all([1, 2, 3], "Alice", (4,5,6),)

# Annat exempel:

# def sum_numbers(*args):
#     return sum(args) # sum är en inbyggd funktion som summerar.

# print(sum_numbers(1,2,3,4))

# Ett till exempel på kwargs:

# def build_profile(**kwargs):
#     return kwargs

# profile = build_profile(name="Ali", age=30, job="Hacker")
# print(profile)

# Exempel:

# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(1,2,3, name="Ali", age=30, job="Göteborg")
# print(display_info)

# Avancerad uppgift:

# def calculate(operation, *args, **kwargs):
#     if operation == "add":
#         return sum(args)
#     elif operation == "subtract":
#         result = args[0]
#         for num in args[1:]:
#             result -= num
#         return result
#     elif operation == "multiply":
#         result = 1
#         for num in args:
#             result *= num
#         return result
#     elif operation == "divide":
#         result = args[0]
#         try:
#             for num in args[1:]:
#                 result /= num
#         except ZeroDivisionError:
#             return "Can't divide by zero"
#         return result
#     else:
#         return "Unknown operation"

# print(calculate("add", 1, 2, 3, 4,))
# print(calculate("subtract", 10, 2, 3,))
# print(calculate("multiply", 2, 3, 4,))
# print(calculate("divide", 2, 3, 4,))


# lambda funktion, Kan ha flera arguments men endast ETT expression.
# lambda arguments: expression

# add = lambda x, y: x + y
# print(add(2,3))
# # Samma sätt ovanför o nedanför exempel.
# def add(x, y):
#     return x + y



# map är en inbyggd python funktion, låter en applicera en speciell funktion i en iterable.

# map(function, iterable)

# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# square_numbers = list(map(square, numbers))

# print(square_numbers)


# Med lambda:

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x * x, numbers))
# print(squared_numbers)

# filter funktionen:
# filter(function, iterable)

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

## Exakt samma som ovanför men med lambda:
# number = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, number))
# print(even_numbers)


# Inbäddade if satser.

# def check_numbers(num):
#     if num > 0:
#         if num % 2 == 0:
#             print(f"{num} is a positive even number")
#         else:
#             print(f"{num} is a positive odd number")
#     else:
#         if num == 0:
#             print (f"{num} is 0")
#         else:
#             print(f"{num} is a negative number")

# check_numbers(10)
# check_numbers(-5)


# Nestlade for loops

# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
#         print()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix(matrix)

# Exempel på local variabel som inte går att anropa utanför funktionen

# def my_function():
#     local_var = 10
#     print(local_var)

# my_function()
# print(local_var)

# Exempel på global var, den är utanför funktionen. 

# global_var = 20

# def my_function():
#     print(global_var)

# my_function()
# print(global_var)

# Exempel 2 på scope:

# def outer_function():
#     outer_var = "Yttre"

#     def inner_function():
#         inner_var = "Inre"
#         print(outer_var)
#         print(inner_var)

#     inner_function()

# outer_function()


# Built in scope:

# x = 10 # x får ett annat värde i funktionen modify_global

# def modify_global():
#     global x # global gör att variabeln blir global.
#     x = 20

# modify_global()
# print(x)


# 

# def outer_function():
#     x = "Outer"

#     def inner_function():
#         nonlocal x
#         x = "Inner"
#         print(x)
#     inner_function()
#     print(x)
# outer_function()


# 

