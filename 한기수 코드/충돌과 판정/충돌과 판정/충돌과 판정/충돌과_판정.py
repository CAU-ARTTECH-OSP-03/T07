
#충돌 def
def Collision():   
    global score_value, player_health
    if player_health <= 0: ## 게임오버 관련 변수가 나오면 그걸로 수정해주세요
        return
    for rect in rectNote:
        if rectNote[i].y + 100 < ypos and (ypos + bar_height) < rectNote[i].y and rectNote[i].x  < (xpos + 5) and (xpos + 5) < rectNote[i].x : # 노트가 bar와 만날 때 체력 20과 점수 100을 깎음
            player_health -= 20 
            score_value -= 100 

#verdictBar 생성
verdictBar = pygame.image.load("투명.png")
verdictBar_width = bar_width +20
verdictBar_height = bar_height
verdictBar_char= pygame.transform.scale(verdictBar,(20,100))
rectVerdictBar = verdictBar.get_rect()
verdictBar_xpos = xpos - 20
verdictBar_ypos = ypos

### while문에 들어갈 내용

            if event.type ==pygame.KEYDOWN and event.key ==pygame.K_SPACE: #스페이스바를 누를 때 verdictBar와 노트가 겹치면 
                if rectNote[i].y + 100 < ypos and (ypos + bar_height) < rectNote[i].y and rectNote[i].x < (verdictBar_xpos + 5) and (verdictBar_xpos + 5) < rectNote[i].x + 30:
                    rectNote[i].x = -607
                    rectNote[i].y = random.randint(0, SCREENHEIGHT - 100)
                    player_health += 20 
                    score_value += 10





    if verdictBar_ypos < 0:        #캐릭터가 창을 넘어가려 하면 멈춤
            verdictBar_ypos = 0


    elif verdictBar_ypos > SCREENHEIGHT - bar_height:   #캐릭터가 창을 넘어가려하면 멈춤
            verdictBar_ypos = SCREENHEIGHT - bar_height

    verdictBar_ypos += to_y * dt  # 캐릭터의 포지션을 y만큼 실제 움직임 프레임수(dt)만큼 곱해서 보정




     Collision()