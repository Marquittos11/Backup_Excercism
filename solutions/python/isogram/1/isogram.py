"""Programa que determina si una palabra es isograma o no"""
def is_isogram(string):
    """Se elimina restricción de case sensitive al transformar a minúscula el string y quitar espacios y guiones"""
    word = string.lower().replace(' ',"").replace('-', '')
    """Se comprueba los elementos del conjunto (elimina repetidos) con la dimensión de la palabra"""
    return len(set(word)) == len(word)