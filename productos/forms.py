from . import models
from django.forms import ModelForm


class productoform(ModelForm):
    class Meta:
        model = models.producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
