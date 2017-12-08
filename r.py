"""Generar tipo de transicion."""
import numpy as np
import random
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
            return "retiro", random.lognormvariate(.7, .4)
        else:
            return "pago", random.lognormvariate(.5, .4)
    else:
        return "deposito", random.lognormvariate(1, .4)


for _ in range(5):
    tipo, ts = generate_request()
