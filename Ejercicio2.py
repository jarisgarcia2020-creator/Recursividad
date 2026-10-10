class Contar_Vocales:

    @staticmethod
    def contar(cadena: str):
        if cadena == "":
            return 0

        vocales = "aeiou"
        if cadena[0].lower() in vocales:
            return 1 + Contar_Vocales.contar(cadena[1:])

        return Contar_Vocales.contar(cadena[1:])


texto = input("Ingrese un texto: ")
resultado = Contar_Vocales.contar(texto)
print("Cantidad de vocales:", resultado)