import cv2
import numpy as np
import matplotlib.pyplot as plt

img= cv2.imread('apple.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#as i had told u earlier that in matplotlib we have to use RGB format
img=cv2.resize(img,(700,700))
#lets try homogenious filter
kernal=np.ones((5,5),np.float32)/25
homogenious=cv2.filter2D(img,-1,kernal)
#simple blurring of image
blur=cv2.blur(img,(5,5))#so it was blurring, it was too smooth
#lets try gaussian filter
gaussian=cv2.GaussianBlur(img, (5,5),0)#so that was gaussian filter it was pretty good
#lets try median filter
median=cv2.medianBlur(img,5)#so median filter is better then gaussian filter
#now in the last lets try bilateral filter
bilateral=cv2.bilateralFilter(img, 9, 75,75)
#so these are all filters
#now lets show all the filters using matplotlib
title=['image','Homogenious','blur','Gaussian','Median','Bilateral']#these are all the window names
images=[img,homogenious,blur,gaussian,median,bilateral]#these are the variables that contain filtered images
for i in range(6):#here i had used for loop to iterate all the filters by an iterator i
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')#here 3,3 is the number of rows and column
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()#this method will directly show all the windows in one window
