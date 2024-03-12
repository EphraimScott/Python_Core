print("Hello Jesse Freire!")

class funcoes(object):

    def medianum(self):
        a = float(input("Insira um numero: "))
        b = float(input("Insira outro numero: "))
        c = float(input("Insira mais um numero: "))

        media = (a + b + c) / 3

        print(media)


    def icmnum(self):
        Peso = float(input("Insira seu peso: "))
        Altura = float(input("Insira sua altura: "))
        IMC = Peso / Altura ** 2

        print(IMC)


    def eoprofessor(self):
       nome = input("Digite seu nome: ")
       idade = int(input("Insira sua idade: "))

       if (nome == "Rômulo") and (idade == 45):
        print("É o professor")
       else:
        print("Não é o professor")

class intfloatoustr(object):

    def int(self):
        inteiro = input("Digite um numero inteiro: ")

        if type(inteiro) == int:
            print("Esse numero é int")
        else:
            print("Esse provavel numero não é inteiro")

    def float(self):
        flutuante = input("Digite um numero flutuante: ")

        if type(flutuante) == float:
            print("Isso é um numero flutuante")
        else:
            print("Isso provavel numero não é flutuante")

    def true(self):
        verdade = input("Digite um valor boleano: ")

        if type(verdade) == True:
            print("Esse valor é um boleano verdadeiro")
        else:
            print("Esse valor não é boleano verdadeiro")

    def false(self):
        falso = input("Digite um valor boleano: ")

        if type(falso) == False:
            print("Esse valor é um boleano falso")
        else:
            print("Esse valor não é boleano falso")

    def str(self):
        string = input("Digite uma string de texto: ")

        if type(string) == str:
            print("Essa é uma string de texto")
        else:
            print("Essa não é uma string de texto")

    def maioroumenor(self):
        num = float(input("Digite um numero"))
        division = num % 2

        if (num > 6) and (num > 10) and (division == 0):
            print("O numero é maior que 6 e 10 e é par")
        elif (num < 6) and (num < 10) and (division == 0):
            print("O numero é menor que 6 e 10 e é par")
        elif (num > 6) and (num < 10) and (division == 0):
            print("O numero é maior que 6 e menor que dez e é par")
        elif (num > 6) and (num > 10) and (division == 1):
            print("O numero é maior que 6 e 10 e é impar")
        elif (num < 6) and (num < 10) and (division == 1):
            print(" O numero é menor que 6 e 10 e é impar")
        elif (num > 6) and (num < 10) and (division == 1):
            print("O numero é maior que 6 e menor que 10 e é impar")
        else:
            print("Valor não alcaçado pelo codigo")


        while(True):
            menu = int(input("1) Digitar um int \n"
                             "2) Digitar um float \n"
                             "3) Digitar uma str"))

        match(menu):
            case 1: escolha


def main():
    escolha = funcoes()

    while(True):
     menu = int(input("O que deseja fazer? \n"
             "1) Calcular a media \n"
             "2) Calcular o IMC \n"
             "3) Você é o professor?\n"
             "4) Isso é int?\n"
             "5) Maior ou menor? \n"
             "6) Sair"))

     match(menu):
        case 1: escolha.medianum()
        case 2: escolha.icmnum()
        case 3: escolha.eoprofessor()
        case 4: escolha.intfloatoustr()
        case 5: escolha.maioroumenor()
        case 6: break
        case _: print("Tente um numero")

if __name__ == '__main__':
 main()

def sec():
    escolha = intfloatoustr()

    while(True):
        menu2 = int(input("Escolha qual escrever: \n"
                          "1) Inteiro \n"
                          "2) Flutuante \n"
                          "3) String \n"
                          "4) True \n"
                          "5) False \n"
                          "6) String \n"
                          "7) Sair"))

        match(menu2):
            case 1: escolha
