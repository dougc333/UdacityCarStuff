import csv
import cv2
import numpy as np

lines = []
with open('/Users/dc/Desktop/data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

images = []
measurements = []
for line in lines:
    source_path = line[0]
    filename = source_path.split('/')[-1]
    #print('fn:',filename)
    current_path = '/Users/dc/Desktop/data/IMG/' + filename
    print ('cp:',current_path)
    image = cv2.imread(current_path)
    print (image.shape)
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)

print (len(images))
X_train = np.array(images)
#X_train = X_train.astype('float32')
y_train = np.array(measurements)
#y_train = y_train.astype('float32')

input_shape = X_train.shape
print(input_shape, 'input shape')


from keras.models import Sequential
from keras.layers import Flatten, Dense

model = Sequential()
model.add(Flatten(input_shape))
model.add(Dense(1))

model.compile(loss='mse', optimizer = 'adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True)

model.save('model.h5')