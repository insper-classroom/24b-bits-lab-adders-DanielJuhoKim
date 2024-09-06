#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]  # (1)

    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    s1 = Signal(bool(0))
    c1 = Signal(bool(0))
    s2 = Signal(bool(0)) 
    c2 = Signal(bool(0))

    half = halfAdder(x[0], y[0], soma[0], c1)
    full = fullAdder(x[1], y[1], c1, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    tamanho = len(x)
    c = [Signal(bool(0)) for i in range(tamanho)]
    full_lista = [None for i in range(tamanho)]

    half = halfAdder(x[0], y[0], soma[0], c[0])
    for elemento in range(tamanho):
        full_lista[elemento] = fullAdder(x[elemento], y[elemento], c[elemento - 1], soma[elemento], c[elemento])
    
    return instances()
