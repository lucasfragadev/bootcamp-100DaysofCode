# Seção 3: Day 3 - Beginner - Control Flow and Logical Operators

# Geral

# print("Welcome")
# heigth = int(input("What is your height in cm? "))

# if heigth >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

    

# Número Par ou Ímpar

# number = int(input("Digite um número: "))

# if number % 2 == 0:
#     print("Este número é par")
# else:
#     print("Este número é ímpar.")

# Height and +18 or not

# print("Welcome")
# heigth = int(input("What is your height in cm? "))
# if heigth >= 120:
#     age = int(input("How old are you? "))
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         print("Pay $5.")
#     elif age <= 18:
#         print("Pay $7.")
#     else:
#         print("Pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# BMI

# weight = float(input("What is your weight? "))
# height = int(input("What is your height in cm? "))
# height_meter = height / 100.00
# bmi = (weight/height_meter**2)

# if bmi < 16:
#     print("Severely underweight")
# elif 16 <= bmi <= 17:
#     print("Moderately underweight")
# elif 17 < bmi <= 18.5:
#     print("Slightly underweight")
# elif 18.5 < bmi <= 24.9:
#     print("Normal weight")
# elif 25 <= bmi <= 29.9:
#     print("Overweight")
# elif 30 <= bmi <= 34.9:
#     print("Obesity class I")
# elif 35 <= bmi <= 39.9:
#     print("Obesity class II")
# else:
#     print("Obesity class III")


#  PIZZA PYTHON

# print("Thank you for choosing Python Pizza Deliveries! ")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0 

# if size == "S":
#     bill =+ 15
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill =+ 18
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 17
#             print(f'Your final bill is: ${bill}.')
#     else:
#         if extra_cheese == "Y":
#             bill =+ 16
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 15
#             print(f'Your final bill is: ${bill}.')
# elif size == "M":
#     bill =+ 20
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill =+ 24
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 23
#             print(f'Your final bill is: ${bill}.')
#     else:
#         if extra_cheese == "Y":
#             bill =+ 21
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 20
#             print(f'Your final bill is: ${bill}.')

# elif size == "L":
#     bill =+ 25
#     if add_pepperoni == "Y":
#         if extra_cheese == "Y":
#             bill =+ 29
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 28
#             print(f'Your final bill is: ${bill}.')
#     else:
#         if extra_cheese == "Y":
#             bill =+ 26
#             print(f'Your final bill is: ${bill}.')
#         else:
#             bill =+ 25
#             print(f'Your final bill is: ${bill}.')
# else:
#     print("Invalid")




