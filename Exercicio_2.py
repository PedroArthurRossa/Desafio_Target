number_fibonacci = [0,1]

while True:
    try:
        number_user = int(input("Qual valor deseja verificar na sequencia de fibonacci?\n"))
        break
    except:
        print("Digite um valor válido\n")

while number_user > number_fibonacci[-1]:
    number_fibonacci.append(number_fibonacci[-1]+number_fibonacci[-2])

if number_user in number_fibonacci:
    print("Seu númmero está na sequência de fibonacci")
else:
    print("Seu númmero não está na sequência de fibonacci")
