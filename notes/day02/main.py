# Seção 2: Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

# Data Types

# mystery = 734_529.678
# type(mystery)
# print(type(mystery))

# num_char = len(input("Whats your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))
# print(70 + 100.5)


# height = input("Altura: ")
# weight = input("Peso: ")
# weight_int = int(weight)
# height_float = float(height)
# # bmi = weight_int / height_float ** 2 
# bmi = weight_int / (height_float * height_float)
# bmi_int = int(bmi)
# print(bmi_int)

# print (type(8//3))

# import time

# current_age = int(input("Qual a sua idade? "))
# weeks_yr = int(52)
# weeks_max = int(75.5 * weeks_yr)
# time_lived = current_age * weeks_yr
# time_left = weeks_max - time_lived
# time_percentage = ((time_lived/weeks_max)*100)
# time_in_yr = int(time_left / 52)
# time_in_months = time_in_yr * 12
# time_in_days = time_in_months * 30


# print(f"Um ano possui {weeks_yr} semanas. ")
# time.sleep(2)
# print(f"Você deve viver no máximo {weeks_max:.0f} semanas, se estiver morando no Brasil. ")
# time.sleep(2)
# print(f"Dessas semans totais, você já viveu, aos seus {current_age} anos, cerca de {time_lived} semanas, isso representa {time_percentage:.2f}% de todo o tempo que irás viver. ")
# time.sleep(2)
# print(f"Ainda te restam {time_in_yr} anos ou {time_in_months} meses ou {time_left} semanas ou {time_in_days} dias. ")

print("Bem vindo a calculadora de conta! ")
total_conta = input("Qual o valor total da conta? ")
gorjeta = int(input("Quanto de gorjeta pretende dar? 10, 12 ou 15 (%)? "))
qnt_pessoas = input("Quantas pessoas irão dividir a conta? ")
qnt_pessoas_float = float(qnt_pessoas)
total_conta_float = float(total_conta)
total_conta_com_gorjeta = total_conta_float + (total_conta_float * (gorjeta / 100))
print(f"O valor total da conta com a porcentagem aplicada é de {total_conta_com_gorjeta}")
valor_cada = total_conta_com_gorjeta / qnt_pessoas_float
print(f"Por isso, cada pessoa deverá pagar R$ {valor_cada:.2f}. ")