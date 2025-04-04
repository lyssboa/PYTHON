#print("******** Menu ********")
#print("Criar Usuário")
#print("Depositar")
#print("Sacar")

#importação de biblioteca
from datetime import datetime

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
usuario = [] #criei uma lista vazia, pois serão adicionados valores posteriormente
contas = []
agencia ='001'


def menu():

    print('''
     ******** Menu ********
     (1) Criar Usuário
     (2) Criar conta
     (3) Listar Contas
     (s) Sacar
     (d) Depositar
     (e) Extrato
     (q) Sair
    ''')
    return input('Qual opção deseja')

def deposito(valor,saldo):
    #vou receber o valor do depósito e somar ao saldo
    if valor > 0 :
        saldo += valor
        #print mostrando o valor depositado
        print(f'Você depositou R${valor}')

    else:
        print('Valor do deposito inválido.Verifique a quantia digitada.')
    
    return saldo 

def saque(saque,saldo):
    global numero_saques,limite,limite_saques
    # de acordo com a documentação python, váriaveis globais não ficam presas ao limite do escopo da função
    if numero_saques >= limite_saques:
        print('Você atingiu o limite de saques de sua conta. Tente novamente no próximo dia útil.')

    else:
        if saque <= 0:
             print('Saque Inválido. Verifique o valor e tente novamente')
        elif saque > limite:
             print('Valor limite excedido. Verifique o valor e tente novamente')
         elif saque > saldo:
             print('Saldo insuficiente. Verifique o valor e tente novamente')
        else:
            saldo -= saque
             numero_saques += 1
    return saldo

def extrato (saldo):  
    hora = datetime.now() #Obtem a hora atual 
    horaatual = hora.strftime('%d/%m/%Y/ %H:%M')
    print('=============Extrato=============')
    print(f'{horaatual} \nSaldo disponível:{saldo}' )
    print('\n=============Extrato=============')

def sair():
    print('**********Encerrando o sistema.**********')

def novo_usuario(usuario):
    cpf = int(input('Digite seu CPF (Somente números);'))
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print('Usuário já cadastrado na base de dados!')
        return 

    nome = str('Escreva seu nome completo : ')
    data_nascimento = input('Infome a data de nascimento (dd/mm/aa) : ')
    endereço = input('Informe seu endereço (Rua, Número, CEP, Bairro e Cidade)')

    # o append adiciona usuario ao meu banco.

    usuarios.append(f'nome:{nome},data de nascimento:{data_nascimento},endereço:{endereço}')
    print('Cadastro realizado com sucesso!')


while True:
    op = menu()

    if op =='d':
        valor = float(input('Digite o valor do depósito: '))
        saldo = deposito(valor,saldo)
    if op =='s':
        valor = float(input('Digite o valor do Saldo: '))
        saldo = saque(valor,saldo)

    break

