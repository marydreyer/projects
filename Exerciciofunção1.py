'''
lista_de_marcas
[FIAT,GM,FORD,VW,JEEP]
   0   1   2   3   4
0 [FIAT]
1 [GM]
2 [FORD]
3 [VW]
4 [JEEP]

'''

lista_de_marcas = ['FIAT','GM','FORD','VW']

def validar_marca():
    while True:
        #ler uma nova marca
        nova_marca = input('...digite a nova marca: ').upper()
        #verificar se ela ja existe
        if nova_marca not in lista_de_marcas:
            return nova_marca  #se não existir retorna como uma marca válida para o cadastro
            # se existir, pede para digitar novamente
        input('---Erro, Marca ja cadastrada. [ENTER] digita novamente.')

def cadastrar_marca():
    lista_de_marcas.append(validar_marca())

def relatorio_de_marcas():
    for marca in lista_de_marcas:
        print(marca, end=' - ')
    print()

def localiza_indice():
    while True:
        marca_errada = input('...digite a marca a ser alterada:').upper()
        if marca_errada in lista_de_marcas:
            return lista_de_marcas.index(marca_errada)
        else:
            input('---ERRO, marca não cadastrada. [ENTER] Continua.')
    #ler uma marca a ser alterada
    #verificar se esta marca já existe
    #localizar seu indice
def alterar_marca():
    indice = localiza_indice()
    lista_de_marcas[indice] = validar_marca()
    #ler a nova marca
    #realizar a alteração

def valida_marca ():
    marca = input('..digite a marca a ser excluída: ').upper()
    if marca in lista_de_marcas:
       return marca
    else:
        input('---ERRO, Marca não encontrada.[ENTER]')

def excluir_marca():
    lista_de_marcas.remove(valida_marca)


while True:

    escolha = input('''Menu
        0-	Finalizar o Programa
        1-	Cadastrar as marcas
        2-	Listar as marcas cadastradas
        3-	Alterar alguma marca digitada erradamente
        4-	Excluir uma marca da lista
        Escolha:2
         ''')
    if escolha == '0': break
    if escolha == '1': cadastrar_marca()
    if escolha == '2': relatorio_de_marcas()
    if escolha == '3': alterar_marca()
    if escolha == '4': excluir_marca()
