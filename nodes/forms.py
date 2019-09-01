from django import forms
from nodes.models import Nodes
from django.forms import ModelForm

class NodesForm(forms.ModelForm):

	class Meta:
		model = Nodes
		fields = [
				'name',
				'percentage_commission',
		]
		labels = {
				'name': 'Nombre de la tienda',
				'percentage_commission': 'Porcentaje de comision para tus vendedores',
		}
		widgets = {
				'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'percentage_commission':forms.NumberInput(),
	    }
  

class NodesCodeForm(forms.Form):

	generateCode = forms.CharField(max_length=100)
