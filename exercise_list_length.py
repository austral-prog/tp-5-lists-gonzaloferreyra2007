# Ejercicio 1: Obtener la longitud de una lista

def list_length(lista):
    """
    Retorna la cantidad de elementos en la lista.

    Args:
        lista: Una lista de cualquier tipo de elementos

    Returns:
        Un entero con la cantidad de elementos
    """
    pass  
    return len(lista)

mi_lista = input("ingrese su lista separada por espacio: ").split()
lista_final = len(mi_lista)
print(lista_final)