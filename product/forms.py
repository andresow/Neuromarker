from django import forms
from product.models import Product

class newProduct(forms.ModelForm):

	class Meta:
		model = Product
		CHOICES = [('1', 'Nuevo'), ('2', 'Usado')]
		fields = [
				'name',
				'description',
				'value',
				'quantity',
				'restriction',
				'state',
				'category',
		]
		labels = {
				'name': 'Nombre',
				'description': 'Descripción',
				'value': 'Precio',
				'quantity': 'Cantidad',
				'restriction': 'Restricción de edad',
				'state': 'Estado de uso',
				'category': 'Categoria',

		}
		widgets = {
				'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'description': forms.Textarea(),
				'value':forms.NumberInput(), 
				'quantity':forms.NumberInput(), 
				'state':forms.Select(choices=CHOICES),
				'category':forms.TextInput(attrs={'class':'form-control form-control-user'}),
		}

       
class ImageForm(forms.Form):
    
 filename = forms.CharField(max_length=100)
 docfile = forms.ImageField(
        label='Selecciona una imagen'
    )