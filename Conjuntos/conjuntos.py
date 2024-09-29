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

conj_a = {1, 2, 3, 4}
conj_b = {2, 3, 4, 5}
print("Union")
print(conj_a.union(conj_b))
print("Intersection")
print(conj_a.intersection(conj_b))
print("Difference")
print(conj_a.difference(conj_b))


