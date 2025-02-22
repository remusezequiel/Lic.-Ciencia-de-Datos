import unittest
from solucion import palabras_por_consonantes

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertDictEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class Ej1Test():
    def __init__(self, *args, **kwargs):
        super(Ej1Test, self).__init__(*args, **kwargs)
        self.method = palabras_por_consonantes

    def test_textos_sin_palabras(self):
        entrada: str = ""
        entrada_copia: str = ""
        salida: dict[int,int] = {} 
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
        entrada: str = "                  "
        entrada_copia: str = "                  "
        salida: dict[int,int] = {}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
       
    def test_texto_con_una_palabra(self):
        entrada: str = "holatodobien"
        entrada_copia: str = "holatodobien"
        salida: dict[int,int] = {6: 1}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
       
    def test_texto_con_varias_palabras(self):
        entrada: str = "hola todo bien"
        entrada_copia: str = "hola todo bien"
        salida: dict[int,int] = {2: 3}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
       
    def test_texto_con_varias_palabras_distintos_largos(self):
        entrada: str = "holato do bien"
        entrada_copia: str = "holato do bien"
        salida: dict[int,int] = {1: 1, 2: 1, 3: 1}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def test_texto_con_una_palabra_y_espacios(self):
        
        entrada: str = "    holatodobien     "
        entrada_copia: str = "    holatodobien     "
        salida: dict[int,int] = {6: 1}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
        entrada: str = "holatodobien     "
        entrada_copia: str = "holatodobien     "
        salida: dict[int,int] = {6: 1}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)

        entrada: str = "    holatodobien"
        entrada_copia: str = "    holatodobien"
        salida: dict[int,int] = {6: 1}
        res = palabras_por_consonantes(entrada)        
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        

    def test_texto_palabras_de_una_letra(self):
        
        entrada: str = " a e  i F X i M W u"
        entrada_copia: str = " a e  i F X i M W u"
        salida: dict[int,int] = {0: 5, 1: 4}
        res = palabras_por_consonantes(entrada)
        self.assertDictEqualWithUnorderedLists(res, salida)
        self.assertEqual(entrada, entrada_copia)
        
    def assertDictEqualWithUnorderedLists(self, dict1, dict2):
            self.assertEqual(dict1.keys(), dict2.keys(), "Los diccionarios tienen distintias claves.")
            for key in dict1:
                self.assertEqual(dict1[key], dict2[key], f"El valor de la clave '{key}' es distinto")

if __name__ == '__main__':
    unittest.main(verbosity=2)
