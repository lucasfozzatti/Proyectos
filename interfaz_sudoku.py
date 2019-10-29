from sudoku import sudok
from api import api


class Interfaz():

    def __init__(self):
        self.tab = api()
        self.Su = sudok(self.tab)

    def jugar(self):
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.Su.tablero[i][j], end=" ")
            print(" ")

        try:
            print("Ingrese fila donde desea poner el numero (0 a 8)")
            f = int(input(">>"))
            if self.verificar_fyc(f) is True:
                print("Ingrese columna donde desea poner el numero (0 a 8)")
                c = int(input(">>"))
                if self.verificar_fyc(c) is True:
                    print("Ingrese numero")
                    n = int(input(">>"))
                    if self.verificar_num(n) is True:
                        print(self.Su.ingresarnum(n, f, c))
                    else:
                        print('Ingrese un numero correcto')
                else:
                    print('Ingrese un numero correcto')
            else:
                print('Ingrese un numero correcto')
        except:
            print('Ingrese un numero correcto')

    def verificar_num(self, n):
        if 1 <= n <= 9:
            return True
        else:
            return False

    def verificar_fyc(self, foc):
        if 0 <= foc <= 8:
            return True
        else:
            return False

    def estado_juego(self):
        if self.Su.ganar() is True:
            return True
        return False

# juego = Interfaz()
# while juego.estado_juego() is not True:
#     juego.jugar()