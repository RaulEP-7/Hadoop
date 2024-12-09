#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

# -*- coding: utf-8 -*-

import sys

# Iterar sobre cada linea del stdin
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir por tabuladores
    data = line.strip().split("\t")
    
    # Comprobar que hay exactamente 6 elementos (formato esperado)
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        # Imprimir la salida en formato clave-valor (store, cost)
        print("{}\t{}".format(store, cost))
    else:
        # Si la linea no tiene el formato adecuado, simplemente se ignora
        continue
