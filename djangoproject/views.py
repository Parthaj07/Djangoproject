from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PatientSignupForm, DoctorSignupForm
from django.contrib.auth.models import User
from doctor.models import Doctor
from patient.models import Patient
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            request.session['user_type'] = 'patient'
            messages.success(request, 'Patient signup successful. Please login.')
            return redirect('patient_login')
        else:
            messages.error(request, 'Invalid form submission. Please check your inputs.')
    else:
        form = PatientSignupForm()
    return render(request, 'patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            request.session['user_type'] = 'doctor'
            messages.success(request, 'Doctor signup successful. Please login.')
            return redirect('doctor_login')
        else:
            error_message = "Form submission error. Please check your inputs."
            for field, errors in form.errors.items():
                error_message += f"\n{field}: {', '.join(errors)}"
            messages.error(request, error_message)
    else:
        form = DoctorSignupForm()
    return render(request, 'doctor_signup.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Received username: {username}, password: {password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")
        if user is not None and hasattr(user, 'patient'):
            login(request, user)
            return redirect('patient_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'patient_login.html')
    return render(request, 'patient_login.html')


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'doctor'):
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'doctor_login.html')
    return render(request, 'doctor_login.html')

def patient_dashboard(request):
    if hasattr(request.user, 'patient'):
        patient = request.user.patient
        return render(request, 'patient_dashboard.html', {'patient': patient})
    else:
        return HttpResponse("You are not authorized to access this page.")

def doctor_dashboard(request):
    if hasattr(request.user, 'doctor'):
        doctor = request.user.doctor
        return render(request, 'doctor_dashboard.html', {'doctor': doctor})
    else:
        return HttpResponse("You are not authorized to access this page.")


