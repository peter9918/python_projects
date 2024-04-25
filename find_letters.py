import string

alfabet = list(string.ascii_lowercase)

with open(r"C:\temp\Python\curs\guta.txt", "r") as f:
    file_data = f.read()

#print(file_data)

aparente = []

for letter in alfabet:
    aparente.append(file_data.count(letter))

result = list(zip(alfabet, aparente))

for i in result:
    print(f"Litera {i[0]} apare de {i[1]} ori in textul citit")