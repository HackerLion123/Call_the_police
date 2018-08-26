from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from random import shuffle
import numpy as np
import os
import sys
import cv2
import h5py

#code = {0:'Kidnapping',1:'Poaching',2:'Robbery',3:'Vehicle theft',4:'Burglary',5:'Physical Assault',6:'Murder',7:'Pickpocketing',8:'Arms trafficking'}
def load_images():
	code = {'Kidnapping':0,'Poaching':1,'Robbery':2,'vehicle theft':3,'Burglary':4,'Physical Assault':5,'Murder':6,'Pickpocket':7,'Arms trafficking':8}
	train_labels = os.listdir('.')
	current = os.getcwd()
	data = np.array([],dtype=np.int32)
	labels = []
	for label in train_labels:

		dir = os.path.join(os.getcwd(),label)

		if os.path.isdir(dir):
			os.chdir(dir)

			for image in os.listdir('.'):
				img = cv2.imread(image)

				try:
					data = np.append(data,img)
					labels.append(code[label])
				except Exception as e:
					print(label)
		os.chdir(current)

	with open('data.csv','w+') as fp:
		for i in range(len(labels)):
			fp.write(labels[i]+','+','.join(data[0].tolist()))

	# h = h5py.File("data.hdf5",'w')
	# h.create_dataset('data',data=data)
	# h.create_dataset('label',data=labels)	

def load_data():
	pass
	#with open('data.csv') as fp:

def main():
	load_images()

if __name__ == '__main__':
	main()
