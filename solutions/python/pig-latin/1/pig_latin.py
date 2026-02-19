#Función para manejo de frases e impresión de la traducción
def translate(text):
    frase = []
    for palabra in text.split(' '):
        frase.append(translate_word_by_word(palabra))
    traduccion = " ".join(frase)
    return traduccion

def translate_word_by_word(palabra):
    if palabra.isalpha() and palabra.isascii():
        vocales = 'aeiou'
        # Regla 1: Si la palabra empieza con una vocal o en las sílabas xr o yt.
        if palabra.startswith('xr') or palabra.startswith('yt') or palabra[0].lower() in vocales: 
            return(f'{palabra}ay')
        # Regla 2: Si la palabra empieza con una o más consonantes.
        else:
            #Localización de la primera vocal y la letra 'y'
            primera_vocal = 0
            for i, letra in enumerate(palabra):
                if letra in vocales or (letra == 'y' and i > 0):
                    primera_vocal = i
                    break
            
            if palabra.startswith(('qu'), primera_vocal -1):
                primera_vocal +=1

            consonantes = palabra[:primera_vocal]
            resto_text = palabra[primera_vocal:]
            return(f'{resto_text}{consonantes}ay')

    else:
        return(f'El valor de {palabra} es un número o está en español')
