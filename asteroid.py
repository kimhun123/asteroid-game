import pygame
import random
import time

gunrect =[0,0]
pygame.init() #게임 자원 초기화
screen = pygame.display.set_mode((480,640))#s화면 크기

FPS = 30 #초당 프래임
fpsClock = pygame.time.Clock()

asteroidtimer = 100 #운석 출현 빈도 제어
guntimer = 100
bossguntimer = 100
count = 0
count_1 = 0


score = 0
x_plus = 50
x =  0
a = 0
y = 0
k = 0


asteroids = [[20, 0, 0]] #[[x,y,state]] state는 3개 이미지 종류
guns = [[100,0]]
bossguns = [[50,0]]




try:
    spaceshipimg = pygame.image.load("./img/spaceship2.png")
    gunimg = pygame.image.load("./img/gun2.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)
    gameover = pygame.image.load("./img/gameover.jpg")
    bombimg = pygame.image.load("./img/bomb3.png")
    #heartimg = pygame.image.load("./img/heart123.png")
    bossimg = pygame.image.load("./img/boss2.png")
    #itemimg = pygame.image.load("./img/potion.png")
    bossgunimg =pygame.image.load("./img/gun1.png")
    supporterimg = pygame.image.load("./img/supporter.png")

    #level_2 = pygame.image.load("./img/level_2.png")
    #level_3 = pygame.image.load("./img/level_3.png")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    bombsound = pygame.mixer.Sound("./audio/bomb.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")
    basesound = pygame.mixer.Sound("./audio/base_audio.wav")

except Exception as err:
    print('그림 또는 효과음 삽입에 문제가 있습니다.: ',err)
    pygame.quit()
    exit(0)


def text(arg,x,y):
    font = pygame.font.Font(None, 24)
    text = font.render("Score: " + str(arg).zfill(6), True,(0,0,0))
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)


def level_up():
    if score == 200:
        screen.fill((255,255,255))#흰색으로 화면 지우기
        screen.blit(level_2, (0,0))
        pygame.display.flip()
        time.sleep(3)

    elif score == 400:
        screen.fill((255,255,255))#흰색으로 화면 지우기
        screen.blit(level_3, (0,0))
        pygame.display.flip()
        time.sleep(3)

def speed_up():
    global asteroidtimer

    if 200<score<400:
        asteroidtimer -= 15

    elif 400<score<700:
        asteroidtimer -=20


basesound.play()
running = True
while running:
    screen.fill((0,0,0))#흰색으로 화면 지우기

    for event in pygame.event.get(): #키보드 마우스
        if event.type == pygame.QUIT:# X를 누르면 게임 중료
            pygame.quit()
            exit(0)

    score += 1
    text(score,400,10)

    if x_plus > 300:
        y = 1

    if x_plus < 50:
        y = 0

    if y == 1:
        x_plus -= 1
    if y == 0:
        x_plus += 1

    #level_up()
    speed_up()
    #landingsound.play()
    #basesound.play()

    #screen.blit(heartimg,(20,30))
    #screen.blit(itemimg,(50,200))

    position = pygame.mouse.get_pos()#마우스의 위치를 position에 저장
    spaceshippos = (position[0], 550)#spaceship 위치를 마우스위치 사용하여 세팅
    gunpos = (position[0], 550)
    bosspos = (x_plus,10)

    spaceshiprect = pygame.Rect(spaceshipimg.get_rect()) #spaceship사각형 좌표
    spaceshiprect.left = spaceshippos[0] #왼쪽
    spaceshiprect.top = spaceshippos[1] # 위쪽

    bossrect = pygame.Rect(bossimg.get_rect())
    bossrect.left = bosspos[0]
    bossrect.top = bosspos[1]



    asteroidtimer -= 10 #새로운 운석을 리스트에 추가
    guntimer -= 10
    bossguntimer -=10


    if bossguntimer <= 0:
        bossguns.append([x_plus,10])
        bossguntimer = random.randint(50,200)

    if asteroidtimer <= 0:
        asteroids.append([random.randint(5,475),0, random.randint(0,2)])
        asteroidtimer = random.randint(50,200)


    if guntimer <= 0:
        guns.append([position[0],550])

        guntimer = 100



    '''
    index = 0
    for stone in asteroids:

        stone[1] += 10  #이속 stone[0]은 x좌표 stone[1]은 y좌표 stone[2]는 state

        if stone[1] > 640:
            asteroids.pop(index) #바닥에 닿으면 삭제


        stonerect = pygame.Rect(asteroidimgs[stone[2]].get_rect()) #운석
        stonerect.left = stone[0]
        stonerect.top = stone[1]

        if stonerect.colliderect(spaceshiprect):
            landingsound.play()
            asteroids.pop(index)
            running = False


        screen.blit(asteroidimgs[stone[2]],(stone[0], stone[1]))
        index += 1
        '''


    index_1 = 0
    count_1 = -1
    k = 0

    for bossgun in bossguns:

        bossgun[1] +=10

        if bossgun[1] > 640:
            bossguns.pop(index_1)

        bossgunrect = pygame.Rect(bossgunimg.get_rect())
        bossgunrect.left = bossgun[0]
        bossgunrect.top = bossgun[1]

        index_1 += 1

        if bossgunrect.colliderect(spaceshiprect):
            screen.blit(bombimg,(position[0], 550))
            pygame.display.flip()
            bombsound.play()
            running = False


        screen.blit(bossgunimg,(bossgun[0]+130 , bossgun[1]))
        screen.blit(bossgunimg,(bossgun[0] , bossgun[1]))




    index_2 = 0
    for spaceshipgun in guns:
        spaceshipgun[1]-= 10

        if spaceshipgun[1] < 0:
            guns.pop(index_2)

        spaceshipgunrect = pygame.Rect(gunimg.get_rect())
        spaceshipgunrect.left = spaceshipgun[0]
        spaceshipgunrect.top = spaceshipgun[1]

        screen.blit(gunimg,(spaceshipgun[0], spaceshipgun[1]))


        index_2 += 1

        if spaceshipgunrect.colliderect(bossrect):
            bombsound.play()







    screen.blit(bossimg, (x_plus,10))
    screen.blit(spaceshipimg, spaceshippos)# spaceshippos에 위치에 spaceship을 그림
    #screen.blit(supporterimg,(position[0]-20,570))
    #screen.blit(supporterimg,(position[0]+60,570))


    fpsClock.tick(FPS) #게임 속도 #어떤 컴퓨터이건 일정한 속도


    pygame.display.flip()#화면 전체 업데이트


screen.blit(gameover, (0,0))# gameover 화면


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
