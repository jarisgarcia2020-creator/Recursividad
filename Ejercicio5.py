class FlattenList:

    @staticmethod
    def aplanar(lista):
        if not lista:
            return []

        primero = lista[0]
        resto = lista[1:]

        if isinstance(primero, list):
            return FlattenList.aplanar(primero) + FlattenList.aplanar(resto)
        else:
            return [primero] + FlattenList.aplanar(resto)


entrada = eval(input("Ingrese una lista: "))
print("Lista plana:", FlattenList.aplanar(entrada))