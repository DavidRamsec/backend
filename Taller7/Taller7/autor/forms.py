from django import forms
from .models import Autor
class AutorForm(forms.ModelForm):
 class Meta:
    model = Autor
    fields = ['nombre', 'apellido', 'fecha_nacimiento']
    # Opcional: widgets para mejorar la UX, especialmente para la fecha
    widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),}
