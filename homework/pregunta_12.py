"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.
    """
    import pandas as pd

    df = pd.read_csv('files/input/tbl2.tsv', sep='\t')
    # Ordena por c0 y c5a antes de agrupar
    df = df.sort_values(['c0', 'c5a'])
    grouped = df.groupby('c0').apply(lambda x: ','.join(x['c5a'] + ':' + x['c5b'].astype(str))).reset_index()
    grouped.columns = ['c0', 'c5']
    return grouped