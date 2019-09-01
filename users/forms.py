from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'password1',
				'password2',
		]
		labels = {
				'username': 'Nickname',
				'first_name': 'Nombre',
				'last_name': 'Apellido',
				'email': 'Correo electrónico',
				'password1': 'Contraseña',
				'password2': 'Confirmación de contraseña',
		}
		widgets = {
				'username':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'first_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'last_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'email':forms.TextInput(attrs={'class':'form-control form-control-user'}),
				'password1':forms.CharField(widget=forms.PasswordInput()),
				'password2':forms.CharField(widget=forms.PasswordInput()),
		}	

class ProfileForm(forms.ModelForm):

	class Meta:
		
		model = Profile

		fields = [    
				'birthday',
				'address',
		]
		labels = {
				'birthday': 'Fecha de nacimiento',
				'address': 'Direccion',
		}
		widgets = {
				'birthday':forms.DateInput(attrs={'class':'form-control  form-control-user', 'type':'date','id':'myDate','value':'aaaa-mm-dd'}),
				'address':forms.TextInput(attrs={'class':'form-control form-control-user'}),
		}