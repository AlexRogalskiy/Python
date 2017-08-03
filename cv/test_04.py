import cv2 as cv
cap = cv.VideoCapture('111.divx') #Замените 111.mp4 на какой-нибудь ролик с лицами
# Загрузка обученного каскадного классификатора
cascade = cv.CascadeClassifier("lbpcascade_frontalface.xml")
 
while True:
    ok, img = cap.read() 
    if not ok: 
        break 
    gray = img
    sf = min(640./img.shape[1], 480./img.shape[0])
    gray = cv.resize(gray, (0,0), None, sf, sf) 
    # Масштабирование 
    rects = cascade.detectMultiScale(gray, scaleFactor=1.3, 
        minNeighbors=4, minSize=(40, 40), 
        flags= cv.CASCADE_SCALE_IMAGE)
    
    out = gray
    for x, y, w, h in rects: 
        cv.rectangle(out, (x, y), (x+w, y+h), (0,255,0), 2)
    # Вокруг найденного лица
    # рисуем красный прямоугольник 
    cv.imshow("edges+face", out)
    if cv.waitKey(20) > 0:
        break