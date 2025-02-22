import unittest
from queue import Queue as Cola
from solucion import aprobados_y_desaprobados

class Ej3Test():
    def __init__(self, *args, **kwargs):
        super(Ej3Test, self).__init__(*args, **kwargs)
        self.method = aprobados_y_desaprobados

    def test_sin_examenes(self):
        entrada = Cola()
        correctas = Cola()
        salida_esperada = Cola()
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)

    def test_todos_aprobados_queda_igual(self):
        entrada = construir_cola_con_elementos([[True, False], [True, True, True, True], [False, False]])
        correctas = construir_cola_con_elementos([[True, False], [True, True, True, False], [False, False]])
        salida_esperada = construir_cola_con_elementos([[True, False], [True, True, True, True], [False, False]])
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)

    def test_todos_desaprobados_queda_igual(self):
        entrada = construir_cola_con_elementos([[True, False], [True, True, True, True], [False, False]])
        correctas = construir_cola_con_elementos([[False, True], [False, False, True, False], [True, True]])
        salida_esperada = construir_cola_con_elementos([[True, False], [True, True, True, True], [False, False]])
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)

    def test_desaprobados_antes_que_aprobados(self):
        entrada = construir_cola_con_elementos([[True, False], [True, True, True, True], [False, False], [False, True]])
        correctas = construir_cola_con_elementos([[False, True], [False, False, True, False], [False, False], [False, True]])
        salida_esperada = construir_cola_con_elementos([[False, False], [False, True], [True, False], [True, True, True, True]])
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)
        
    def test_intercalados(self):
        entrada = construir_cola_con_elementos([[True, False], [False, False], [True, True, True, True], [False, True]])
        correctas = construir_cola_con_elementos([[False, True], [False, False], [False, False, True, False], [False, True]])
        salida_esperada = construir_cola_con_elementos([[False, False], [False, True], [True, False], [True, True, True, True]])
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)

    def test_preserva_correctas(self):
        entrada = construir_cola_con_elementos([[True, False], [False, False], [True, True, True, True], [False, True]])
        correctas = construir_cola_con_elementos([[False, True], [False, True], [False, False, True, False], [False, True]])
        salida_esperada = construir_cola_con_elementos([[False, False], [False, True], [True, False], [True, True, True, True]])
        correctas_esperada = construir_cola_con_elementos([[False, True], [False, True], [False, False, True, False], [False, True]])
        aprobados_y_desaprobados(entrada, correctas)
        self.assertEqual(entrada.queue, salida_esperada.queue)
        self.assertEqual(correctas.queue, correctas_esperada.queue)


def construir_cola_con_elementos(elementos: list[list[bool]]) -> Cola[list[bool]]:
    res: Cola = Cola()
    for elem in elementos:
        res.put(elem)
    return res

if __name__ == '__main__':
    unittest.main(verbosity=2)