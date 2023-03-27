import cv2

def auxiliar(cv_image,menor,maior):

    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    lower = menor
    upper= maior
    mask = cv2.inRange(hsv, lower, upper)
    
    contornos, arvore = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    maior_contorno = None
    maior_contorno_area = 0
    

    for cnt in contornos:
        area = cv2.contourArea(cnt)
        if area > maior_contorno_area:
            maior_contorno = cnt
            maior_contorno_area = area

    M = cv2.moments(maior_contorno)
   
    if M["m00"] == 0:
        cX = 0
        cY = 0
        centro = (cX, cY)
    else:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centro = (cX, cY)
    
       
    return mask, centro, maior_contorno_area