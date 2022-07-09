import  cv2



#read image
img = cv2.imread("C:/Users/Daniel Samuel/Desktop/image.PNG")#load the image
img_resize  = cv2.resize(img,(300,400))
#CONVERT IMAGE TO GRAYSCALE
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blur image
blur_img = cv2.GaussianBlur(img,(7,7),6)
cv2.imshow("blur image",blur_img)
cv2.imshow("input image",img)
cv2.waitKey(0)
