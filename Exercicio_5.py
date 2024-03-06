texto = " " + input("Qual a frase que deseja inverter?\n")
texto_novo = []

for i in range(1,len(texto)):
    texto_novo.append(texto[-i])

print("".join(texto_novo))
