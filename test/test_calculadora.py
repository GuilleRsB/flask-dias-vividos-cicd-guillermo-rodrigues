from calculadora import dias_vividos

def test_dias_vividos():
    # Prueba básica para verificar la función
    assert dias_vividos(1) == 365
    assert dias_vividos(0) == 0
    assert dias_vividos(10) == 3650
