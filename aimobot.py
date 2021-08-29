import cv2
import numpy as np
import pyautogui as pag
import pygetwindow as pgw
import re
import time
from PIL import ImageGrab


def windowPrep():
    print("In windowPrep")
    alltitles = pgw.getAllTitles()

    # Used string search from https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
    osuwin = [winnm for winnm in alltitles if "osu!" in winnm]
    print( osuwin[0])
    osutab = pgw.getWindowsWithTitle(osuwin[0])
    print("osutab list: ")
    print(osutab)
    print("osutab 1item: ")
    print(osutab[0])

    # Functions and attributes available with pygetwindow: https://pypi.org/project/PyGetWindow/
    # Grab the first osu window's handle for all reference purposes'
    owinobj = osutab[0]
    owinobj.restore()
    owinobj.activate()
    time.sleep(1)


def grabScreenshot():
    print("In grabScreenshot")
    screen1 = pag.screenshot()

    # convert these pixels to a proper numpy array to work with OpenCV
    framebgr = np.array(screen1)
    # convert colors from BGR to RGB
    framergb = cv2.cvtColor(framebgr, cv2.COLOR_BGR2RGB)

    return( framergb )

# Takes an image, applies a lowpass and highpass RGB filter and returns a new image bounded by the
#   low and highpass values
def filterScreenshot(image, lowpass, highpass):
    print("In filterScreenshot")
    mask = cv2.inRange(image,lowpass,highpass) # Create a mask with range
    filteredimage = cv2.bitwise_and(image,image,mask = mask)  # Performing bitwise and operation with mask in img variable

    return(filteredimage)

# Takes an image and houghcircle parameters and returns array of circles (if they exist)
def filterCircle(image, dp, mindist, minrad, maxrad):
    print("In filterCircle")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, mindist,minRadius=minrad,maxRadius=maxrad)
    return(circles)

# Take an image, grab the whites from that image, calucltate circles.
#    grab the blues from that image, calucalte circles
#    grab the slider from image, calucate location?
#    grab the spinner from image, T/F
def processScreenshot(screenshot):
    print("In processScreenshot")
    white_low, white_high = np.array([75,75,75 ]), np.array([200,200,200])
    whiteimg = filterScreenshot(screenshot,white_low,white_high)
    print(whiteimg.shape)
    circles = filterCircle(whiteimg,2.0,20,None,110)
    print(circles)

def displayScreenshot():
    print("In displayScreenshot")
    None

def saveScreenshot():
    print("In saveScreenshot")
    None

#initialize values/variables
running = True

windowPrep()

i = 0
#start main loop
while(running):
    # Grab ORIGINAL screen (oscreen)
    oscreen = grabScreenshot()

    processScreenshot(oscreen)
    displayScreenshot()
    saveScreenshot()
    time.sleep(1)    
    i=i+1
    if( i>10 ):
        running = False

