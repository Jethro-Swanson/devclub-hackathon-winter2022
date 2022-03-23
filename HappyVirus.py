# HappyVirus.py
# Created by Jethro Swanson and Jordon Hong
# 30/03/2022
# Purpose: Does various comical things such as changing the users background, creating a large number of files filled with semi-motivational quotes
# on the users desktop and in the file where the virus is, opening happy songs in the users browser, and playing harsh beeps to keep the users focus
# on the stuff the program is doing.

import ctypes
import os
import random 
from time import sleep
import webbrowser
import winsound

def main():    
  functions = (swapBackground, cheerUpBaby, happyBeep, randomDancing)
  swapBackground()
  textFileCreator()
  
#   Constantly wait a random amount of time up to 10 seconds and execute something chaotic ;)
  while True:
    delay = random.randrange(10)
    sleep(delay)
    
    funcNum = random.randrange(0, len(functions))
    
    functions[funcNum]() # call a random function from the functions tuple

#creates a random number of text files in the users system
def textFileCreator():
    
    MOTIVE_QUOTES = ("Study or die!", "You can probably do this?", "Are you sure you don't have homework to do?", "Get on that calculus grind!", "Things probably can't get THAT much worse right?"
                     ,"You're ok!" ,"Don't feel down, most people are also average just like you!" ,"Studying is overrated, you're good at other things too...")

    #creates anywhere from 1 to 200 "happyfiles"
    for i in range(1, random.randrange(2,200)):
        textFileName = ("HappyFile" + str(i) + ".txt")#generates the current files name
        desktopPath = os.path.expanduser("~\\Desktop") #grabs path to the users desktop
        textFilePath = desktopPath + "\\" + textFileName #creates full file path to desktop
        
        #creates a file on desktop, writes a quote to it, and then closes it
        file = open(textFilePath, 'w')
        currFileText = MOTIVE_QUOTES[random.randrange(0,len(MOTIVE_QUOTES))] #randomly selects a motivational quote for this file
        file.write(currFileText)                       
        file.close()
        
        #creates a duplicates of files in the same directory as as the virus
        textFilePath = textFileName
        file = open(textFilePath, 'w')
        currFileText = MOTIVE_QUOTES[random.randrange(0,len(MOTIVE_QUOTES))] #randomly selects a motivational quote for this file
        file.write(currFileText)                       
        file.close()
      
      
        # If file doesn't exist, create a new one, then open it. If it does exist, we just open the existing file
        if not os.path.isFile(textFilePath):
          currFileText = MOTIVE_QUOTES[random.randrange(0, len(MOTIV_QUOTES))]  # randomly select a quote
          file = open(textFilePath, 'w')
          file.write(currFileText)
          file.close()
          
        os.startfile(textFileName) # run the text file with default application
      

#swaps users background for a randomly selected one
#HappyPics must be in same directory as this file
def swapBackground():
    NUM_PICS = 5
    
    backgroundFilePath = "HappyPic" + str(random.randrange(1,NUM_PICS +1)) + ".jpg" #randomly chooses a provided img
    directoryName = os.path.dirname(os.path.abspath(__file__)) #gets the directory where this file is located

    ctypes.windll.user32.SystemParametersInfoW(20, 0, directoryName + "\\" + backgroundFilePath, 0) #replaces the users wallpaper with file located at backgroundFilePath
    
def cheerUpBaby():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=o2yY_58QhuA') # open a new tab in the default browser to a youtube video
    
def randomDancing():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=O-oS_M96dQY') # open a new tab to a different video

#plays a series of beep sounds to keep the users attention
def happyBeep():
  
  #plays 9 beeps of varying intensity and length
  for i in range(1,10):
    hzVariance = 100 * random.randrange(1,5)
    winsound.Beep(300 + hzVariance,100 * random.randrange(1,20))
    
if __name__ == "__main__":
    main()
    
