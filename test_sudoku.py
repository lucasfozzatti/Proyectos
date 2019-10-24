import unittest
from sudoku import sudok


class TestSudoku(unittest.TestCase):

    def setUp(self):

        self.juego = sudok([

            '53xx7xxxx',

            '6xx195xxx',

            'x98xxxx6x',

            '8xxx6xxx3',

            '4xx8x3xx1',

            '7xxx2xxx6',

            'x6xxxx28x',

            'xxx419xx5',

            'xxxx8xx79'

        ])


    def test_columna(self):
        self.assertEqual(self.juego.ingresarnum('8',0,3), "ingrese otro numero")
        self.assertEqual(self.juego.tablero,
            [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
   
    def test_fila(self):
        self.assertEqual(self.juego.ingresarnum('7',5,3),"ingrese otro numero")    
        self.assertEqual(self.juego.tablero,
          [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    def test_bloques(self):
        self.assertEqual(self.juego.ingresarnum('5',0,2),"ingrese otro numero")    
        self.assertEqual(self.juego.tablero,
          [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    def test_tablerox(self):
        self.assertEqual(self.juego.ingresarnum('4',1,0),"coordenada equivocada")    
        self.assertEqual(self.juego.tablero, 
           [['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    def test_gano(self):
       self.juego = sudok([
           '531171111',
           '611195111',
           '198111161',
           '811161113',
           '411813111',
           '711121116',
           '161111281',
           '111419115',
           '11118117x'
          ])
       self.assertEqual("Numero ingresado",self.juego.insertar_numero('4', 8, 8)) 
       self.assertTrue(self.juego.gano())





          

       
    


        




if __name__ == "__main__":

    unittest.main()



