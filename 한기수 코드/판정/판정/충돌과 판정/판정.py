
#충돌 def
#def Collision():   
#    global score_value, player_health
#    for rect in rectNote:
#        if rect.y == -1:
#            continue
#        if rectNote[i].y + 100 < ypos and (ypos + bar_height) < rectNote[i].y and rectNote[i].x  < (xpos + 5) and (xpos + 5) < rectNote[i].x : # 노트가 bar와 만날 때 체력 20과 점수 100을 깎음
#            player_health -= 20 
#            score_value -= 100 

def judge():   
    global score_value, player_health
    if player_health <= 0:
        return
    for rectN in rectNote:
        if rectN.x == -1:
            continue
        if rectN.top < rectVerdictBar.bottom and rectVerdictBar.top < rectN.bottom and rectN.left < rectVerdictBar.right and rectVerdictBar.left < rectN.right: # 노트가 판정bar와 만날 때 체력 20과 점수 100을 올림
            rectN.x = -607 
            rectN.y = random.randint(0, SCREENHEIGHT - 100)
            player_health += 20 
            score_value += 100 
            break
        else:
            continue

#verdictBar 생성
verdictBar = pygame.image.load("판정구역.png")
verdictBar_width = bar_width +30
verdictBar_height = bar_height
verdictBar_char= pygame.transform.scale(verdictBar,(30,160))
rectVerdictBar = verdictBar.get_rect()
verdictBar_xpos = xpos - 30
verdictBar_ypos = ypos

### while문에 들어갈 내용


            if event.key ==pygame.K_SPACE: #스페이스바를 누르면 judge함수 실행
                  judge()





    if verdictBar_ypos < 0:        #캐릭터가 창을 넘어가려 하면 멈춤
            verdictBar_ypos = 0


    elif verdictBar_ypos > SCREENHEIGHT - bar_height:   #캐릭터가 창을 넘어가려하면 멈춤
            verdictBar_ypos = SCREENHEIGHT - bar_height

    verdictBar_ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정




