#from call_the_police import Model
from mail import send_mail
from label_image import predict
import numpy as np
import cv2
import os


def Test_Video(filename):
	detection_count = 0
	cap = cv2.VideoCapture(filename)

	while True:
		ret,frame = cap.read()
		cv2.imwrite('proof'+str(detection_count+1)+'.png',frame)
		crime = predict('proof1.png')
		#print(crime)
		if crime != 0:
			detection_count += 1
			print(detection_count)

			if detection_count >= 2:
				send_mail(crime,'proof1.png','proof2.png')
				detection_count = 0
		else:
			os.remove('proof1.png')



def Live_Cam():

	cap = cv2.VideoCapture(0)

	while True:
		ret,frame = cap.read()
def main():
	Test_Video('1.mp4')

if __name__ == '__main__':
	main()