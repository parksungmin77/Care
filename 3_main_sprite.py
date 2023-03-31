import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 640 # 가로크기
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


# 이벤트 루프
running = True # 게임이 진행중?
while running:
    for event in pygame.event.get(): # Tape boshi가 실행되기 위해 반드시 필요한 문장. 어떤이벤트가 발생햇나?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생?
            running = False # 게임이 진행중이 아님

screen.blit(background,(0,0)) #배경 그리기 첫 번째 0은 x 좌표, 두번째 0은 y 좌표

screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 생성

pygame.display.update()

# 게임종료
pygame.quit()