"""Programa que determina si una palabra es isograma o no"""
def is_isogram(string):
    #Se elimina restricción de case sensitive del string y en frases quitar espacios y guiones
    word = string.lower().replace(' ','').replace('-', '')
    #Se comprueba los elementos del conjunto (elimina repetidos) con la dimensión de la palabra
    return len(set(word)) == len(word)