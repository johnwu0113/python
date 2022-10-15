import cv2
import mediapipe as mp
import numpy as np 
import time
import os,glob

mp_drawing = mp.solutions.drawing_utils          # mediapipe drawing
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe drawing style
mp_hands = mp.solutions.hands                    # MediaPipe Hands
pTime = 0
cTime = 0
# cap = cv2.VideoCapture(0)
#inputPath = './upload'
#outputPath = '.'

#for filename in glob.glob(os.path.join('./upload', '*.mp4')):
#    with open(filename, 'r') as f:
        #text = f.read()
#        cap = cv2.VideoCapture(filename)
        #print (len(text))
#cap = cv2.VideoCapture(filename)
cap = cv2.VideoCapture("./upload/f_001.mp4")


# create a 500*500 3 
#img = np.zeros((500,500,3),np.uint8)
#img.fill(255)

j = 0
# MediaPipe Hands
with mp_hands.Hands(
    model_complexity=0,
    # max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # Change BGR to RGB
        results = hands.process(img2)                 # Detate palm
        # print multi_hand_landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # draying the node and bone to images
                for i, lm in enumerate(hand_landmarks.landmark):                  
                   #print(i,"x = {}, y = {}, z = {}".format(lm.x,lm.y,lm.z))                      
                   xPos = int(lm.x * img.shape[0])
                   yPos = int(lm.y * img.shape[1])
                   #zPos = int(lm.z * img.shape[2])
                   print(i,"x = {}, y = {} ".format(xPos,yPos))                      
                    #cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)
                # mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)    
       
        # Displayed FPS 
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        # Video Size
        size = img.shape
        h, w = size[0], size[1]
        # Frams #        
        frames = cap.get(7)         
        
        cv2.putText(img, f"FPS: {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)          
        cv2.putText(img, f"FRAMES#: {int(frames)},{int(j)}", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)  
        cv2.putText(img, f"SIZES: {int(w)}x{int(h)}", (20, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)  

                # 顯示影片
        cv2.imshow('img', img)           
        
        j = j + 1 
        # 按下 q 鍵停止
        if cv2.waitKey(5) == ord('q'):
            break    
cap.release()
cv2.destroyAllWindows()

    