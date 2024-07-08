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

weight = float(input("What is your weight? "))
height = int(input("What is your height in cm? "))
height_meter = height / 100.00
bmi = (weight/height_meter**2)

if bmi < 16:
    print("Severely underweight")
elif 16 <= bmi <= 17:
    print("Moderately underweight")
elif 17 < bmi <= 18.5:
    print("Slightly underweight")
elif 18.5 < bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
elif 30 <= bmi <= 34.9:
    print("Obesity class I")
elif 35 <= bmi <= 39.9:
    print("Obesity class II")
else:
    print("Obesity class III")
