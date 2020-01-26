import tensorflow as tf
import numpy as np
import os
import sys

arglist = str(sys.argv)
#os.remove('Software1.txt')
#os.remove('Software2.txt')
arglist = arglist.split("\'")
print(arglist)
f = open(arglist[-2],'r')
o1 = open('Software1.txt','a')		
o2 = open('Software2.txt','a')
	
dataTest = []
dataTestNum = []
while True:
	val = f.readline()
	if val == '':
		break
	v = int(val)
	dataTestNum.append(v)
	res = [int(i) for i in list('{0:0b}'.format(v))]
	filling = 10-len(res)
	for i in range(0,filling):
		res.insert(0,0)
	dataTest.append(np.array(res))

	if v%15 == 0:
		pt = "fizzbuzz\n"
		o1.write(pt)
	elif v%3 == 0:
		pt = "fizz\n"
		o1.write(pt)
	elif v%5 == 0:
		pt = "buzz\n"
		o1.write(pt)
	else:
		pt = val
		o1.write(pt)

dataTest = np.array(dataTest)
model = tf.keras.models.load_model('fizzbuzz.h5')

labelsOut = model.predict(dataTest)
for i in range(0,labelsOut.shape[0]):
	a = labelsOut[i,:]
	oitr = np.argmax(a)
	if oitr == 0:
		pt = "fizzbuzz\n"
		o2.write(pt)
	elif oitr == 1:
		pt = "buzz\n"
		o2.write(pt)
	elif oitr == 2:
		pt = "fizz\n"
		o2.write(pt)
	else:
		pt = str(dataTestNum[i])+"\n"
		o2.write(pt)

