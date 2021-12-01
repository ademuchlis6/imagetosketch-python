import cv2
img = cv2.imread("images.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_inv = cv2.bitwise_not(img_grey)
img_blur = cv2.GaussianBlur(img_inv, (21,21),0)
img_inv_blur = cv2.bitwise_not(img_blur)
img_sketch = cv2.divide(img_grey,img_inv_blur,scale=256.0)
cv2.imwrite("sketch.jpg",img_sketch)