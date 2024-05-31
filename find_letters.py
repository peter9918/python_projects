import string

alfabet = list(string.ascii_lowercase)

path = ""

with open(path, "r") as f:
    file_data = f.read()

aparente = []

for letter in alfabet:
    aparente.append(file_data.count(letter))

result = list(zip(alfabet, aparente))

for i in result:
    print(f"Litera {i[0]} apare de {i[1]} ori in textul citit")