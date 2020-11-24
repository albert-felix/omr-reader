import sys
import cv2
import json


def answer_box_1(ROI):

    ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for ri in range(len(roi_contours[0])):
        roi_area = cv2.contourArea(roi_contours[0][ri])
        if (roi_area > 100) and (roi_area < 200):
            (x,y),radius = cv2.minEnclosingCircle(roi_contours[0][ri])
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(new_image, center, radius, (0,0,255), 2)

    # first row

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
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'A'
            elif (45 <= option <= 55):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'B'
            elif (65 <= option <= 75):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'C'
            elif (85 <= option <= 95):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'D'


def answer_box_2(ROI):

    ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for ri in range(len(roi_contours[0])):
        roi_area = cv2.contourArea(roi_contours[0][ri])
        if (roi_area > 100) and (roi_area < 200):
            (x,y),radius = cv2.minEnclosingCircle(roi_contours[0][ri])
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(new_image, center, radius, (0,0,255), 2)

    # first row

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
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'A'
            elif (45 <= option <= 55):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'B'
            elif (65 <= option <= 75):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'C'
            elif (85 <= option <= 95):
                if ques_no in answers:
                    answers.pop(ques_no)
                else:
                    answers[ques_no] = 'D'


def enrollment_num(ROI):

    ret, thresh = cv2.threshold(ROI, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    roi_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for ri in range(len(roi_contours[0])):
        roi_area = cv2.contourArea(roi_contours[0][ri])
        if (roi_area > 100) and (roi_area < 200):
            (x,y),radius = cv2.minEnclosingCircle(roi_contours[0][ri])
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(new_image, center, radius, (0,0,255), 2)

            a,b = center
            position = 1
            value = 0

            # finding position of enrollment number

            if (25 <= a <= 35):
                position = 1
            elif (45 <= a <= 55):
                position = 2
            elif (65 <= a <= 75):
                position = 3
            elif (85 <= a <= 95):
                position = 4
            elif (105 <= a <= 115):
                position = 5
            elif (125 <= a <= 135):
                position = 6
            elif (145 <= a <= 155):
                position = 7
            elif (165 <= a <= 175):
                position = 8
            elif (185 <= a <= 195):
                position = 9
            elif (205 <= a <= 215):
                position = 10

            # finding value of enrollment number

            if (70 <= b <= 80):
                value = 1
            elif (90 <= b <= 100):
                value = 2
            elif (110 <= b <= 120):
                value = 3
            elif (130 <= b <= 140):
                value = 4
            elif (150 <= b <= 160):
                value = 5
            elif (170 <= b <= 180):
                value = 6
            elif (190 <= b <= 200):
                value = 7
            elif (210 <= b <= 220):
                value = 8
            elif (230 <= b <= 240):
                value = 9
            elif (250 <= b <= 260):
                value = 0

            # adding enrollment values to dictionary
            enroll_dict[position] = value

image_location = sys.argv[1]
answer_key_json = sys.argv[2]
correct_mark = int(sys.argv[3])
enroll_dict = {}
answers = {}
answer_key = {}


image = cv2.imread(image_location)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 80, 90)
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

ques_box_1 = False
ques_box_2 = False
enrollment_box = False

# selecting Answer Box from OMR Sheet

for i in range(len(contours[0])):
    if contours[1][0][i][1] == -1:
        area = cv2.contourArea(contours[0][i])
        if area > 50000:
            x,y,w,h = cv2.boundingRect(contours[0][i])

    # selecting Answer Box 1

            if (265 <= w <= 280):
                if not ques_box_1:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_1 = True
                    answer_box_2(ROI)

    # selecting Answer Box 2

            if (675 <= w <= 690):
                if not ques_box_2:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    ques_box_2 = True
                    answer_box_1(ROI)

    # selecting enrollment code box

            if (365 <= w <= 380):
                if not enrollment_box:
                    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 1 )
                    ROI = gray[y:y+h, x:x+w]
                    new_image = image[y:y+h, x:x+w]
                    enrollment_box = True
                    enrollment_num(ROI)


enroll_dict = dict(sorted(enroll_dict.items()))
if len(enroll_dict) == 10:
    enrollment_code = ''
    for enroll in enroll_dict:
        enrollment_code += str(enroll_dict[enroll])
else:
    enrollment_code = 'Enrollment number not properly coded'

answers = dict(sorted(answers.items()))

answer_key_json = json.loads(answer_key_json)
for json in answer_key_json:
    answer_key.update(json)

marks = 0
for answer in answers:
    if(str(answer) in answer_key):
        if (answers[answer] == answer_key[str(answer)]):
            marks += correct_mark

result = {}
result['e_code'] = enrollment_code
result['marks'] = marks
print(result)
