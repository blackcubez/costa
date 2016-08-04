from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import request, HttpResponse
from .forms import TicketForm
from .models import Ticket
# Create your views here.

def ticket_create(request):
    form = TicketForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponse("Successfully created")
    return render(request, "tickets/create.html", { "form": form })

def ticket_list(request):
    objList = get_list_or_404(Ticket)
    
    return render(request, "tickets/list.html", { "ticketList": objList })

def ticket_detail(request):
    
    return render(request, "tickets/detail.html")

def ticket_update(request, id=None):
    obj = get_object_or_404(Ticket, id=id)
    form = TicketForm(request.POST or None, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponse("Saved successfully")
    objID = obj.id
    return render(request, "tickets/update.html", { "form": form, "objID": objID })