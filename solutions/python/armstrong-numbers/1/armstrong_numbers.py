def is_armstrong_number(number):
    if number < 0:
        return False

    armstrong = number
    cifras = []

    if number == 0:
        cifras = [0]
    else:
        while number > 0:
            digito = number % 10
            cifras.append(digito)
            number = number // 10

    potencia = len(cifras)

    total = 0
    for i in cifras:
        total += i ** potencia

    return total == armstrong

