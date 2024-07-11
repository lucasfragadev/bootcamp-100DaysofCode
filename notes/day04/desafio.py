line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] # Nesse caso temos uma lista com três listas dentro [[], [], []]
print("Encontre o tesouro! Marque um 'X' em um ponto.")
position = input("Qual a posição que o tesouro está? ") # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")


