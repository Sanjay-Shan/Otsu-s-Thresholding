import cv2
from matplotlib import pyplot as plt


img = cv2.imread('3.jpg',0) #reading the image in grayscale
print(img.shape) #h ,w
histr = cv2.calcHist([img],[0],None,[256],[0,256]) #function to get the histogram values
print(sum(histr[-1:]),img.shape[0]*img.shape[1])


plt.plot(histr)
plt.show()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]>140:
            img[i][j]=255
        else:
            img[i][j]=0

cv2.imwrite("threshold_3_140.jpg",img)
