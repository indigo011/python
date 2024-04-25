import csv

with open("data.csv", "r") as file:
    row = list(csv.reader(file,delimiter=","))
    charactere = str(row[1][0])
    qtd = int(row[1][1])
    print(f"Char: {charactere}\nQtd: {qtd}")

with open("data.csv","w") as file:
    csv.writer