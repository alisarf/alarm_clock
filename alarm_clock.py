'''Alarm Clock ~ 1/17/21'''

from playsound import playsound
import datetime

print("What time would you like to wake up?\n")

alarmHour= int(input("Hour:"))
alarmMinutes = int(input("Minute:"))

am_pm = str(input("Is this am or pm?\n"))
print(f"Ok, I have set an alarm for {alarmHour}:{alarmMinutes}")
if am_pm == "pm" :
    alarmHour = alarmHour + 12

while True:
    if(alarmHour == datetime.datetime.now().hour and
       alarmMinutes == datetime.datetime.now().minute):
        print("Wake up!")
        playsound('grandfather_clock.mp3')
        break
