import cv2
import mediapipe as mp
import numpy as np 

cap = cv2.VideoCapture("./upload/f_001.mp4")

mpHands = mp.solutions.hands  
hands = mpHands.Hands(static_image_mode=False,max_num_hands=2,min_detection_confidence=0.75,min_tracking_confidence=0.5) 

mpDraw = mp.solutions.drawing_utils

# create a 500*500 3 

img = np.zeros((500,500,3),np.uint8)

img.fill(255)
i = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # Change BGR to RGB
    results = hands.process(frame)                 # Detate palm

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # draying the node and bone to images
            print("\n")
            m = hand_landmarks.landmark
            for i, lm in enumerate(hand_landmarks.landmark):
                print("x = {}, y = {}, z = {}".format(lm.x,lm.y,lm.z))    
            
            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
            
    cv2.imwrite('.' + str(i) + '.png', img)
    
    cv2.imshow('img', img)
    
    img = np.zeros((500,500,3),np.uint8)
    img.fill(255)    
    
    i = i + i
    if cv2.waitKey(1) & 0xFF == 27:           
        break    
    print ("totals {} frams,{}".format(cap.get(7),i))
    
cap.release()