# Archivo con las funciones de testing para el cálculo del área del triángulo

import pytest
from triangulo import area_triangulo, validar_base, validar_altura

def test_area_triangulo_correcto():
    """
    Prueba que valida el resultado cuando la base sea 5 y la altura sea 7
    Área esperada: (5 * 7) / 2 = 17.5
    """
    resultado = area_triangulo(5, 7)
    assert resultado == 17.5

def test_base_negativa():
    """
    Prueba que valida que no se acepten valores negativos para la base
    """
    with pytest.raises(ValueError, match="La base debe ser mayor que cero"):
        area_triangulo(-3, 5)

def test_altura_negativa():
    """
    Prueba que valida que no se acepten valores negativos para la altura
    """
    with pytest.raises(ValueError, match="La altura no puede ser negativa"):
        area_triangulo(5, -3)

def test_base_cero():
    """
    Prueba que valida que la base no sea cero
    """
    with pytest.raises(ValueError, match="La base debe ser mayor que cero"):
        area_triangulo(0, 5)

def test_validar_base_positiva():
    """
    Prueba adicional para la función validar_base con valor positivo
    """
    assert validar_base(5) == True

def test_validar_base_cero():
    """
    Prueba adicional para la función validar_base con valor cero
    """
    assert validar_base(0) == False

def test_validar_base_negativa():
    """
    Prueba adicional para la función validar_base con valor negativo
    """
    assert validar_base(-3) == False

def test_validar_altura_positiva():
    """
    Prueba adicional para la función validar_altura con valor positivo
    """
    assert validar_altura(7) == True

def test_validar_altura_cero():
    """
    Prueba adicional para la función validar_altura con valor cero
    """
    assert validar_altura(0) == True

def test_validar_altura_negativa():
    """
    Prueba adicional para la función validar_altura con valor negativo
    """
    assert validar_altura(-5) == False

def test_area_triangulo_decimales():
    """
    Prueba adicional con valores decimales
    """
    resultado = area_triangulo(2.5, 4.2)
    assert resultado == 5.25