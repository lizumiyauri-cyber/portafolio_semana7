class CategoriaTicket:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []

    def agregar(self, subcategoria):
        self.subcategorias.append(subcategoria)
        return subcategoria


def recorrer_categorias(nodo, nivel=0):
    print("    " * nivel + "- " + nodo.nombre)
    for hijo in nodo.subcategorias:
        recorrer_categorias(hijo, nivel + 1)

raiz = CategoriaTicket("Soporte Técnico")

hardware = raiz.agregar(CategoriaTicket("Hardware"))
impresoras = hardware.agregar(CategoriaTicket("Impresoras"))
impresoras.agregar(CategoriaTicket("Atascos de papel"))
hardware.agregar(CategoriaTicket("Computadoras"))

software = raiz.agregar(CategoriaTicket("Software"))
software.agregar(CategoriaTicket("Sistema operativo"))
software.agregar(CategoriaTicket("Ofimática"))

redes = raiz.agregar(CategoriaTicket("Redes"))
redes.agregar(CategoriaTicket("Wi-Fi"))
redes.agregar(CategoriaTicket("Internet cableado"))

if __name__ == "__main__":
    recorrer_categorias(raiz)