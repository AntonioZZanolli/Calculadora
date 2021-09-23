print("Super calculadora!!")


def soma(numero):
    numero2 = input("Dígite outro número: ")
    return print(float(numero) + float(numero2))


def subtracao(numero):
    numero2 = input("Dígite outro número: ")
    return print(float(numero) - float(numero2))


def divisao(numero):
    numero2 = input("Dígite outro número: ")
    return print(float(numero) / float(numero2))


def multiplicacao(numero):
    numero2 = input("Dígite outro número: ")
    return print(float(numero) * float(numero2))


def escolher_operacao(numero):
    operacao = input("Dígite a operação desejada:")
    if operacao == "/" or "*" or "+" or "-":
        if operacao == "+":
            soma(numero)
        if operacao == "-":
            subtracao(numero)
        if operacao == "/":
            divisao(numero)
        if operacao == "*":
            multiplicacao(numero)


    else:
        print("Operação indisponivel")


def main():
    numero = input("Dígite um número: ")
    escolher_operacao(numero)


main()
