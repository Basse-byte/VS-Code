## Input validering ##

# user_input = input("Skriv något:")
# print(user_input)

# while True:
#     user_input = input("Skriv ett nummer:")
#     if user_input.isdigit():
#         user_number = int(user_input) # Konverterar inputen från string till int.
#         print(f"Du angav: {user_number}")
#         break
#     else:
#         print("Ogiltig input")

# try:
#     user_input = input("Skriv ett nummer: ")
#     user_number = int(user_input)
#     print(f"Du angav: {user_number}")
# except ValueError:
#     print("Ogiltig input")


# valid_options = ["ja", "nej", "kanske"]
# user_input = input("Vill du sova? ").lower # .lower gör att inputen konverteras till små bokstäver.

# if user_input in valid_options:
#     print(f"Du valde {user_input}")
# else:
#     print("Jag förstår inte, försök igen")



## OOP - Objektorienterad programmering ###########################################################################################


# class Car:
#     wheels = 4

#     def __init__(self, make, model, year): # self måste alltid vara med först.
#         self.make = make
#         self.model = model
#         self.year = year

#     def description(self):
#         return f"{self.make}, {self.model}, {self.year}"
    
# car1 = Car("Volvo", "240", 1985)
# car2 = Car("Honda", "Civic", 2017)

# print(car1.description())
# print(car2.description())

# print(car1.make, car1.model, car1.year)
# print("Wheels:",car1.wheels)

# print(car2.make, car2.model, car2.year)
# print("Wheels:",car2.wheels)


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())
# print(cat.speak())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name, breed, color):
#         super().__init__(name)
#         self.breed = breed
#         self.color = color

#      def speak(self):
#         return f"{self.name} says Woof!"

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"My name is: {self.name}, I am {self.age} years old."

# person1 = Person("Bobbo", 37)
# print(person1)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __repr__(self):
#         return f"My name is: {self.name}, I am {self.age} years old."
    
# person1 = Person("Bobbo", 37)
# print(person1)



## Ärva från befintlig datatyp ##############################################################
## AVANCERAT / ÖVERKURS #####################################################################

# class StringReversed(str):
#     def reverse(self):
#         return self[::-1]

# my_string = StringReversed("Hello")
# print(my_string.reverse())

# class DefaultDict(dict):
#     def __init__(self, default_value):
#         super().__init__()
#         self.default_value = default_value
    
#     def __getitem__(self, key):
#         return super(). get(key, self.default_value)

# my_dict = DefaultDict(0)
# print(my_dict["missing_key"])
# my_dict["random"] = 10
# print(my_dict["random"])
