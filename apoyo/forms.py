from django import forms
from .models import Donacion, AddPatient

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['Nombre', 'Apellidos', 'Celular', 'Direccion', 'Comuna', 'Monto']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'Celular': forms.NumberInput(attrs={'style': '-webkit-appearance: none', 'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Comuna': forms.TextInput(attrs={'class': 'form-control'}),
            'Monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = AddPatient 
        fields = ['Nombre', 'Apellidos' , 'Run' , 'Genero', 'Direccion', 'Comuna']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'Run': forms.TextInput(attrs={'class': 'form-control'}),
            'Genero': forms.Select(attrs={'class': 'form-control'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'Comuna': forms.TextInput(attrs={'class': 'form-control'}),
        }