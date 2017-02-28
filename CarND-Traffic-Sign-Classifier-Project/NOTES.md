
fig and plotting notes:

The easiest to remember for multiple rows and columns is:

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



