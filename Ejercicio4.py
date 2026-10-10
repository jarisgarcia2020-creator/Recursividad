class Caminos:

    @staticmethod
    def caminos(n, m):
        if n == 1 or m == 1:
            return 1

        return Caminos.caminos(n - 1, m) + Caminos.caminos(n, m - 1)


filas = int(input("Ingrese número de filas: "))
columnas = int(input("Ingrese número de columnas: "))

print("Número de caminos posibles:", Caminos.caminos(filas, columnas))
