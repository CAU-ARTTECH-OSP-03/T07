##실행하면 카메라가 켜짐,손바닥 피고 있는것이 준비 자세
# 손바닥을 위로 올리면 up출력(위 1/8지점까지),아래로 내리면 down출력(아래1/8지점까지)
#그 중간에 있으면 stay출력

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip
        image = cv2.flip(image, 1)

        # Set flag
        image.flags.writeable = False

        # Detections
        results = hands.process(image)

        # Set flag to true
        image.flags.writeable = True

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # cam size
        CamHeight, CamWidth, _ = image.shape

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, )

            # -----------------------------------------------------중지의 점9의 y 좌표를 위해
            for hand_landmarks in results.multi_hand_landmarks:

                for ids, landmark in enumerate(hand_landmarks.landmark):
                    if ids == 9:
                        y = landmark.y * CamHeight

                if y < CamHeight * (1 / 8):
                    status="up"
                    print(status)
                elif y > CamHeight * (7 / 8):
                    status = "down"
                    print(status)
                else:
                    status = "stay"
                    print(status)
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()





