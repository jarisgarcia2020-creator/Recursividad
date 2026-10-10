class Patron:

    @staticmethod
    def imprimir_patron(numero, Contador=1):
        if Contador > numero:
            return

        print("*" * Contador)
        Patron.imprimir_patron(numero, Contador + 1)


n = int(input("Ingrese un número: "))
Patron.imprimir_patron(n)

