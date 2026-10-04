from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from .forms import TicketForm


def lista_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/lista.html', {'tickets': tickets})


def crear_ticket(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tickets')
    return render(request, 'tickets/formulario.html', {'form': form, 'titulo': 'Nuevo ticket'})


def editar_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('lista_tickets')
    return render(request, 'tickets/formulario.html', {'form': form, 'titulo': 'Editar ticket'})