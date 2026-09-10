def is_valid(isbn):
    # 1) limpiar
    isbn = isbn.replace(" ", "").replace("-", "")

    # 2) validación de formato
    if len(isbn) == 10:
        if not isbn[:-1].isdigit():
            return False
        if isbn[-1] != "X" and not isbn[-1].isdigit():
            return False
    elif len(isbn) == 13:
        if not isbn.isdigit():
            return False
    else:
        return False

    # 3) validación de checksum
    if len(isbn) == 10:
        suma = 0
        for i in range(9):
            suma += int(isbn[i]) * (10 - i)
        if isbn[9] == "X":
            suma += 10
        else:
            suma += int(isbn[9])
        return suma % 11 == 0

    if len(isbn) == 13:
        suma = 0
        for i in range(12):
            if i % 2 == 0:
                suma += int(isbn[i])
            else:
                suma += int(isbn[i]) * 3
        check_digit = (10 - (suma % 10)) % 10
        return check_digit == int(isbn[12])

    return False