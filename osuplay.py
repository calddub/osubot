import cv2
import numpy as np
import pyautogui as pag
import pygetwindow as pgw
import re
import time


# Identify OSU window (2-3 linse of code)
# Get OSU coordinates (1-2 lines of code)
# Start Capture Loop
#    Grab a screenshot (1 line)
#    Save it  (1-2 lines)


print( "Import complete" )

z1 = pgw.getAllTitles()
# print(z1)
# print( "PGW complete")

# Used string search from https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
osuwin = [winnm for winnm in z1 if "osu" in winnm]
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


#cwinsz  = cwinobj.size
owinsz   = osutab[0].size
print(owinsz)
owintl   = osutab[0].topleft
print(owintl)
# An error that occured while testing: when recording video via "XVID" it seems to only capture an unmoving screenshot

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
outfile = "output5.avi"
# create the video write object
#fourcc = cv2.VideoWriter_fourcc(*'VP80')
#self.filename = file+".webm"   # webm is extension for VP8
# H264 CODEC  - High resource consumption on writes
#fourcc = cv2.VideoWriter_fourcc(*'X264')
#outfile = "output5.mov"    # mov is extension for H264
# MJPG CODEC  - Appears to be decent medium
#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#self.filename = file+".avi"   # avi is extension for mjpg for opencv, not .mjpg!

# Create video file
out = cv2.VideoWriter(outfile, fourcc, 20.0, (SCREEN_SIZE))

#self.fmwd = wd     # Frame Width
#self.fmht = ht     # Frame Height
#self.fps  = fps    # FPS output rate to file
#self.framecnt = 0  # Current count of frame

# Writer that stores the video file
#self.vid = cv2.VideoWriter(self.filename, fourcc, fps, (wd,ht), clr)



for i in range(80):
    print("Running Loop "+str(i))
    # make a screenshot
    #img = pag.screenshot()
    img = pag.screenshot(region=(0, 0, 1920, 1080))
    # pyautogui.locateOnScreen(�Sceenshot.PNG�)
    #winar = pag.locateOnScreen("Command Prompt")
    #print( winar )

    # convert these pixels to a proper numpy array to work with OpenCV
    framebgr = np.array(img)
    # convert colors from BGR to RGB
    framergb = cv2.cvtColor(framebgr, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(framergb)
    time.sleep(1/20)

    # show the frame
    #Pressing "q' to break the loop while [cv2.imshow("screenshot", framergb)] is inactive is ineffective
    #cv2.imshow("screenshot", framergb)
    # if the user clicks q, it exits
    #if cv2.waitKey(1000) == ord("q"):
    #    break

# make sure everything is closed when exited
#cv2.destroyAllWindows()
out.release()

print( "Made it to the end")
