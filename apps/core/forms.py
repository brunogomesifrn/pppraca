from django.forms import ModelForm
from apps.plantas.models import Planta, Familia, FotosPlanta
from apps.espacos.models import Espaco
from apps.usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm

class PlantaForm(ModelForm):
		class Meta:
			model = Planta
			fields = ['nome_popular', 'nome_cientifico', 'familia', 'id_espaco']
                   
class EspacoForm(ModelForm):
        class Meta:
            model = Espaco
            fields = ['nome', 'imagem_espaco']

class UsuarioForm(UserCreationForm):
        class Meta:
                model = Usuario
                fields = ['username', 'email']

class FamiliaForm(ModelForm):
        class Meta:
                model = Familia
                fields = ['nome', 'imagem']

class FotosPlantaForm(ModelForm):
        class Meta:
                model = FotosPlanta
                fields = ['planta', 'nome', 'imagem_planta']