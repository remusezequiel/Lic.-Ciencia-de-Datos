import unittest
from solucion import cantidad_de_filas_valle

class Ej2Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Ej2Test, self).__init__(*args, **kwargs)
        self.method = cantidad_de_filas_valle


    def test_matriz_vacia(self):
        entrada = []
        entrada_copia = entrada.copy()
        salida_esperada = 0
        self.assertEqual(cantidad_de_filas_valle(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_matriz_una_fila_valle(self):
        entrada = [[7, 5, 3, 6]]
        entrada_copia = entrada.copy()
        salida_esperada = 1
        self.assertEqual(cantidad_de_filas_valle(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_matriz_varias_filas_sin_valles(self):
        entrada = [[4, 7, 5, 3], [9, 8, 6, 4], [1, 2, 3, 6]]
        entrada_copia = entrada.copy()
        salida_esperada = 0
        self.assertEqual(cantidad_de_filas_valle(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_matriz_varias_filas_todas_valles(self):
        entrada = [[4, 2, 3, 8], [7, 5, 3, 6], [1, 0, 1, 2]]
        entrada_copia = entrada.copy()
        salida_esperada = 3
        self.assertEqual(cantidad_de_filas_valle(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

    def test_matriz_varias_filas_algunas_valles(self):
        entrada = [[4, 7, 5, 3], [9, 8, 6, 4], [4, 2, 3, 8], [1, 2, 3, 6], [1, 0, 1, 2]]
        entrada_copia = entrada.copy()
        salida_esperada = 2
        self.assertEqual(cantidad_de_filas_valle(entrada), salida_esperada)
        self.assertEqual(entrada, entrada_copia)

if __name__ == '__main__':
    unittest.main(verbosity=2)