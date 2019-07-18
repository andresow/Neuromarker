from django import forms
from product.models import Product

class newProduct(forms.ModelForm):

	class Meta:
		model = Product
		INTEGER_CHOICES= [tuple([x,x]) for x in range(1,19)]
		CHOICES = [('1', 'Nuevo'), ('2', 'Usado')]
		fields = [
				'name',
				'description',
				'value',
				'quantity',
				'restriction',
				'state',
		]
		labels = {
				'name': 'Nombre',
				'description': 'Descripción',
				'value': 'Precio',
				'quantity': 'Cantidad',
				'restriction': 'Restricción',
				'state': 'Estado de uso',
		}
		widgets = {
				'name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'description': forms.Textarea(),
				'value':forms.NumberInput(), 
				'quantity':forms.NumberInput(), 
				'restriction':forms.Select(choices=INTEGER_CHOICES),
				'state':forms.Select(choices=CHOICES),
		}

# class ProfileForm(forms.ModelForm):

# 	class Meta:
		
# 		model = Profile

# 		fields = [    
# 				'birthday',
# 				'address',
# 		]
# 		labels = {
# 				'birthday': 'Fecha de nacimiento',
# 				'address': 'Direccion',
# 		}
# 		widgets = {
# 				'birthday':forms.DateInput(attrs={'class':'form-control  form-control-user', 'type':'date','id':'myDate','value':'aaaa-mm-dd'}),
# 				'address':forms.TextInput(attrs={'class':'form-control form-control-user'}),
# 		}