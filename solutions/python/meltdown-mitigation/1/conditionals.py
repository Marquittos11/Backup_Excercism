"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    criticality = False
    if temperature < 800 and neutrons_emitted > 500:
        producto = temperature * neutrons_emitted
        if  producto < 500000:
            criticality = True 
            return criticality           
    return criticality

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current 
    percentage = (generated_power/theoretical_max_power)*100

    if percentage >= 80.0:
        return 'green'
    elif percentage <= 79.9 and percentage >= 60.0:
        return 'orange'
    elif percentage <= 59.9 and percentage >= 30.0:
        return 'red'
    elif percentage <= 29.9:
        return 'black'

    return 'Valor de eficiencia fuera del rango'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    state_code = temperature * neutrons_produced_per_second
    percentage_90 = (threshold * 90)/100
    percentage_10 = (threshold * 110)/100
    if state_code < percentage_90:
        return 'LOW'
    elif state_code <= percentage_10:
        return 'NORMAL'
    else:
        return 'DANGER'