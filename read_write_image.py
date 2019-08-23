import numpy as np
import cv2

cap = cv2.VideoCapture(0)

image_counter = 1

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)

   
    # Display the resulting frame
    cv2.imshow('frame',frame)
    # Display fram in BW
    #cv2.imshow('gray',gray)
    key = cv2.waitKey(20)
    # Hit q to exit
    if key & 0xFF == ord('q'):
       	break
    # Hit space to capture image
    elif key & 0xFF == ord(' '):
    	image_name = "img{}.png".format(image_counter)
    	cv2.imwrite(image_name, frame)
    	print('Image taken!')
    	image_counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Display images taken
image_counter -= 1
if image_counter > 1:
	while image_counter > 0:
		image_reader = cv2.imread("img{}.png".format(image_counter))
		print("img{}.png".format(image_counter))
		cv2.imshow("image{}".format(image_counter), image_reader)
		image_counter -= 1
	# Hit any key to close windows
	cv2.waitKey(0)
	cv2.destroyAllWindows()

