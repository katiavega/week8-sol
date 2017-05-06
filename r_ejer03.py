# Escribir una funcion recursiva que encuentre el mayor elemento de una lista
def mayor(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        if l[0] > l[1]:
            return l[0]
        else:
            return l[1]
    elif len(l) > 2:
        return mayor(l[1:])
