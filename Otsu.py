import cv2

img=cv2.imread("3.jpg",0)
pixels=img.shape[0]*img.shape[1]
hist = cv2.calcHist([img],[0],None,[256],[0,256]) #function to get the histogram values

P1,P2,Mu1,Mu2,Var_max,Pred_thresh,variance=0,0,0,0,0,0,0

#calculate the P1 P2 and Mu1 Mu2 for the forground the background pixels on the go
#we will be calculating the interclass variance between the 2 classes  C1 and C2
#iterating through the values of T
for T in range(0,256,1):
    try:
        P1= sum(hist[0:T])/pixels #probablity of pixels on foreground
        P2= sum(hist[T:256])/pixels #probablity of pixels on background
        Mu1=sum([i*hist[i] for i in range(0,T)])/sum(hist[0:T]) #averge intensity on the foreground side
        Mu2=sum([i*hist[i] for i in range(T,256)])/sum(hist[T:256]) #average intensity on the background side
    except Exception as e:
        print(e)
        continue
    variance=P1*P2*((Mu1-Mu2)**2)
    if variance>Var_max:
        Var_max=variance
        Pred_thresh=T

print("The predicted Otsu's threshold is :",Pred_thresh)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j]>Pred_thresh:
            img[i][j]=255
        else:
            img[i][j]=0

cv2.imwrite("threshold_3_Otsu.jpg",img)





