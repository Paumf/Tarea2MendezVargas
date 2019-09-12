import tarea2


def test_exito():                           # test de prueba exitosa
    assert tarea2.funcion(5, 1) == (6, 5, 4)


def test_error_2():                         # test de error por A<B
    assert tarea2.funcion(5, 20) == -2


def test_error_1():                         # test de error por valor literal
    assert tarea2.funcion(5, "mgd") == -1
