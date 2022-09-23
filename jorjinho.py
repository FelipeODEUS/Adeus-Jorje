import cv2

fJorje = cv2.imread("poster.jpg")
#cv2.imshow("Adeus Jorjinho", fJorje)
#cv2.waitKey(0)

veiculoJorje = fJorje[120 : 360, 400 : 500]
fJorje[0 : 240, 500 : 600] = veiculoJorje
Jorje = "O fim de uma era :("
cv2.putText(fJorje, Jorje,(20,220),fontFace = cv2.FONT_HERSHEY_DUPLEX, fontScale = 1.0, color = (138, 43, 226))

cv2.imshow("Jorje2.0", fJorje)
cv2.waitKey(0)