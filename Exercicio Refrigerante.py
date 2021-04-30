''' Construir um algoritmo que contenha 3 listas:
        •  Nomes de produtos
        •  Preços de cada produto
        •  Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas
'''


lista_bebidas = ['Coca-Cola','Guaraná','Pepsi']
lista_valores = ['5,00','3,75','4,00']
lista_quantidades = ["10","12","13"]



def cadastrar_bebidas():
    print('-----CADASTRO-----')
    lista_bebidas.append(ler_marca('...digite a marca: '))
    lista_valores.append(valor('...digite o valor da bebida: '))
    lista_quantidades.append(estoque("...digite a quantidade de refrigerantes em estoque: "))

def ler_marca(mensagem):
    return input(mensagem).upper()
def valor(mensagem):
    return input(mensagem).upper()
def estoque(mensagem):
    return input(mensagem).upper()

def validar_marca(mensagem):
    while True:
        marca = ler_marca(mensagem)
        if marca in lista_bebidas:
            return marca
        input('ERRO. Marca não existe. [ENTER]')

def bebida_valida(mensagem):
    while True:
        marca = ler_marca(mensagem)
        if marca in lista_bebidas:
            return marca
    input("---ERRO. Bebida nao encontrada.[Enter]")

def relatorio_de_bebidas():
    for index in range(len(lista_bebidas)):
        print(f"    Bebida: {lista_bebidas[index]} Valor: {lista_valores[index]} Estoque:{lista_quantidades[index]}")


def relatorio_por_bebida():
    bebida_esc = bebida_valida("Digite uma bebida: ")
    for ind,bebida in enumerate(lista_bebidas):
        if bebida == bebida_esc:
            print('A bebida escolhida foi: ','\t-', lista_bebidas[ind],lista_valores[ind],lista_quantidades[ind])
        else:
            print('Produto não consta na lista')

def excluir_prod():
        produto_exclui = input('Digite o refrigerante a ser excluido: ').upper()
        for index, produto in enumerate(lista_bebidas):
            if produto == produto_exclui:
                lista_bebidas.pop(index)
            else:
                print('Produto não consta na lista')


while True:
    escolha = input('''Menu
        0-	Finalizar o Programa
        1-	Cadastrar Bebidas
        2-  Lista de Bebidas
        3-	Imprimir a bebida escolhida
        4-	Excluir uma bebida da lista


    Escolha:''')

    if escolha == '0': break
    elif escolha == '1': cadastrar_bebidas()
    elif escolha == '2': relatorio_de_bebidas()
    elif escolha == '3': relatorio_por_bebida()
    elif escolha == '4': excluir_prod()



