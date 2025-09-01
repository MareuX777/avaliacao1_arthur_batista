while True:
    
    altura = float(input("Qual a sua altura?: "))
    peso = float(input("Qual seu peso?: "))
    print("------------------------------------------------------")

    calculoaltu = altura * altura
    imc = peso/calculoaltu

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc <= 25:
        print("Peso normal")
    elif imc <= 30:
        print("Sobrepeso")
    else:
        print("Obesidade")
    print("------------------------------------------------------")
