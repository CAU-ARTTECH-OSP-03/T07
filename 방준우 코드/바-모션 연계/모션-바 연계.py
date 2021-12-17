import pygame
from pygame.rect import*
import random

#변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
#move = Rect(0,0,0,0) (무슨 변수인지 몰라서 주석처리)
delay = 0

verdict = False  # 판정 시작 종료를 True False로 했습니다. 스페이스바를 누르면 True로 바뀌고 함수 실행후 Flase


#시간def
clock = pygame.time.Clock()

#스크린생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('통합')

# 바 생성
bar = pygame.image.load("bar.png")  # 원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width, bar_height = 20, 100  # 캐릭터 가로,세로  설정   가로:20  세로:100
real_char = pygame.transform.scale(bar, (20, 100))  # 원본캐릭터에서에서 원하는 크기로 커스텀
xpos = 730  # 바의 x좌표위치
ypos = (SCREENHEIGHT / 2) - (bar_height / 2)  # 바의 y좌표위치
to_y = 0  # 바가 y 좌표로 이동하는 정도
bar_speed = 0.5  # 바의 속도


#--------추가-------------------
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
#-------------------------------------
#while문


while play:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    ###---------추가------------------------------------------------
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:


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

                if y < CamHeight * (1 / 3):
                    status = "up"
                    to_y = -bar_speed
                    print(status)
                elif y > CamHeight * (2/3):
                    status = "down"
                    to_y = +bar_speed
                    print(status)
                else:
                    status = "stay"
                    print(status)
        cv2.imshow('Hand Tracking', image)
        #-----------------------------------------------------------------------------


    if ypos < 0:  # 캐릭터가 창을 넘어가려 하면 멈춤
        ypos = 0

    elif ypos > SCREENHEIGHT - bar_height:  # 캐릭터가 창을 넘어가려하면 멈춤
        ypos = SCREENHEIGHT - bar_height

    ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    #화면지우기
    SCREEN.fill((0, 0, 0))
    #makeNote() #moveNote()에서 이미 이 함수를 재귀호출함


    SCREEN.blit(real_char, (xpos, ypos))  # 캐릭터 그리기 # real_char는 바 이미지를 의미

    pygame.display.flip()
    clock.tick(60)
    #------추가----------------------------
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
# --------------------------------------
pygame.quit()

