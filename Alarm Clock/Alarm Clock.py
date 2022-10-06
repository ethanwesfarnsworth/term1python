# Ethan Farnsworth
# 09.28.22
# Soviet Anthem




# imports
from tkinter import *
from tkinter import ttk
from tkinter import font

import winsound
import time
import calendar
import datetime

alh = ""
alm = ""
als = ""
t = ""



# time zones
# UTC +14   LINT = 14
# UTC +13   NZDT = 13
# UTC +12   ANAT = 12
# UTC +11   SBT = 11
# UTC +10   AEST = 10
# UTC +9    JST = 9
# UTC +8    CST = 8
# UTC +7    WIB = 7
# UTC +6    BST = 6
# UTC +5    UZT = 5
# UTC +4    GST = 4
# UTC +3    MSK = 3
# UTC +2    CEST = 2
# UTC +1    BST = 1
# UTC -1    GMT -= 1
# UTC -2    CVT -= 2
# UTC -3    WGST -= 2
# UTC -4    ART -= 2
# UTC -5    EDT -= 2
# UTC -6    CDT -= 2
# UTC -7    CST -= 2
# UTC -8    PDT -= 2
# UTC -9    AKDT -= 2
# UTC -10   HDT -= 10
# UTC -11   NUT -= 11
# UTC -12   AoE -= 12


# Clock
def getTimeString(h,m,s,t):
    total_seconds = calendar.timegm(time.gmtime()) # Current amount of seconds since 1970
    cur_sec = total_seconds%60  # converts the gm time into seconds in a year
    total_mins = total_seconds//60  # converts the total seconds into total minutes since 1970
    cur_min = total_mins % 60  # converts the total seconds into minutes in a year
    total_hours = total_mins//60  # converts the total minutes into hours since 1970
    cur_hours = total_hours % 24  # converts the total minutes into hours in a year
    am_pm_tag = ""
    if cur_hours >= 12:
        cur_hours = cur_hours-12
        am_pm_tag = "PM"
        if cur_hours == 0:
            cur_hours = cur_hours + 12
    else:
        "AM"
        if cur_hours == 0:
            cur_hours = cur_hours + 12

    xmin= str(cur_min)
    xsec= str(cur_sec)


    if cur_min < 10:
        xmin = "0+"+str(cur_min)
    if cur_sec < 10:
        xsec = "0"+str(cur_sec)

    alarm = str.format("Current Time is: {:2}:{}:{} " ,alh,alm,als,t)



    timeString = str.format("Current Time is: {:2}:{}:{} " ,cur_hours,xmin,xsec)

    if getTimeString == alarm:
        alarm_snd()

    return timeString


# Da Song
def alarm_snd():
    for i in range(10):
        winsound.Beep(391, 200)
        winsound.Beep(523, 400)
        winsound.Beep(391, 300)
        winsound.Beep(440, 100)
        winsound.Beep(493, 400)
        winsound.Beep(329, 200)
        winsound.Beep(329, 200)
        winsound.Beep(440, 400)
        winsound.Beep(391, 300)
        winsound.Beep(349, 100)
        winsound.Beep(391, 400)
        winsound.Beep(261, 200)
        winsound.Beep(261, 200)
        winsound.Beep(293, 400)
        winsound.Beep(293, 300)
        winsound.Beep(329, 100)
        winsound.Beep(349, 400)
        winsound.Beep(349, 300)
        winsound.Beep(391, 100)
        winsound.Beep(440, 400)
        winsound.Beep(493, 200)
        winsound.Beep(523, 200)
        winsound.Beep(587, 600)
        winsound.Beep(391, 200)
        winsound.Beep(659, 400)
        winsound.Beep(587, 300)
        winsound.Beep(523, 100)
        winsound.Beep(587, 400)
        winsound.Beep(493, 200)
        winsound.Beep(391, 200)
        winsound.Beep(523, 400)
        winsound.Beep(493, 300)
        winsound.Beep(440, 100)
        winsound.Beep(493, 300)
        winsound.Beep(329, 200)
        winsound.Beep(329, 200)
        winsound.Beep(440, 400)
        winsound.Beep(391, 300)
        winsound.Beep(349, 100)
        winsound.Beep(391, 400)
        winsound.Beep(261, 300)
        winsound.Beep(261, 100)
        winsound.Beep(523, 400)
        winsound.Beep(493, 300)
        winsound.Beep(440, 100)
        winsound.Beep(391, 800)




def show_time():
    global h
    global m
    global s
    global t
    time = getTimeString(h,m,s,t)
    textvar.set(time)
    root.after(1000,show_time)















# Da GUI
root = Tk() # create the tkinter object to work with
root.geometry("500x500") # set the size of the window
root.attributes("-fullscreen",False) # change the full screen setting
root.configure(background='Black') # setting the background color
root.title("Soviet Alarm Clock") # Sets the Title of the window
textvar = StringVar()

lbl = ttk.Label(root,textvariable= textvar)

lbl.place(relx=0.5, rely=0.5, anchor= CENTER)

root.mainloop()