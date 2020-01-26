import os

#os.remove('Software1.txt')
#os.remove('Software2.txt')

f = open('test_input.txt','r')
o1 = open('Software1.txt','a')		
o2 = open('Software2.txt','a')	


while True:
	val = f.readline()
	if val == '':
		break
	v = int(val)
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

import numpy as np

def genData(start,ending):
	data = []
	labels = []
	for num in range(start,ending+1):
		if num%15 == 0:
			labels.append(np.array([1,0,0,0]))
		elif num%5 == 0:
			labels.append(np.array([0,1,0,0]))
		elif num%3 == 0:
			labels.append(np.array([0,0,1,0]))
		else:
			labels.append(np.array([0,0,0,1]))
		res = [int(i) for i in list('{0:0b}'.format(num))]
		filling = 10-len(res)
		for i in range(0,filling):
			res.insert(0,0)
		data.append(np.array(res))
	return np.array(data), np.array(labels)

data, labels = genData(101,1000)
dataTest, labelsTest = genData(1,100)
print(data,labels)
print(dataTest)
import tensorflow as tf

model = tf.keras.models.Sequential([
		tf.keras.layers.Dense(1000, input_shape=(10,),activation="relu"),
		tf.keras.layers.Dense(4,activation="softmax")
		])
adamOpt=tf.keras.optimizers.Adam(learning_rate=1e-4)
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])
history = model.fit(data,labels,epochs=100,batch_size=16)

model.evaluate(dataTest,labelsTest)

model.save('fizzbuzz.h5')

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
		pt = str(i+1)+"\n" #had to replace this
		o2.write(pt)


