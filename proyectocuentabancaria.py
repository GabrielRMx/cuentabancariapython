from os import *
from random import *


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Hola, bienvenido {self.nombre}. → Numero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}$'

    def depositar(self, monto):
        if not monto.isnumeric():
            input('Ha ingresado un monto no permitido.\nPresione enter para volver...')
            return menu()
        elif monto.isnumeric():
            self.balance += int(monto)
            input(f'Ha hecho un deposito de {monto}$, presione enter para volver. ')
            return float(monto)

    def retirar(self, monto):
        if float(monto) > cliente.balance:
            print('Saldo insuficiente.')
            input('Presione enter para continuar...')
        else:
            self.balance -= round(float(monto), 2)
            input(f'Ha hecho un retiro de {monto}$, presione enter para volver. ')


def inicio():
    print('------------------------')
    print('---- BANCO ♦ PYTHON ----')
    print('------------------------\n')
    input('Presione enter para creacion de cuenta. ')


def menu():
    print('---------------------------------------')
    print('Depositar [D] | Retirar [R] | Salir [S]')
    print('---------------------------------------')


def crear_cliente(nombre, apellido):
    numero_cuenta = randint(1000000, 9999999)
    print(f'{nombre} {apellido}, tu cuenta bancaria ha sido creada con exito.')
    return Cliente(nombre, apellido, numero_cuenta, 0)


finalizar_programa = False
opcion = ''

inicio()
cliente = crear_cliente(input('Nombre: '), input('Apellido: '))

while not finalizar_programa or opcion != 'S':
    system('cls')
    print(cliente)
    menu()
    opcion = input('Opcion: ').upper()
    match opcion:
        case 'D':
            system('cls')
            cliente.depositar(input('Monto a depositar: '))
        case 'R':
            system('cls')
            cliente.retirar(input('Monto a retirar: '))
        case 'S':
            print('Gracias. ')
            finalizar_programa = True
