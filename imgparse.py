import cv2
import numpy as np
import time

print( "Import complete" )

print( "cv2:"+cv2.__version__ )
print( "np:"+ np.__version__ )


img = cv2.imread("output/refimg.png", cv2.IMREAD_COLOR )

#cv2.imshow("screenshot", img)
#
#if cv2.waitKey(10000) == ord("q"):
#    print("Done")
