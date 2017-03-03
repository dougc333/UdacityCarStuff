
l2 regularization:
https://github.com/tensorflow/tensorflow/blob/7e3b8b23835ab0ac55d390aed2349af6e05dbe3b/tensorflow/models/image/mnist/convolutional.py#L216

Dropout:
The paper: https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf
says dropout applied to all layers is better than at the FC layer, from 3.02$ to 2.55%
p = (0.9, 0.75, 0.75, 0.5, 0.5, 0.5)
Test this on our dataset. pyth 

fig and plotting notes:

The easiest to remember for multiple rows and columns is:
GridSpec(#rows,#cols)
subplot(rows,cols, )
gs1 = gridspec.GridSpec(2, 2)
#this spacing doesnt make a difference
gs1.update(wspace=2.0, hspace= 2.0)
plt.subplot(2,2,1)
plt.imshow(X_train[0])
plt.title(csv_dict[y_train[0]])
#test 
plt.subplot(2,2,2)
plt.imshow(X_test[0])
plt.title(csv_dict[y_test[0]])

plt.subplot(2,2,3)
plt.imshow(X_train_pp[0],cmap='gray')
plt.title(csv_dict[y_test[0]])

plt.subplot(2,2,4)
plt.imshow(X_test_pp[0],cmap='gray')
plt.title(csv_dict[y_test[0]])


The bad habit is to use: 
fig = plt.figure()
plt.subplot(1,total num images, current image number to plot)
plt.imshow(img)

the problem with the above is setting the columns and rows correctly. not worth the debug time
start with gridspec first and use it to set rows columns
note: the horiz/vertical spacing never worked 


Prove RGB vs BGR in train.p test,p

#for documentation prove the images in train.p are RGB and not BGR
#imgtest=cv2.imread('/Users/dc/Downloads/german_traffic_sign_data/GTSRB/Final_Training/Images/00000/00000_00000.ppm')
#print(imgtest.shape)
#print (imgtest[:,:,0])
#plt.imshow(imgtest[:,:,0]) #first channel B


#print (imgtest[:,:,1])
#Eplt.imshow(imgtest[:,:,1]) #first channel G

to plot more use print options
#np.set_printoptions(threshold=5000)
#print (X_train[0,:,:,0])
#plt.imshow(X_train[0,:,:,0])

#plt.imshow(X_train[0][:,:,1])
#print (X_train[0,:,:,1])
#print (X_train[0,:,:,1].shape)

#print(X_train[0,:,:,2])
#plt.imshow(X_train[0,:,:,2]) #looks like Blue, matches




