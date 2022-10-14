import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils          # mediapipe drawing
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe drawing style
mp_hands = mp.solutions.hands                    # MediaPipe Hands
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)

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

        imgHeight = img.shape[0]
        imgWidth = img.shape[1]     
     
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # draying the node and bone to images
                mp_drawing.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                for i, lm in enumerate(hand_landmarks.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)
                    # Display finger thumbs 
                    #if i == 4:
                    #     cv2.circle(img, (xPos, yPos), 20, (166, 56, 56), cv2.FILLED)
                    print(i, xPos, yPos)
       
        # Displayed FPS 
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f"FPS : {int(fps)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2)          
        cv2.imshow('img', img)    


        # 按下 q 鍵停止
        if cv2.waitKey(5) == ord('q'):
            break    
cap.release()
cv2.destroyAllWindows()