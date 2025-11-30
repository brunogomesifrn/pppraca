from django.forms import ModelForm
from apps.plantas.models import Planta
from apps.espacos.models import Espaco

class PlantaForm(ModelForm):
		class Meta:
			model = Planta
			fields = ['nome_popular', 'nome_cientifico']
                   
class EspacoForm(ModelForm):
        class Meta:
            model = Espaco
            fields = ['nome', 'imagem']