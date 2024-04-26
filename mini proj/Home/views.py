from django.shortcuts import render,HttpResponse, resolve_url
from Utils.database import *
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutVaccines(request):
    return render(request,"aboutVaccines.html")

def contact(request):
    return render(request,"contact.html")

def covidCare(request):
    return render(request,"covidCare.html")

def ourDoctors(request):
    return render(request,"ourDoctors.html")

def readMoreFromCovidCare(request):
    return render(request,"readMoreFromCovidCare.html")

def aboutVaccinesShowMore(request):
    return render(request,"aboutVaccinesShowMore.html")

def reportChangeInHealth(request):
    return render(request,"reportChangeInHealth.html")

def shop(request):
    return render(request,"shop.html")

def location(request):
    return render(request,"location.html")

def bookAppointment(request):
    return render(request,"bookAppointment.html")

def age(request):
    return render(request,"age.html")

def ScheduleVaccineLocationEligiblity(request):
    context = {
        "pincodes":execute_select_query("SELECT DISTINCT Pincode from VaccineCenters")
    }
    return render(request,"ScheduleVaccineLocationEligiblity.html",context=context)

def ScheduleVaccineDoseSelect(request):
    return render(request,"ScheduleVaccineDoseSelect.html")

def ScheduleVaccinePreChecks(request):
    return render(request,"ScheduleVaccinePreChecks.html")

def submitAppointment(request):
    vaccineAvaiablilityArray = execute_select_query("""WITH RECURSIVE
        dateIncrementer(x) AS (
            SELECT 1
            UNION ALL
            SELECT x+1 FROM dateIncrementer
            LIMIT 30
        )
        SELECT x as dateIncrementer,vcntr.ID as vcntrID,CenterName,Address,Pincode,PhoneNo,v.ID as vID,VaccineName,Manufacturer,HourlyCapacity,StartHour,EndHour,vstk.DailyAvailability FROM dateIncrementer join VaccineCenters vcntr inner JOIN VaccineCenterStockAvailable vstk on vcntr.ID = vstk.VaccineCenterID INNER JOIN Vaccines v on vstk.VaccineID = v.ID 
        INNER JOIN VaccineCenterSchedules vsch on vsch.VaccineCenterID = vcntr.ID;""")
    vaccineAvaiablilitydict={"arr":vaccineAvaiablilityArray}

    vaccineBookedArray = execute_select_query("select VaccineCenterID,VaccineID,ScheduleStartHour,ScheduleDate,ScheduleStartHour,ScheduleEndHour from Appointments WHERE AppointmentStatus = 'BOOKED' and ScheduleDate BETWEEN date('now','+1 day') and date('now','+30 day');")
    vaccineBookedDict = {"arr":vaccineBookedArray}
    
    context = {
        "vaccineAvaiablilityObject":vaccineAvaiablilitydict,
        "vaccineBookedObject" : vaccineBookedDict
    }
    return render(request,"submitAppointment.html",context=context)

@csrf_exempt
def confirmAppointment(request):
    print(request.POST)
    appointmentID = execute_insert_update_query("""
        INSERT INTO Appointments (UserFirstName,UserLastName,AadharNo,PhoneNo,EmailID,VaccineCenterID,VaccineID,ScheduleDate,ScheduleStartHour,ScheduleEndHour,AppointmentStatus) VALUES 
        ('{0}','{1}','{2}','{3}','{4}',{5},{6},'{7}',{8},{9},'{10}')
    """.format(request.POST['appointmentFirstName'],request.POST['appointmentLastName'],request.POST['appointmentAadharNo'],request.POST['appointmentPhoneNo'],
    request.POST['appointmentEmailID'],request.POST['appointmentVaccinationCenter'],request.POST['appointmentVaccine'],request.POST['appointmentDate'],
    request.POST['appointmentVaccinationSlot'].split(' - ')[0],request.POST['appointmentVaccinationSlot'].split(' - ')[1],'BOOKED'))

    context = {
        "appointmentID":appointmentID
    }
    return render(request,"confirmAppointment.html",context=context)

def viewAppointments(request):
    appointmentArray = execute_select_query("""SELECT va.ID,UserFirstName,UserLastName,AadharNo,va.PhoneNo as userPhoneNo,EmailID,ScheduleDate,ScheduleStartHour,ScheduleEndHour,CenterName,Address,Pincode,VaccineName,AppointmentStatus
FROM Appointments va inner join VaccineCenters vcntr on vcntr.ID = va.VaccineCenterID INNER JOIN Vaccines v on va.VaccineID = v.ID;""")

    appointmentsdict={"arr":appointmentArray}

    context = {
        "appointmentsdict":appointmentsdict
    }
    return render(request,"viewAppointments.html",context=context)