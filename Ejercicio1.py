class multiplicacion_rusa:

    @staticmethod
    def multiplicar(a: int, b: int):
        
        if b == 0:
            return 0

        return a + multiplicacion_rusa.multiplicar(a, b - 1)

a = int(input("Ingrese el numero: "))
b = int(input("Ingrese el numero: "))
print("Resultado:", multiplicacion_rusa.multiplicar(a, b))


