import os
import cv2
import numpy
import shutil



"""
	Downsize images to 64 x 64 using opencv and also convert to gray scale
"""


def downsize(url):
	print(url)
	image = cv2.imread(url,0)
	#cv2.imshow("orginal",image)
	#plt.imshow(image)


	down_sized = cv2.resize(image,(64,64))

	#down_sized = cv2.cvtColor(down_sized,cv2.COLOR_BGR2GRAY)

	return down_sized

def main():
	folder_name = "resized"
	
	if folder_name not in os.listdir(os.getcwd()):
		os.mkdir(folder_name)
		
	pwd = os.path.join(os.getcwd(),folder_name)

	for f in os.listdir("."):
		if ('.jpg' in f or '.png' in f or '.jpeg' in f) and '_64x64' not in f:
			down_sized = downsize(f)
		
			cv2.imwrite(f[:-4] + "_64x64.png",down_sized)	

		#plt.imshow(down_sized)

	for f in os.listdir("."):
		if "_64x64" in f:
			shutil.move(f,pwd)

:
if __name__ == '__main__':
	main()
