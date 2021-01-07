import subprocess
import pyautogui as magic
import time
import pandas as pd
from datetime import datetime
import threading
import sys
import webbrowser

sys.tracebacklimit=0
read_file = pd.read_csv (r'settings.txt', header = None)
read_file.columns = ['location','starttime','meetingid','meetingpswd']
read_file.to_csv (r'settings.csv', index=None)

sett = pd.read_csv('settings.csv')

locate= sett['location']

def sign_in(meetingid, meetingpswd):
    subprocess.call(locate)

    time.sleep(10)
    join_btn = magic.locateCenterOnScreen('core\join_button.png')
    magic.moveTo(join_btn)
    magic.click()

    meeting_id_btn =  magic.locateCenterOnScreen('core\meeting_id_button.png')
    magic.moveTo(meeting_id_btn)
    magic.click()
    magic.write(meetingid)
	
    meeting_id_btn2 =  magic.locateCenterOnScreen('core\meeting_id.png')
    magic.moveTo(meeting_id_btn2)
    magic.click()
    magic.write(meetingid)
	
    media_btn = magic.locateAllOnScreen('core\media_btn.png')
    for btn in media_btn:
        magic.moveTo(btn)
        magic.click()
        time.sleep(2)

    join_btn = magic.locateCenterOnScreen('core\join_btn.png')
    magic.moveTo(join_btn)
    magic.click()
    
    time.sleep(5)
	
    meeting_pswd_btn1 = magic.locateCenterOnScreen('core\meeting_pswd.png')
    magic.moveTo(meeting_pswd_btn1)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')
	
    meeting_pswd_btn2 = magic.locateCenterOnScreen('core\meeting_pswd_btn.png')
    magic.moveTo(meeting_pswd_btn2)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')
	
    meeting_pswd_btn3 = magic.locateCenterOnScreen('core\meeting_pswd2.png')
    magic.moveTo(meeting_pswd_btn3)
    magic.click()
    magic.write(meetingpswd)
    magic.press('enter')


def waiting():
    while True:
        k = magic.locateCenterOnScreen('core\checkpoint.png')
        if k == None:
            print("waiting to be entered")
            time.sleep(2)
        else:
            magic.moveTo(k)
            magic.press('enter')
            magic.click()
            break
        
thread3 = threading.Thread(target=waiting, daemon = True)

def turnmic():
    while True:
        l = magic.locateCenterOnScreen('core\startmic.png')
        if l == None:
            print("Ready for popups")
            time.sleep(10)
        else:
            time.sleep(4)
            start_video_later = magic.locateCenterOnScreen('core\staymuted.png')
            magic.moveTo(start_video_later)
            magic.click()
            magic.hotkey('alt', 'h')
            sorry1 = "There is something wrong with my device, i dont know why both my microphone and my video camera is not working..."
            magic.write(sorry1)
            magic.press('enter')
            magic.hotkey('alt', 'h')
            magic.click()

thread1 = threading.Thread(target=turnmic, daemon = True)

def noid():
    from linkcred import lst
    isStarted = False
    for i in lst:
        while isStarted == False:
                if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                    webbrowser.open(i[0])
                    isStarted = True


def turnvid():
    while True:
        m = magic.locateCenterOnScreen('core\startvid.png')
        if m == None:
            print("Waiting for further instrutions")
            time.sleep(20)
        else:
            start_video_later = magic.locateCenterOnScreen('core\later.png')
            magic.moveTo(start_video_later)
            magic.click()
            magic.hotkey('alt', 'h')
            sorry2 = "There is something wrong with my device, i dont know why both my microphone and my video camera is not working..."
            magic.write(sorry2)
            magic.press('enter')
            magic.hotkey('alt', 'h')
            magic.click()

thread2 = threading.Thread(target=turnvid, daemon = True)

def meetingend():
    while True:
        en = magic.locateCenterOnScreen('core\meetingend.png')
        if en == None:
            print('Waiting for instructions')
            time.sleep(5)
        else:
            magic.press("enter")
            time.sleep(4)
            magic.hotkey('alt', 'f4')
            print("Waiting for next meeting to start")
            mainq()

thread4 = threading.Thread(target=meetingend, daemon = True)            
                        
def mainq():
    while True:
        curr = datetime.now().strftime("%H:%M")
        nodataid = str(sett.iloc[0,2])
        nodatapswd = str(sett.iloc[0,3])
        if curr in str(sett['starttime']):
            print("Found Meeting ID and Password")
            print("Waiting for starttime")
            row1 = sett.loc[sett['starttime'] == curr]
            meetingid = str(row1.iloc[0,2])
            meetingpswd = str(row1.iloc[0,3])
            sign_in(meetingid, meetingpswd)
            thread3.start()
            thread1.start()
            thread2.start()
            print('signed in')
            meetingend()
        elif nodataid == "meetingid" and nodatapswd == 'meetingpswd':
            print("Found Link")
            print("Waiting for starttime")
            noid()
            thread3.start()
            thread1.start()
            thread2.start()
            print('signed in')
            meetingend()

mainq()
