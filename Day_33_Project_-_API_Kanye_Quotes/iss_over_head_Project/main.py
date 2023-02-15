import requests
from datetime import datetime
import smtplib

my_mail = "newacc01222023@gmail.com"
password = "pobbfhlzozcaczmz"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5< iss_latitude:
        if MY_LAT +5 > iss_latitude:
            if MY_LONG-5 < iss_longitude:
                if MY_LONG+5 > iss_longitude:
                    return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >=sunset or time_now<=sunrise:
        return True
    
    
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail, to_addrs="azamat.salamatov2004@gmail.com",
                        msg="Subject:LOOK UP FOR ISS\n\nThere is ISS in your area.")

if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs="azamat.salamatov2004@gmail.com",
                            msg="Subject:LOOK UP FOR ISS\n\nThere is ISS in your area.")

