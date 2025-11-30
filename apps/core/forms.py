from django.forms import ModelForm
from apps.plantas.models import Planta

class PlantaForm(ModelForm):
    class Meta:
   		model = Planta
   		fields = ['nome_popular', 'nome_cientifico']