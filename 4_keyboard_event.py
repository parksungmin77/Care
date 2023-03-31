import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 설정값을 screen이라는 변수에 받

# 화면 타이틀 설정
pygame.display.set_caption("Tape boshi") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/USER/Desktop/pygame/background.png")

# 캐릭터 부르기
character = pygame.image.load("C:/Users/USER/Desktop/pygame/캐릭터.png")
character_size = character.get_rect().size # 이미지의 크기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)# 화면 가로의 절반 크기에 해당하는 곳에 위치 (가)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당되는 곳에 위치 (세)

# 이동 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중?
while running:
    for event in pygame.event.get(): # Tape boshi가 실행되기 위해 반드시 필요한 문장. 어떤이벤트가 발생햇나?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽
                to_x -=5 # to_x = to_x -5
            elif event.key == pygame.K_RIGHT: # 오른쪽
                to_x +=5
            elif event.key == pygame.K_UP: # 위
                to_y -=5
            elif event.key == pygame.K_DOWN: # 아래
                to_y +=5

        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춘다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

character_x_pos += to_x
character_y_pos += to_y

# 가로 경계값 처리
if character_x_pos < 0:
    character_x_pos = 0
elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

# 세로 경계값 처리
if character_y_pos < 0:
    character_y_pos = 0
elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height

screen.blit(background, (0,0)) #배경 그리기 첫 번째 0은 x 좌표, 두번째 0은 y 좌표

screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 생성

pygame.display.update()  # 게임 화면을 다시 그리기!

# 게임종료
pygame.quit()