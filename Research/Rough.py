import pyautogui as pgi
import webbrowser
import time
googlemeet_url="https://meet.google.com/lookup/aplckzgevt?authuser=2&hs=179" #google meet link
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' #chrome path
opening_time = "21:39:00"
Current_time = time.strftime("%H:%M:%S")
while Current_time!=opening_time:
    print(Current_time)
    Current_time = time.strftime("%H:%M:%S")
    time.sleep(1)
if Current_time==opening_time:
    webbrowser.get(chrome_path).open(googlemeet_url)
time.sleep(7)
#print(pgi.position()) - pgi.position() is used to find the position of the element on the screen.
pgi.click(701,446)
time.sleep(8)
#print(pgi.position())
pgi.click(399,583)
time.sleep(2)
#print(pgi.position())
pgi.click(490,583)
time.sleep(2)
pgi.click(994,421)