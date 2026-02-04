def response(hey_bob):
    # Limpieza de los espacios en blanco al inicio y al final
    hey_bob = hey_bob.strip()

    # Condiciones en el orden correcto de especificidad
    if not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif hey_bob.endswith('?'):
        return 'Sure.'
    else:
        return "Whatever."