from te import Te

instacia_1 = Te()
instancia_2 = Te()

tipo1 =type(instacia_1)
tipo2 = type(instancia_2)

print(tipo1)
print(tipo2)

if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos son de distinto tipo")

