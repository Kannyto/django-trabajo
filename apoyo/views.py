from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import DonationForm, AddPatientForm
from .models import Donacion, AddPatient
# Create your views here.

def home(request):
    donations = Donacion.objects.filter(user=request.user.id)
    return render(request, 'apoyo/home.html', {'donations' : donations})

def signup(request):

    if request.method == 'GET':
        return render(request, 'apoyo/signup.html', {
        'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
            # register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'apoyo/signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'apoyo/signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
                })

def singin(request):
    if request.method == 'GET':
        return render(request, 'apoyo/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate (request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'apoyo/login.html', {
            'form': AuthenticationForm,
            'error': 'El usuario y/o contraseña son incorrectos'
        })
        else:
            login(request, user)
            return redirect('home')
        

def signout(request):
    logout(request)
    return redirect('home')

def addpatient(request):
    if request.method == 'GET':
        return render(request, "apoyo/add_patient.html", {
            'form': AddPatientForm
        })
    else:
        try:
            form = AddPatientForm(request.POST)
            new_patient = form.save(commit=False)
            new_patient.user = request.user
            new_patient.save()
            return redirect('home')
        except ValueError:
            return render(request, "apoyo/add_patient.html", {
                'form': AddPatientForm,
                'error': 'Revisa los datos'
            })


def donate(request):
    if request.method == 'GET':
        return render(request, "apoyo/donate.html",{
            'form': DonationForm
        })
    else:
        try:
            form = DonationForm(request.POST)
            new_donate = form.save(commit=False)
            new_donate.user = request.user
            new_donate.save()
            return redirect('home')
        except ValueError:
            return render(request, "apoyo/donate.html", {
            'form': DonationForm,
            'error': 'Revisa los datos'
            })

#Mostrar donaciones
def donation(request):
    donations = Donacion.objects.filter(user=request.user.id)
    
    return render(request, 'apoyo/donation.html', {'donations' : donations})

#Mostrar personas
def patient(request):
    patients = AddPatient.objects.filter(user=request.user.id)
    
    return render(request, 'apoyo/patient.html', {'patients' : patients})