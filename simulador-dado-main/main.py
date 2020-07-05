import random

from time import sleep


class SimuladorDeDado:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 6

    def Iniciar(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)
        print(self.valor_aleatorio)
        sleep(1)
        self.DesejaContinuar()

    def DesejaContinuar(self):
        self.continuar = input('Deseja rolar o dado novamente?(s/n) ')

        if self.continuar == 's':
            self.Iniciar()
        elif self.continuar == 'n':
            print('Encerrando o simulador!')
        else:
            print('Digite "s" para continuar ou "n" para parar.')
            self.DesejaContinuar()


rolar_dados = SimuladorDeDado()
rolar_dados.Iniciar()
