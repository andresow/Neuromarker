from django import forms
from nodes.models import Nodes
from django.forms import ModelForm

class NodesForm(forms.ModelForm):

	class Meta:
		model = Nodes
		fields = [
				'is_red',
				'name',
				'percentage_commission',
		]
		labels = {
				'is_red': 'Propietario de red',
				'name': 'Nombre',
				'percentage_commission': 'Porcentaje de comision',
		}
		widgets = {
				'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'percentage_commission':forms.TextInput(attrs={'class':'form-control form-control-user'}),
	    }
			