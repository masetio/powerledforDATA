   
"""
Python LED Google Calendar
K. M. Loeffler, 2018
kevinmloeffler.com
An application to demonstrate how LED displays that use the PowerLed software
can be automated to display dynamic content from the internet. This is best
run on an idle PC, like an old laptop you are upcycling. Personally, I run this
on an Intel Atom compute stick. Follow the instructions in the README as far as
how to create your credentials and how to get started.
"""
from __future__ import print_function
#from apiclient.discovery import build
##from dateutil import tz, parser
#from httplib2 import Http
#from oauth2client import file, client, tools
from pywinauto.application import Application
import datetime
import subprocess
import time

# Path to PowerLed installation directory
power_led_dir = 'C:\Program Files (x86)\PowerLed\PowerLed.exe'
# PowerLed window name
window_name = 'Led.ledprj - PowerLed V2.89.4'
# Sign WiFi name
sign_wifi_name = 'TF-WIFI_8BE602'
# Your WiFi name
your_wifi_name = 'FILLTHISIN'
# Your timezone
#t_zone = tz.gettz('America/Denver')
# Update time in seconds
updateTime = 60*3

while True:
    #open file rates.txt
    lines =[]
    with open('rates.txt') as f:
        lines= f.readlines()
    dataRate=int(lines[0].strip())
    with open('dis.txt') as f:
        lines= f.readlines()
    disRate=int(lines[0].strip())
    finalRate=round(dataRate*(100-disRate)/100)
    # Open the template and read it in, then replace keywords with our display
    # strings so that we can use this file in PowerLed
    #dataRate=" 260"
    #input file
    fin = open("pop.ledprj", "rt")
    #output file to write the result to
    fout = open("led.ledprj", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('REPLACE1', ' '+str(finalRate)))
    #close input and output files
    fin.close()
    fout.close()    
    # Need to connect to the LED sign
    # Assumes you have already connected to it before!
    # process = subprocess.Popen(
    #         'netsh wlan connect {0}'.format(sign_wifi_name),
    #         shell=True,
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # # Open PowerLed
    app = Application().start(power_led_dir)
    window = app.window(best_match=window_name)
    time.sleep(30)
    window.menu_select("Tools(T)->Search Panel")
    time.sleep(5)
    okWindow = app.window(best_match='Progress')
    okWindow.Ok.click()
    window.menu_select("Tools(T)->Send All")
    time.sleep(5)
    window.menu_select("File(F)->Quit(X)")
    exitWindow = app.window(best_match='PowerLed')
    exitWindow.Yes.click()
    # Need to connect back to your WiFI network
    # Assumes you have already connected to it before!
    # ReconnectProcess = subprocess.Popen(
    #         'netsh wlan connect \"{0}\"'.format(your_wifi_name),
    #         shell=True,
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE)
    # stdout, stderr = ReconnectProcess.communicate()
    time.sleep(updateTime)
