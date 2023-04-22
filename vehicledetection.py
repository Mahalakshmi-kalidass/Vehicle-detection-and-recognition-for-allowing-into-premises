import cv2
import numpy
import time
import os
from datetime import datetime
import pytesseract
import dbconnection

def build_tesseract_options(psm=7):
	# tell Tesseract to only OCR alphanumeric characters
	alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	options = "-c tessedit_char_whitelist={}".format(alphanumeric)
	# set the PSM mode
	options += " --psm {}".format(psm)
	# return the built options string
	return options

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
filename = str('car'+dt_string+'.jpg')
print(filename)
cap=cv2.VideoCapture(0)
cap.set(3,540) #width of the frame
cap.set(5,540)
classifier = cv2.CascadeClassifier('//home/balaji//Downloads//code//plate_number.xml')
cropped=[] 
while (True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our car classifier
	cars = classifier.detectMultiScale(gray, 1.4, 2)
	#print(len(cars))
    # Extract bounding boxes for any bodies identified
	#cv2.imshow('video2', frame)
	for (x,y,w,h) in cars:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
		print(x,y,w,h)
		cropped = gray[y:y+h,x:x+w]
		denoise = cv2.GaussianBlur(cropped, (5, 5), 0)
		thresholded_img1 = cv2.adaptiveThreshold(denoise,255,cv2. ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,4)
		#plate = cv2.threshold(denoise, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]		
		cv2.imshow("window1",thresholded_img1)
		configuration = build_tesseract_options(11)
		new_predicted_result = pytesseract.image_to_string(thresholded_img1, lang ='eng',config = configuration  )
		lst= [''.join(e for e in string if e.isalnum()) for string in new_predicted_result.split()]
		filter_new_predicted_result = ''.join(map(str,lst))
		print(filter_new_predicted_result)
		sql = 'SELECT * FROM VEHICLE_DETAILS WHERE VEHICLE_NUMBER = %s'
		dbconnection.select_from_db(sql,filter_new_predicted_result)
	#print(cropped)
	cv2.imshow("window",frame)	
	cv2.waitKey(10)
	if len(cars) !=0:
		#os.chdir(directory)
		print(cv2.imwrite("detectedimages//car.jpg",cropped))
		print("write success")
		
	'''denoise = cv2.GaussianBlur(cropped, (5, 5), 0)
	configuration = build_tesseract_options(7)
	new_predicted_result = pytesseract.image_to_string(denoise, lang ='eng',config = configuration  )
	filter_new_predicted_result= "".join(new_predicted_result.split()).replace(":", "").replace("-", "")
	print(new_predicted_result)'''


