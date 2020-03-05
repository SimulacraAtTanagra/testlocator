# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:55:27 2020

@author: sayers
"""

import pyautogui
import time
import os

time.sleep(5)
#pyautogui.click(pyautogui.locateCenterOnScreen('run.png'))
if pyautogui.locateCenterOnScreen('run.png')==None:
    print("None")
else:
    print("Found it!")
    
time.sleep(5)
while not pyautogui.locateCenterOnScreen('run.png')== None:
    print("...Scanning...")
    time.sleep(.25)
else:
    print("Lost it, bossman!")

time.sleep(3) 
print(pyautogui.locateCenterOnScreen('run.png',confidence=0.8))

directory_in_str = 'S:\\desktop\\programs'
def main():
    global statuscode
    statuscode = 0
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for file in os.listdir(directory):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename.endswith(".png"):                  #isolates epub for further action
            if not pyautogui.locateCenterOnScreen(filename) == None:
                pass
            else:
                print(f'{filename} not found.')
                break
                
 
time.sleep(5)                
while statuscode==0:
    main()
