def is_pangram(sentence):
    panagram = False
    alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    frase = sentence.lower()

    for letra in alfabeto:
        if letra not in frase:
            panagram = False
            break
        else:
            panagram = True

    return panagram