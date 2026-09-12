from django.db import models


class Pila:
    def __init__(self):
        self._elementos = []

    def push(self, dato):
        self._elementos.append(dato)

    def pop(self):
        if self.isEmpty():
            return None
        return self._elementos.pop()

    def isEmpty(self):
        return len(self._elementos) == 0


class Ticket:
    def __init__(self, codigo, estado_inicial="Abierto"):
        self.codigo = codigo
        self.estado_actual = estado_inicial
        self._historial_estados = Pila()

    def cambiar_estado(self, nuevo_estado):
        self._historial_estados.push(self.estado_actual)
        self.estado_actual = nuevo_estado

    def deshacer_ultimo_cambio(self):
        estado_anterior = self._historial_estados.pop()
        if estado_anterior is not None:
            self.estado_actual = estado_anterior
        return self.estado_actual
    # cambio-1