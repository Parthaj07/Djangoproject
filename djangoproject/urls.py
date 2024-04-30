
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('login/patient/', views.patient_login, name='patient_login'),
    path('login/doctor/', views.doctor_login, name='doctor_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

