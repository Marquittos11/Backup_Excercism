def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    pasos = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2 
            pasos += 1
        elif number % 2 != 0:
            number = (number * 3) + 1
            pasos += 1 
    return pasos
