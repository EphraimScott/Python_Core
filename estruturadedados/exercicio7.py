print("Olá! Somos da clínica São Francisco de Assis")
print("Você é o nosso digitador!")
lista = []
while True:
    op = int(input("Escolha uma opção: \n"
                   "0) Cadastrar uma materia: \n"
                   "1) Cadastrar uma modulo \n"
                   "2) Sair"))
    if op == 0:
        break
    else:
        esp = input("Digite a materia: ")
        lista.append(esp)
for e in lista:
    print(e)
print(type(lista))