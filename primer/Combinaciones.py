from itertools import combinations

x = 15
a = [12, 1, 2, 3, 8, 3]

for b in combinations(a, 3):
    if sum(b) == x:
        print("La combinacion es: " + str(b))
        break
    else:
        print("No hay combinacion")
        break
