def _is_valid_triangle(sides):
    a, b, c = sorted(sides)
    # Todos los lados deben ser mayores que 0 y cumplir la desigualdad del triángulo.
    return a > 0 and a + b > c

def equilateral(sides):
    if not _is_valid_triangle(sides):
        return False
    # Usar un Set para contar elementos únicos es una forma eficiente.
    # Si solo hay 1 elemento único, todos son iguales.
    return len(set(sides)) == 1

def isosceles(sides):
    if not _is_valid_triangle(sides):
        return False
    # Si hay 1 o 2 elementos únicos, es isósceles (incluye equiláteros).
    return len(set(sides)) <= 2

def scalene(sides):
    if not _is_valid_triangle(sides):
        return False
    # Si hay 3 elementos únicos, todos los lados son diferentes.
    return len(set(sides)) == 3
