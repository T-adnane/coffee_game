import cv2
import mediapipe as mp
import random

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

x = random.randint(0,900)
y = random.randint(0, 600)

initHand = mp.solutions.hands
mainHand = initHand.Hands()

def handLandmarks(colorImg):
    landmarkList = []
    landmarkPositions = mainHand.process(colorImg)
    landmarkChek = landmarkPositions.multi_hand_landmarks
    if landmarkChek:
        for hand in landmarkChek:
            for index, landmark in enumerate(hand.landmark):  # Change here
                landmarkList.append([index, int(landmark.x*1280), int(landmark.y*720)])
    return landmarkList
yes_clicked = False
text_cofee = "You need a coffee ?"
color = (153, 153, 255)

while True:
    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    lmlist = handLandmarks(img)

    if lmlist:
        if x+5<lmlist[8][1]<x+170 and y+40<lmlist[8][2]<y+75 and yes_clicked == False:
            text_cofee = "then drink one"
            yes_clicked = True
        elif x+180<lmlist[8][1]<x+340 and y+40<lmlist[8][2]<y+75 and yes_clicked == False:
            x = random.randint(0, 930)
            y = random.randint(0, 670)

    if text_cofee == "You need a coffee ?":
        cv2.rectangle(img, (x, y), (x+350, y+50), color, cv2.FILLED)
        cv2.putText(img, text_cofee, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

        cv2.rectangle(img, (x, y+50), (x + 175, y + 80), color, cv2.FILLED)
        cv2.putText(img, "Yes", (x + 40, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

        cv2.rectangle(img, (x+175, y+50), (x + 350, y + 80), color, cv2.FILLED)
        cv2.putText(img, "No", (x + 215, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    else:
        cv2.rectangle(img, (x, y), (x + 270, y + 50), color, cv2.FILLED)
        cv2.putText(img, text_cofee, (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()