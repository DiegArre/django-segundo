from django.shortcuts import render
from time import gmtime, strftime
from datetime import date, datetime
# Create your views here.

def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M:%S %p" , gmtime())
    }
    return render(request,"index.html",context)

#CON DATETIME
def time(request):

    now = datetime.now()

    context = {

        "tiempo" : now.strftime("%m/%d/%Y, %H:%M:%S"),
        "hora": now.strftime("%H"),
        "minuto" :now.strftime("%M"),
        "segundo" : now.strftime("%S"),
        "fecha1": now.strftime("%B %d, %Y")
    }

    return render(request,"time.html",context)


# PRUEBA CON DATETIME 
# from datetime import datetime

# now = datetime.now()
# prueba = datetime.now().strftime("%A, %B %d, %Y")
# print(prueba)

# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)