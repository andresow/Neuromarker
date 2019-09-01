from django import forms
from product.models import Product

class newProduct(forms.ModelForm):

	class Meta:
		model = Product
		CHOICES = [('1', 'Nuevo'), ('2', 'Usado')]
		CHOICES2 = [('Mercado', 'Mercado'), ('Salud y belleza', 'Salud y belleza'),('Televisores', 'Televisores'),('Celulares', 'Celulares'),('Informatica', 'Informatica'),('Tecnologia', 'Tecnologia'),('Electrodomesticos', 'Electrodomesticos'),('Colchones', 'Colchones'), ('Hogar', 'Hogar'),('Libros', 'Libros'),('Moda', 'Moda'),('Bebés', 'Bebés'),('Jugeteria', 'Jugeteria'),('Deportes', 'Deportes'),('Llantas', 'Llantas'),('Bebés', 'Bebés'),('Ferreteria', 'Ferreteria'),('Vehiculos', 'Vehiculos'), ('Comidas', 'Comidas'),('Otros', 'Otros')
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