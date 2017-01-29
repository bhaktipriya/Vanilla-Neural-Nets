import numpy as np
import scipy.misc
import copy
import scipy.ndimage.interpolation
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def parse(filename):
	content = [line.rstrip('\n') for line in open(filename)]
	digits = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
	for ll in xrange(0,len(content),33):

		#print ll
		digit_and_label = copy.deepcopy(content[ll:ll+33])
		digit_ = copy.deepcopy(np.zeros([32,32]))
		digit_ = copy.deepcopy([list(line) for line in digit_])
		for i in xrange(32):
			for j in xrange(32):
				if digit_and_label[i][j]=='1':
					digit_[i][j] = int(255)

		num = int(digit_and_label[32])
		a = copy.deepcopy(np.array(digit_))
		#print num
		# print a.shape
		res = copy.deepcopy(scipy.misc.imresize(a,(8,8),interp='nearest'))
		#print res

		for i in xrange(8):
			for j in xrange(8):
				if res[i][j]<=128:
					res[i][j] = 0
				else:
					res[i][j] = 1

		#print num, "====================="
		res = copy.deepcopy(np.insert(res.flatten(),0,1))
		#scipy.misc.imshow(res)
		res=copy.deepcopy(res.tolist())
		#print res
		digits[str(num)].append(copy.deepcopy(res))
	return 	digits

#print parse('train')
