import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import dias_vividos

def test_dias_vividos_un_ano():
    resultado = dias_vividos(1)
    assert resultado == 365, f"Se esperaba 365, pero se obtuvo {resultado}"

def test_dias_vividos_cero_anos():
    resultado = dias_vividos(0)
    assert resultado == 0, f"Se esperaba 0, pero se obtuvo {resultado}"

def test_dias_vividos_varios_anos():
    resultado = dias_vividos(10)
    assert resultado == 3650, f"Se esperaba 3650, pero se obtuvo {resultado}"
