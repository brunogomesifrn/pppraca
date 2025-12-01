from django.forms import ModelForm
from apps.plantas.models import Planta
from apps.espacos.models import Espaco
from apps.usuarios.models import Usuario

class PlantaForm(ModelForm):
		class Meta:
			model = Planta
			fields = ['nome_popular', 'nome_cientifico', 'id_espaco']
                   
class EspacoForm(ModelForm):
        class Meta:
            model = Espaco
            fields = ['nome', 'imagem']

class UsuarioForm(ModelForm):
        class Meta:
                model = Usuario
                fields = ['email', 'senha']