class ColaCircularDinamica:
    def __init__(self, capacidad_inicial=3):
        self.capacidad = capacidad_inicial
        self.arreglo = [None] * self.capacidad
        self.inicio = 0
        self.total = 0

    def esta_llena(self):
        return self.total == self.capacidad

    def encolar(self, valor):
        if self.esta_llena():
            self._crecer()
        pos = (self.inicio + self.total) % self.capacidad
        self.arreglo[pos] = valor
        self.total += 1

    def desencolar(self):
        if self.total == 0:
            return None
        valor = self.arreglo[self.inicio]
        self.inicio = (self.inicio + 1) % self.capacidad
        self.total -= 1
        return valor

    def _crecer(self):
        nueva_cap = self.capacidad * 2
        nuevo = [None] * nueva_cap
        for k in range(self.total):
            nuevo[k] = self.arreglo[(self.inicio + k) % self.capacidad]
        self.arreglo = nuevo
        self.capacidad = nueva_cap
        self.inicio = 0

    def ver_todos(self):
        salida = []
        for k in range(self.total):
            salida.append(self.arreglo[(self.inicio + k) % self.capacidad])
        return salida


def esta_en_lista(codigos, buscado):
    izq = 0
    der = len(codigos) - 1
    while izq <= der:
        centro = (izq + der) // 2
        if codigos[centro] == buscado:
            return True
        elif codigos[centro] < buscado:
            izq = centro + 1
        else:
            der = centro - 1
    return False


lista_atendidos = []
fila_soporte = ColaCircularDinamica(3)


def registrar_turno(codigo):
    fila_soporte.encolar(codigo)


def atender_turno():
    codigo = fila_soporte.desencolar()
    if codigo is None:
        return None
    indice = 0
    for c in lista_atendidos:
        if c >= codigo:
            break
        indice += 1
    lista_atendidos.insert(indice, codigo)
    return codigo


def turno_ya_atendido(codigo):
    return esta_en_lista(lista_atendidos, codigo)


registrar_turno(201)
print("1) registrar 201:", fila_soporte.ver_todos())

registrar_turno(202)
print("2) registrar 202:", fila_soporte.ver_todos())

registrar_turno(203)
print("3) registrar 203:", fila_soporte.ver_todos())

r = atender_turno()
print("4) atender:", r, "| activos:", fila_soporte.ver_todos())

r = atender_turno()
print("5) atender:", r, "| activos:", fila_soporte.ver_todos())

registrar_turno(204)
print("6) registrar 204:", fila_soporte.ver_todos())

print("7) 201 ya atendido?", turno_ya_atendido(201))
print("8) 204 ya atendido?", turno_ya_atendido(204))