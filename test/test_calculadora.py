# tests/test_calculadora.py

# Importa la función que se desea testear. Si no se extrajo la lógica,
# puedes copiar la función desde app.py a un módulo llamado calculadora.py.
from calculadora import dias_vividos

def test_dias_vividos_un_ano():
    # Prueba que 1 año equivale a 365 días
    resultado = dias_vividos(1)
    assert resultado == 365, f"Se esperaba 365, pero se obtuvo {resultado}"

def test_dias_vividos_cero_anos():
    # Prueba el caso límite de 0 años
    resultado = dias_vividos(0)
    assert resultado == 0, f"Se esperaba 0, pero se obtuvo {resultado}"

def test_dias_vividos_varios_anos():
    # Prueba con otro valor, por ejemplo, 10 años
    resultado = dias_vividos(10)
    assert resultado == 3650, f"Se esperaba 3650, pero se obtuvo {resultado}"
