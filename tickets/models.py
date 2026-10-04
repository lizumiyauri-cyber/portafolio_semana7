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

class TicketConHistorial:
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

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    padre = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE, related_name='subcategorias'
    )

    def __str__(self):
        if self.padre:
            return f"{self.padre} > {self.nombre}"
        return self.nombre


class Ticket(models.Model):
    ESTADOS = [
        ('Abierto', 'Abierto'),
        ('En proceso', 'En proceso'),
        ('Cerrado', 'Cerrado'),
    ]

    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Abierto')
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"