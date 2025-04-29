# crear una función que se encargue de calcular el iva a un precio.

def calcular_iva(precio, iva=0.21):
    """
    Calcula el iva de un precio dado.

    Parametros:
    precio (float): El precio al que se calculará el iva.
    iva (floar): la tasa de IVA a aplicar, por defecto es 0.21.

    Return:
    Retorna el precio más el iva.
    """
    precio_con_iva = precio / 1 * iva
    return precio_con_iva


