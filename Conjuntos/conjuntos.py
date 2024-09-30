print(set(([1,2,3,1,3,4])))
print(set("abacaxi"))
print(set(("palio","gol","celta","palio",)))
carro = set(("gol","fusca","fusca","Kombi"))
print(carro)
linguagem = {"Python","java","Python"}
print(linguagem)

#acessar dados no set
nunber = {1, 2, 3, 2, 1, 4}
print(nunber)
nunbers = list(nunber)
print(nunbers)
print(nunbers[2])

#usanndo for
carros = set(("gol","fusca","fusca","Kombi"))
for carro in carros:
    print(carro)

#usanndo enumerate
for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")

# metodos da classe do set

# {}.union métodos union, intersection, difference

conj_a = {1, 2, 3, 4, 5}
conj_b = {2, 3, 4, 5, 6, 1}
conj_c = {8, 0}
print("Union")
print(conj_a.union(conj_b))
print("Intersection")
print(conj_a.intersection(conj_b))
print("Difference")
print(conj_a.difference(conj_b))
print(conj_b.difference(conj_a))
print("Difference symmetric")
print(conj_a.symmetric_difference(conj_b))
print("Issubset")
print(conj_a.issubset(conj_b))
print(conj_b.issubset(conj_a))
print("Issuper")
print(conj_a.issuperset(conj_b))
print(conj_b.issuperset(conj_a))
print("isdisjoint")
print(conj_a.isdisjoint(conj_b))
print(conj_a.isdisjoint(conj_c))
print(conj_c.isdisjoint(conj_b))
print(conj_c.isdisjoint(conj_a))
print("add")
sorteio = {1, 23}
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.clear()
print(sorteio)
sorteio = {1, 23}

sorteio.copy()
print(sorteio)

print("discart")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(5)
print(numeros)
numeros.discard(45)
print(numeros)
print("pop")

numeros.pop()
numeros.pop()
numeros.pop()
print(numeros)
print("remove")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.remove(1)
print(numeros)
print("len")
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(len(numeros))

print("In")
print(1 in numeros)
print(10 in numeros)








