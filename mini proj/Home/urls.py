
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('main.html',views.index,name='home'),
    path('aboutVaccines.html',views.aboutVaccines,name='aboutVaccines'),
    path('contact.html',views.contact,name='contact'),
    path('covidCare.html',views.covidCare,name='covidCare'),
    path('ourDoctors.html',views.ourDoctors,name='ourDoctors'),
    path('readMoreFromCovidCare.html',views.readMoreFromCovidCare,name="readMoreFromCovidCare"),
    path('aboutVaccinesShowMore.html',views.aboutVaccinesShowMore,name="aboutVaccinesShowMore"),
    path('reportChangeInHealth.html',views.reportChangeInHealth,name="reportChangeInHealth"),
    path('shop.html',views.shop,name="shop"),
    path('location.html',views.shop,name="location"),
    path('location.html',views.location,name="location"),
    path('bookAppointment.html',views.bookAppointment,name="bookAppointment"),
    path('age.html',views.age,name="age"),
    path('ScheduleVaccineLocationEligiblity.html',views.ScheduleVaccineLocationEligiblity,name="ScheduleVaccineLocationEligiblity"),
    path('ScheduleVaccineDoseSelect.html',views.ScheduleVaccineDoseSelect,name="ScheduleVaccineDoseSelect"),
    path('ScheduleVaccinePreChecks.html',views.ScheduleVaccinePreChecks,name="ScheduleVaccinePreChecks"),
    path('submitAppointment.html',views.submitAppointment,name="submitAppointment"),
    path('confirmAppointment.html',views.confirmAppointment,name="confirmAppointment"),
    path('viewAppointments.html',views.viewAppointments,name="viewAppointments")
]

