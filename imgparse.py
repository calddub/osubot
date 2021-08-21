import cv2
import numpy as np
import time

print( "Import complete" )

print( "cv2:"+cv2.__version__ )
print( "np:"+ np.__version__ )


image = cv2.imread("output/refimg.png", cv2.IMREAD_COLOR )
print(image.shape)

#resize image
#width,height = 960,540
#image = cv2.resize(image,(width,height))

#cv2.imshow("screenshot", image)
#if cv2.waitKey(10000) == ord("q"):
#    print("Done")

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
if circles is not None:
	print(circles)
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	print(circles)

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	origcombo = np.vstack([image, output])
	#cv2.imshow("output", origcombo)
	#cv2.waitKey(0)
	#cv2.destroyWindow("output")


#lower_range = np.array([75,75,75 ])  # Set the Lower range value of color in BGR
#upper_range = np.array([200,200,200])   # Set the Upper range value of color in BGR
white_low, white_high = np.array([75,75,75 ]), np.array([200,200,200])
mask = cv2.inRange(image,white_low,white_high) # Create a mask with range
whiteimg = cv2.bitwise_and(image,image,mask = mask)  # Performing bitwise and operation with mask in img variable
#	cv2.imshow("output", np.hstack([image, output]))

output = image.copy()
gray = cv2.cvtColor(whiteimg, cv2.COLOR_BGR2GRAY)
#cv2.imshow("output", gray)
#cv2.waitKey(0)
#cv2.destroyWindow("output")

# detect circles in the image
whtcircles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.0, 20,maxRadius=110)
print(whtcircles)
# ensure at least some circles were found
if whtcircles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	whtcircles = np.round(whtcircles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in whtcircles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 255), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	gray2 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

	whtcombo = np.vstack([gray2, output])
	#cv2.imshow("output", whtcombo)
	#cv2.waitKey(0)
	#cv2.destroyWindow("output")




blue_low, blue_high = np.array([100,0,0 ]), np.array([255,110,110])
mask = cv2.inRange(image,blue_low,blue_high) # Create a mask with range
blueimg = cv2.bitwise_and(image,image,mask = mask)  # Performing bitwise and operation with mask in img variable
#	cv2.imshow("output", np.hstack([image, output]))

output = image.copy()
gray = cv2.cvtColor(blueimg, cv2.COLOR_BGR2GRAY)
#cv2.imshow("output", gray)
#cv2.waitKey(0)
#cv2.destroyWindow("output")

# detect circles in the image
blucircles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 20)
print(blucircles)
# ensure at least some circles were found
if blucircles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	blucircles = np.round(blucircles[0, :]).astype("int")

	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in blucircles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 255), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	gray3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

	blucombo = np.vstack([gray3, output])
	#cv2.imshow("output", blucombo)
	#cv2.waitKey(0)
	#cv2.destroyWindow("output")


fullcombo = np.hstack([origcombo,whtcombo,blucombo])

print(fullcombo.shape)

w,h=1600,600
finimage = cv2.resize(fullcombo,(w,h))
cv2.imshow("final", finimage)
cv2.waitKey(0)
cv2.destroyWindow("final")
