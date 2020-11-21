import numpy as np
import cv2

image_location = 'C:/Users/ALK/Desktop/Test 1.jpeg'

image = cv2.imread(image_location)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 80, 90)

contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

ques_box_1 = False
ques_box_2 = False

for i in range(len(contours[0])):
    if contours[1][0][i][1] == -1:
        area = cv2.contourArea(contours[0][i])
        if area > 50000:
            # print(contours[1][0][i])
            # cv2.drawContours(image, [contours[0][i]], 0, (0,255,0), 1)
            x,y,w,h = cv2.boundingRect(contours[0][i])
            # cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
            print(x,y)

# selecting Question Box

            if (115 <= y <= 130):
                if not ques_box_1:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_1 = True
                    print(x,y)
            elif (380 <= y <= 395):
                if not ques_box_2:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_2 = True
                    print(x,y)


############


# roi_gray = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
# roi_blurred = cv2.GaussianBlur(roi_gray, (5, 5), 0)
# roi_edged = cv2.Canny(ROI, 60, 90)
ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# print(x,y,w,h)

answers = {}

for ri in range(len(roi_contours[0])):
    roi_area = cv2.contourArea(roi_contours[0][ri])
    if (roi_area > 100) and (roi_area < 200):
        # print(roi_area)
        # x,y,w,h = cv2.boundingRect(roi_contours[0][ri])
        # cv2.rectangle(new_image, (x,y), (x+w, y+h), (0,0,255), 2)
        (x,y),radius = cv2.minEnclosingCircle(roi_contours[0][ri])
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(new_image, center, radius, (0,0,255), 2)

        a,b = center
        if (40 <= b <= 45):
            if (a < 100):
                ques_no = 11
                option = a
            elif (160 <= a <= 240):
                ques_no = 13
                option = a - 140
            elif (300 <= a <= 380):
                ques_no = 15
                option = a - 280
            elif (440 <= a <= 520):
                ques_no = 17
                option = a - 420
            elif (580 <= a <= 660):
                ques_no = 19
                option = a - 560

# selecting shaded options
            if (25 <= option <= 35):
                answers[ques_no] = 'A'
            elif (45 <= option <= 55):
                answers[ques_no] = 'B'
            elif (65 <= option <= 75):
                answers[ques_no] = 'C'
            elif (85 <= option <= 95):
                answers[ques_no] = 'D'

# second row

        elif (80 <= b <= 85):
            if (a < 100):
                ques_no = 12
                option = a
            elif (160 <= a <= 240):
                ques_no = 14
                option = a - 140
            elif (300 <= a <= 380):
                ques_no = 16
                option = a - 280
            elif (440 <= a <= 520):
                ques_no = 18
                option = a - 420
            elif (580 <= a <= 660):
                ques_no = 20
                option = a - 560

# selecting shaded options
            if (25 <= option <= 35):
                answers[ques_no] = 'A'
            elif (45 <= option <= 55):
                answers[ques_no] = 'B'
            elif (65 <= option <= 75):
                answers[ques_no] = 'C'
            elif (85 <= option <= 95):
                answers[ques_no] = 'D'



# print(sorted(answers.items()))
# cv2.imshow('abc',new_image)
cv2.imshow('omr',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
