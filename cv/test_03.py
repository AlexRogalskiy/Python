import cv2 as cv

cap = cv.VideoCapture('games.jpg')
while True: 
    ok, img = cap.read() # Загружаем очередной кадр 
    if not ok: 
        break 
    # Конвертируем цветное изображение в монохромное 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
      
    # Добравляем размытие 
    #gray = cv.GaussianBlur(gray, (7, 7), 1.5)  
    edges = cv.Canny(gray, 1, 100) # Детектируем ребра 
    cv.imshow("edges", edges) # Отображаем результат 
    cv.imshow("lisiy", img) # Отображаем результат 
    cv.waitKey()