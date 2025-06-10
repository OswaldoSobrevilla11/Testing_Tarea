# Aplicación para calcular el área de un triángulo

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo
    
    Args:
        base (float): Base del triángulo
        altura (float): Altura del triángulo
    
    Returns:
        float: Área del triángulo
    
    Raises:
        ValueError: Si la base o altura son <= 0
    """
    # Validar que la base no sea cero o negativa
    if base <= 0:
        raise ValueError("La base debe ser mayor que cero")
    
    # Validar que la altura no sea negativa
    if altura < 0:
        raise ValueError("La altura no puede ser negativa")
    
    # Calcular y retornar el área
    return (base * altura) / 2

def validar_base(base):
    """
    Valida que la base sea un valor positivo
    
    Args:
        base (float): Base a validar
    
    Returns:
        bool: True si la base es válida, False en caso contrario
    """
    return base > 0

def validar_altura(altura):
    """
    Valida que la altura sea un valor no negativo
    
    Args:
        altura (float): Altura a validar
    
    Returns:
        bool: True si la altura es válida, False en caso contrario
    """
    return altura >= 0