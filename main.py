import cv2
plateCascade = cv2.CascadeClassifier("Resources/NP.xml")
minArea = 500
cap = cv2.VideoCapture("Resources/CP3.mp4")
cap.set(3, 640)
cap.set(4,480)
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Numbers detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            imgR = img[y:y + h, x:x + w]
            cv2.imshow('ImgR', imgR)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        # To save the results
        # cv2.imwrite("Resources/Scanned/NumberPlate_"+str(count)+".jpg",imgR)
        # count +=1
        break