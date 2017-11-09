import numpy as np
import cv2
import time, threading
import glob
import os
import sys

camera = cv2.VideoCapture(0)

Face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Eye = cv2.CascadeClassifier('haarcascade_eye.xml')
timestr = time.strftime("%Y%m%d%H%M%S")

n = 0
number = 0

def snapTime():
	timestr = time.strftime("%Y%m%d%H%M%S")
	cv2.imwrite('output/capture/capture_'+timestr+'.png',mirror)
	list_of_files = glob.glob('output/capture/*') 
	latest_file = max(list_of_files, key=os.path.getctime)
	print '\n snapped! ', latest_file#, n
	lastPic = cv2.imread(latest_file,0)
	img = cv2.imread(latest_file)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	
	faces = Face.detectMultiScale(gray, 1.4, 5)
	print '\n looking for faces'
	for (x,y,w,h) in faces:
	 	imgCrop = img[y:y+h,x:x+w]
	 	print(" found {0} faces!".format(len(faces)))
	 	cropped = cv2.resize(imgCrop,(400,400))
	 	cv2.imwrite('output/crop/cropped_'+timestr+'.png',cropped)
	threading.Timer(5, snapTime).start()

while(True):
    (grabbed, frame) = camera.read()
    
#    frame = cv2.resize(frame, (1920,1080)) # good
#    frame = cv2.resize(frame, (1280,720))

    mirror = frame[
                   0:1080, # good
                   656:1266 # good
                   ]
    mirror = cv2.flip(mirror, 1)

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Frame", mirror)

    croppedFiles = glob.glob('output/crop/*')

  
    k = cv2.waitKey(1)

    if k & 0xFF == ord('c'):

        threading.Timer(1.0, snapTime).start()


    elif k & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv2.destroyAllWindows()
