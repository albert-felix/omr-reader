import numpy as np
import cv2



answer_key = {1: 'B', 2: 'b', 3: 'C', 4: 'B', 5: 'D', 6: 'a', 7: 'C', 8: 'B', 9: 'C', 10: 'B', 11: 'B', 12: 'D', 13: 'B', 14: 'C', 15: 'C'}

answers = {}

def answer_box_1(ROI):

    ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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

# -------------------------------

def answer_box_2(ROI):

    ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
            # print(center)

            a,b = center
            option = 0
            if (70 <= b <= 80):
                if (a < 110):
                    ques_no = 1
                    option = a - 10
                elif (170 <= a <= 250):
                    ques_no = 6
                    option = a - 145
    # second row

            if (110 <= b <= 120):
                if (a < 110):
                    ques_no = 2
                    option = a - 10
                elif (170 <= a <= 250):
                    ques_no = 7
                    option = a - 145
    # third row

            if (150 <= b <= 160):
                if (a < 110):
                    ques_no = 3
                    option = a - 10
                elif (170 <= a <= 250):
                    ques_no = 8
                    option = a - 145
    # fourth row

            if (190 <= b <= 200):
                if (a < 110):
                    ques_no = 4
                    option = a - 10
                elif (170 <= a <= 250):
                    ques_no = 9
                    option = a - 145
    # fifth row

            if (230 <= b <= 240):
                if (a < 110):
                    ques_no = 5
                    option = a - 10
                elif (170 <= a <= 250):
                    ques_no = 10
                    option = a - 145



    # selecting shaded options
            # print(option)
            if (25 <= option <= 35):
                answers[ques_no] = 'A'
            elif (45 <= option <= 55):
                answers[ques_no] = 'B'
            elif (65 <= option <= 75):
                answers[ques_no] = 'C'
            elif (85 <= option <= 95):
                answers[ques_no] = 'D'

#------------------------------

image_location = 'C:/Users/ALK/Desktop/Test 1.jpeg'

image = cv2.imread(image_location)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 80, 90)
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

ques_box_1 = False
ques_box_2 = False

# selecting Answer Box from OMR Sheet

for i in range(len(contours[0])):
    if contours[1][0][i][1] == -1:
        area = cv2.contourArea(contours[0][i])
        if area > 50000:
            x,y,w,h = cv2.boundingRect(contours[0][i])

    # selecting Answer Box 1

            if (270 <= w <= 280):
                if not ques_box_1:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_1 = True
                    answer_box_2(ROI)

    # selecting Answer Box 2

            if (680 <= w <= 690):
                if not ques_box_2:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_2 = True
                    answer_box_1(ROI)


answers = dict(sorted(answers.items()))
marks = 0
print(answers)
for answer in answers:
    if (answers[answer] == answer_key[answer].upper()):
        marks += 1
print(marks)
# cv2.imshow('omr',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
