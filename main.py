import pandas as pd

#Si se muestra el error: Missing optional dependency 'openpyxl'
# import pip
# pip.main(["install", "openpyxl"])

import exploracionDx as e1

data = pd.read_excel('Inmuebles.xlsx')
print(data.head(10))

print(e1.correlacionPares())

import tratamientoDx as tr

print(tr.tratamientoDatos())
