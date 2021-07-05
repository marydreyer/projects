from abc import ABCMeta, abstractmethod

#=-=-=-=-=-=-=-=-=-=-=-=-=-TORRES-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Torre:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()

    @abstractmethod
    def getImprimir(self):
        print('\nID: {} \nTorre: {} \nEndereco: {}\n'.format (self.id, self.nome, self.endereco))
    
    def cadastrar(self):
        self.id = int(input("Insira o ID da Torre: "))
        self.nome = str(input("Nome da Torre: "))
        self.endereco = str(input("Endereço da Torre: "))
        print('Cadastro feito com sucesso')

#=-=-=-=-=-=-=-=-=-=-=-=-=-APARTAMENTOS-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=       
class Apartamento():
    def __init__(self):
        self.id = int()
        self.numero_apt = str()
        self.torre = None
        self.garagem = int()
        self.proximo = None
        
    @abstractmethod
    def getImprimir(self):
        print('\nID: {}\nTorre: {}\nApt: {}\nNumero da garagem: {}'.format (self.id, self.torre.nome, self.numero_apt, self.garagem))
    
    def cadastrar(self,valor):
        self.id = int(input("ID do Apartamento: "))
        self.numero = str(input("Número do Apartamento: "))
        self.torre = valor
        print('Cadastro feito com sucesso')
#=-=-=-=-=-=-=-=-=-=-=-=-=-NO-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

#=-=-=-=-=-=-=-=-=-=-=-=-=-ESTACIONAMENTO FILA-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Estacionamento:

    def __init__( self, max_vagas ):
        self.max_vagas = max_vagas
        self.vagas_ocupadas = 0
        self.inicio = None
        self.fim = None

    def maximo( self ):
        return self.max_vagas

    def disponivel( self ):
        return self.max_vagas - self.vagas_ocupadas

    def ocupadas( self ):
        return self.vagas_ocupadas

    def entra( self, valor ):
        no = No(valor)
        if self.vagas_ocupadas == 0:
            self.inicio = no
            self.fim = no
        elif self.vagas_ocupadas == self.max_vagas:
            raise Exception('Garagem esta cheia!')
        else:
            self.fim.proximo = no
            self.fim = no
        self.vagas_ocupadas += 1

    def saida( self ):
        if( self.vagas_ocupadas == 0 ):
            raise Exception('Garagem esta vazia!')
        elif self.vagas_ocupadas == 1:
            self.inicio = None
            self.fim = None
            self.vagas_ocupadas -= 1
        else:
            self.inicio = self.inicio.proximo
            self.vagas_ocupadas -= 1

n = int(input('Entre o numero maximo de veiculos : '))

e = Estacionamento(n)


#=-=-=-=-=-=-=-=-=-=-=-=-=-MAIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#cadastro de torres
Bowsers_Castle = Torre()
Bowsers_Castle.cadastrar()
Bowsers_Castle.getImprimir()

Peach_Castle = Torre()
Peach_Castle.cadastrar()
Peach_Castle.getImprimir()

#cadastro de apartamentos
apt1 = Apartamento()
apt1.cadastrar(Peach_Castle )
apt1.getImprimir()

apt2 = Apartamento()
apt2.cadastrar(Bowsers_Castle)
apt2.getImprimir()

#estacionamento
e.entra()
e.entra(1)
e.saida()
print( 'Maximo de vagas: ',e.maximo() )
print( 'Vagas disponiveis: ',e.disponivel() )
print( 'Vagas ocupadas: ',e.ocupadas() )
e.saida()
e.saida()
print( 'Maximo de vagas: ',e.maximo() )
print( 'Vagas disponiveis: ',e.disponivel() )
print( 'Vagas ocupadas: ',e.ocupadas() )