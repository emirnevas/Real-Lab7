# t1
import cv2

# t2
image = cv2.imread('deneme3.png', 1)
image = cv2.resize(image, (int(image.shape[1]/4), int(image.shape[0]/4)))

# t3-4
(R, G, B) = cv2.split(image)

# t5
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# t6
red = cv2.normalize(R, None, 0, 255, cv2.NORM_MINMAX)
green = cv2.normalize(G, None, 0, 0, cv2.NORM_MINMAX)
blue = cv2.normalize(B, None, 0, 255, cv2.NORM_MINMAX)

# t7
modified_image = cv2.merge([blue, green, red])

cv2.imshow("Modified", modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()