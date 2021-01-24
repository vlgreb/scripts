import cv2
image = cv2.imread('test3.jpg')
scale_percent = 15 # Процент от первоначального размера
width = int(image.shape[1] * scale_percent / 100)
heigth = int(image.shape[0] * scale_percent / 100)
dim = (width, heigth)
# Resize the image
resize = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# Load the cascade
face_cascade = cv2.CascadeClassifier('D:\haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(resize, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Resized image', resize)
cv2.waitKey()