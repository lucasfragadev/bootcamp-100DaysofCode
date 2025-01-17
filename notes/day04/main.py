# Seção 4: Day 4 - Beginner - Randomisation and Python Lists
# Documentação: https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences 

# import random 
# import my_module

# random_integer = random.randint (1, 10)
# print(random_integer)


# Módulos: Módulos individuais / Possibilidade de trabalhar em módulos diferentes em um mesmo projeto. Pessoas differentes etc.
# Uma analogia seria a construção de um carro. Onde cada equipe colabora com uma parte do todo. Um módulo "carro", "pneu", "motor" etc.

# Exemplo da utilização de um módulo simples:
# print(my_module.pi)

# Número float 

# random_float = random.random() # Números entre 0 e 1, mas não adicionar o "1". // 0.00000 ~ 0.9999999
# print(random_float)

# How to create a random decimal (float) number between 0 and 5? / Como criar um número decimal (float) aleatório entre 0 e 5?

# randomFloat = random.random() * 5 # 0.00000 ~ 4.9999999 
# print(randomFloat)

# O projeto "LoveMatch" resolvido com .random

# loveScore = random.randint(1, 100)
# print(f'Your love score is {loveScore}!')

# Criação de um programa para "Heads or Tails" (o velho e bom "cara e coroa" hahaha)

# escolha = input("Cara ou coroa? ").capitalize()
# moeda = random.randint(0,1) # Cara = 0 / Coroa = 1
# if escolha == "Cara" and moeda == 0:
#     print(f'Você escolheu {escolha} e deu CARA! Você ganhou!')
# elif escolha == "Cara" and moeda == 1:
#     print(f'Você escolheu {escolha} e deu COROA! Você perdeu!')
# elif escolha == "Coroa" and moeda == 1: 
#     print(f'Você escolheu {escolha} e deu COROA! Você ganhou!')
# else:
#     print(f'Você escolheu {escolha} e deu CARA! Você perdeu!')

# Outra versão

# escolhaMoeda = input("Cara ou coroa? ").capitalize()
# moedaJogada = random.randint(0,1) # Cara = 0 / Coroa = 1

# resultado = "Cara" if moedaJogada == 0 else "Coroa"

# if escolhaMoeda == resultado:
#     print(f'Você escolheu {escolhaMoeda} e deu {resultado.upper()}! Você ganhou!')
# else:
#     print(f'Você escolheu {escolhaMoeda} e deu {resultado.upper()}! Você perdeu!')

# List / Data Structure

# Definição: estrutura de dados que permite armazenar uma coleção de itens em uma única variável. 
# As listas são mutáveis, o que significa que podem ser modificadas após serem criadas.

# A listas começam, em Python, em 0.

# estadosBrasil = [ 
#     'Acre', 
#     'Alagoas',
#     'Amapá',
#     'Amazonas',
#     'Bahia',
#     'Ceará',
#     'Distrito Federal',
#     'Espírito Santo',
#     'Goiás',
#     'Maranhão',
#     'Mato Grosso',
#     'Mato Grosso do Sul',
#     'Minas Gerais',
#     'Pará',
#     'Paraíba',
#     'Paraná',
#     'Pernambuco',
#     'Piauí',
#     'Rio de Janeiro',
#     'Rio Grande do Norte',
#     'Rio Grande do Sul',
#     'Rondônia',
#     'Roraima',
#     'São Paulo',
#     'Sergipe',
#     'Tocantins'
# ]

# estadosBrasil[4] = "Vitória"

# # Adicionar elemento à lista

# # estadosBrasil.append("Fragaland") # Acrescenta um item ao FINAL da lista
# estadosBrasil.extend(["FragaLand", "Sítio Santa Rita", "Ragna Sky", "Bento Land"])

# print(estadosBrasil)

## Quem vai pagar a conta?

# import random 

# nomes = ["lucas", "rafaela", "junior", "paloma"]  # Lista de nomes separados por ", "
# print(nomes) # Apenas para checar a saída
# quantidadeNomes = len(nomes) # Servirá para saber a quantidade de nomes existente na lista
# print(quantidadeNomes) # Checar saída
# escolhaAleatoria = random.randint(0, quantidadeNomes - 1) # Aa escolha é da primeira posição 0 até a quantidade de nomes que existir -1 
# print(escolhaAleatoria) # Checar saída
# print(f'Quem irá pagar a conta é {nomes[escolhaAleatoria]}') # Aqui é o resultado                

# exemploLista = ["casa", 2, True, "carro", 2.1]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# print(fruits[-5])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][3])