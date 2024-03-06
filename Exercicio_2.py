number_fibonatti = [0,1]

while True:
    try:
        number_user = int(input("Qual valor deseja verificar na sequencia de fibonnati?\n"))
        break
    except:
        print("Digite um valor válido\n")

while number_user > number_fibonatti[-1]:
    number_fibonatti.append(number_fibonatti[-1]+number_fibonatti[-2])

if number_user in number_fibonatti:
    print("Seu númmero está na sequência de fibonnati")
else:
    print("Seu númmero não está na sequência de fibonnati")
