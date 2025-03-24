from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.template import loader
from .models import Cliente
from .forms import ClienteForm

def clientes(request):

    if request.method == 'GET':
        meusClientes = Cliente.objects.all().values()

        template = loader.get_template('clientes.html')

        context = {
            "clientes": meusClientes,
        }

        return HttpResponse(template.render(context,request))

    elif request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/consultas/')

        return redirect('/consultas/')