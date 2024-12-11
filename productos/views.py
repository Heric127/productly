from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

import productos
from .forms import productoform
from .models import producto

# Create your views here.


def index(request):
    productos = producto.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    product = producto.objects.get(id=producto_id)

    return render(request, 'detalle.html', context={'producto': product})


def formulario(request):
    if request.method == 'POST':
        form = productoform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = productoform()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
