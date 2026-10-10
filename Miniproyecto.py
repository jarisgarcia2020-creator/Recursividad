class ExploradorRecursivo:


    def imprimir_arbol(self, sistema, nivel=0):
        for nombre, contenido in sistema.items():
            print("  " * nivel + nombre)

            if isinstance(contenido, dict):
                self.imprimir_arbol(contenido, nivel + 1)


    def buscar_archivo(self, sistema, nombre, ruta=""):
        for clave, valor in sistema.items():
            nueva_ruta = ruta + "/" + clave

            if isinstance(valor, dict):
                resultado = self.buscar_archivo(valor, nombre, nueva_ruta)
                if resultado:
                    return resultado
            elif clave == nombre:
                return nueva_ruta

        return None

    
    def contar_archivos(self, sistema):
        total = 0

        for nombre, contenido in sistema.items():
            if isinstance(contenido, dict):
                total += self.contar_archivos(contenido)
            else:
                total += 1

        return total


sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}

explorador = ExploradorRecursivo()

print("Arbol de archivos:")
explorador.imprimir_arbol(sistema_archivos)

print("\nBuscar archivo:")
print(explorador.buscar_archivo(sistema_archivos,"vacaciones.png"))

print("\nTotal de archivos:")
print(explorador.contar_archivos(sistema_archivos))