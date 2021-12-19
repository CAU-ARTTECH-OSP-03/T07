import pygame
from pygame.rect import*
import random
import cv2
import mediapipe as mp


#변수
play = True
SCREENHEIGHT = 400
SCREENWIDTH = 800
move = Rect(0,0,0,0) 
delay = 0
score_x=100 #점수판 위치
score_y=100


#시간def
clock = pygame.time.Clock()


#스크린생성
pygame.init()

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('통합')

#점수판 세팅
score_value=0  #점수판 점수
font=pygame.font.Font("freesansbold.ttf",30) #점수판 글씨 폰트
#점수판 생성함수
def showscore(x, y):
    score = font.render("score:"+str(score_value), True, "red")
    SCREEN.blit(score,(x,y))

# 바 생성
bar = pygame.image.load("bar.png")  # 원본캐릭터 사진 업로드  원하는 경로의 사진을 복사 붙여넣기
bar_width, bar_height = 20, 100  # 캐릭터 가로,세로  설정   가로:20  세로:100
real_char = pygame.transform.scale(bar, (20, 100))  # 원본캐릭터에서에서 원하는 크기로 커스텀
xpos = 730 # 바의 x좌표위치
ypos = (SCREENHEIGHT / 2) - (bar_height / 2)  # 바의 y좌표위치
to_y = 0  # 바가 y 좌표로 이동하는 정도
bar_speed = 0.5  # 바의 속도

#판정선 생성
line = pygame.image.load("line.png")
line_x_pos = 740
line_y_pos = 0

#노트생성
note = [pygame.image.load('노트 프로토.png') for i in range(33)] # 노트 수 # 리스트이다. (노트가 33개 들어가있는)
rectNote = [None for i in range(len(note))] # None을 note(리스트)의 길이 수 만큼 넣은 리스트

#노트생성을 pygame 기본 rect에 저장
for i in range(len(note)): 
    note[i] = pygame.transform.scale(note[i], (30, 100)) #노트 크기변화
    rectNote[i] = note[i].get_rect() #노트의 x,y좌표 정보
    rectNote[i].x = -1



#노트생성 딜레이 def
def delayUpdate():
    global delay  
    delay += 1
    if delay > 200: # 노트생성 딜레이 ex) 100 = 1000ms = 1s # 이 숫자를 줄이면 노트가 더 많이 쏟아짐
        delay = 0
        return True
    return False

#노트생성def
def makeNote():
    if delayUpdate():
        index = random.randint(0, len(note)-1) # 0에서 len(note)-1 까지 범위 중 랜덤으로 int 값을 index에 대입
        if rectNote[index].x == -1:
            rectNote[index].y = random.randint(0, SCREENHEIGHT - 100) 
            rectNote[index].x = 0 #x가 0일때 시작하기


#노트이동def
def moveNote():
    global player_health, score_value
    makeNote()

    for i in range(len(note)):
        if rectNote[i].x > 800: #판정선 너머로 지나가면
            rectNote[i].x = -607
            rectNote[i].y = random.randint(0, SCREENHEIGHT - 100)  #오른쪽 끝으로 넘어가면 노트가 다시 랜덤 y 좌표  부터 시작
            score_value -= 50      # 노트가 800에 도달하면 점수 50, 체력 10을 깎음
            player_health -= 10           
        if rectNote[i].x == -1:
            continue

        rectNote[i].x += 10 #노트속도

        SCREEN.blit(note[i], rectNote[i])
   
#verdictBar 생성
verdictBar = pygame.image.load("투명.png")
verdictBar= pygame.transform.scale(verdictBar,(10,100))
rectVerdictBar = verdictBar.get_rect()
rectVerdictBar.centerx = (720)
rectVerdictBar.centery = (SCREENHEIGHT/2)


#판정 def
def judge():   
    global score_value, player_health
    for rectN in rectNote:
        if rectN.x == -1:
            continue
        if rectN.top < rectVerdictBar.bottom and rectVerdictBar.top < rectN.bottom and rectN.left < rectVerdictBar.right and rectVerdictBar.left < rectN.right: # 노트가 판정bar와 만날 때 체력 20과 점수 100을 올림
            rectN.x = -607 
            rectN.y = random.randint(0, SCREENHEIGHT - 100)
            player_health += 20 
            score_value += 100 
            break

#--------모션-------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
#-------------------------------------




#while문

while play:
    player_health = 300
    to_y = 0
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스가 눌렸는지
            if event.button == 4:  # 마우스휠 올리기
                to_y = -bar_speed  # 캐릭터를 위로 캐릭터의 속도만큼 올리기
            if event.button == 5:  # 마우스휠내리기
                to_y = +bar_speed  # 캐릭터를 아래로 캐릭터의 속도만큼 내리기 
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE: #스페이스바를 누르면 judge함수 실행
                  judge()
 
    ###---------모션------------------------------------------------
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
                elif y > CamHeight * (1.5/3):
                    status = "down"
                    to_y = +bar_speed
                    print(status)
                else:
                    status = "stay"
                    print(status)
        cv2.imshow('Hand Tracking', image)
        #-----------------------------------------------------------------------------
                


    if rectVerdictBar.y < 0:        #캐릭터가 창을 넘어가려 하면 멈춤
            rectVerdictBar.y = 0

    elif rectVerdictBar.y > SCREENHEIGHT-rectVerdictBar.height:   #캐릭터가 창을 넘어가려하면 멈춤
            rectVerdictBar.y = SCREENHEIGHT-rectVerdictBar.height

    if ypos < 0: # 캐릭터가 창을 넘어가려 하면 멈춤
        ypos = 0

    elif ypos > SCREENHEIGHT - bar_height: # 캐릭터가 창을 넘어가려하면 멈춤
        ypos = SCREENHEIGHT - bar_height


    ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    rectVerdictBar.y += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정
    #화면지우기
    SCREEN.fill((0, 0, 0))
    showscore(score_x, score_y)
    makeNote()  # 노트 생성
    moveNote() # 노트 이동

    SCREEN.blit(line, (line_x_pos, line_y_pos))
    SCREEN.blit(real_char, (xpos, ypos))  # 캐릭터 그리기 # real_char는 바 이미지를 의미
    SCREEN.blit(verdictBar, rectVerdictBar)

    pygame.display.flip()

    #------모션----------------------------
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    

    
cap.release()
cv2.destroyAllWindows()
# --------------------------------------    
pygame.quit()


# 추후에 추가해야 할 것 : 체력바, 이펙트
# 가능하다면 구현하기 (시간관계상...) : 게임시작, 오버 화면
# openCV를 쓰면 렉이 걸리는거는 어쩔 수 없는 것 같습니다..
