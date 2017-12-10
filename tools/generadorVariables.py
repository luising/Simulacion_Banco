"""Generador de variables."""
import random
import numpy as np
deposito = 18
pago = 4
retiro = 4

total = deposito + pago + retiro

deposito = deposito / total * 100
pago = pago / total * 100
retiro = retiro / total * 100


def generate_request():
    """Generar proposito."""
    r = np.random.random((1))[0] * 100
    if r > deposito:
        if r > deposito + pago:
            return "retiro", random.expovariate(1.65)
        else:
            return "pago", random.lognormvariate(-0.6992, 1.08)
    else:
        return "deposito", random.uniform(0, 2.31)


def generate_tll():
    """Generar tiempo de llegada del siguiente cliente."""
    return random.lognormvariate(0.888, 1.03)
