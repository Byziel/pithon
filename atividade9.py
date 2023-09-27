altura=float(input("digite tua altura"))
sexo=(input("digite tua altura(M para masculino, F para feminino)"))
if sexo == "F":
    peso_ideAL=(72.7* altura)-58
else:
    peso_ideAL=(62.1*altura)-44.7
    print(peso_ideAL)
