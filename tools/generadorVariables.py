"""Generador de variables."""
import random


def generate_tll():
    """Generar tiempo de llegada del siguiente cliente."""
    tll = random.lognormvariate(3.05653, 1.5459)
    while tll > 219 or tll < 9:
        tll = random.lognormvariate(3.05653, 1.5459)
    return tll


def generate_ts():
    """Generar tiempo de llegada del siguiente cliente."""
    ts = random.lognormvariate(2.84104, 1.043119)
    while ts > 120 or ts < 36:
        ts = random.lognormvariate(2.84104, 1.04311)
    return ts
