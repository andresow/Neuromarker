from django import forms
from product.models import Product

class newProduct(forms.ModelForm):

	class Meta:
		model = Product
		CHOICES = [('1', 'Nuevo'), ('2', 'Usado')]
		CHOICES2 = [('1', 'Mercado'), ('2', 'Salud y belleza'),('3', 'Televisores'),('4', 'Celulares'),('5', 'Informatica'),('6', 'Tecnologia'),('7', 'Electrodomesticos'),('8', 'Colchones'), ('9', 'Hogar'),('10', 'Libros'),('11', 'Moda'),('12', 'Bebés'),('13', 'Jugeteria'),('14', 'Deportes'),('15', 'Llantas'),('16', 'Bebés'),('17', 'Ferreteria'),('18', 'Vehiculos'), ('19', 'Comidas'),('10', 'Otros')
		]
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
				'category':forms.Select(choices=CHOICES2),
		}

       
class ImageForm(forms.Form):
    
 filename = forms.CharField(max_length=100)
 docfile = forms.ImageField(
        label='Selecciona una imagen'
    )