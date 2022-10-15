import pygame

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()
run = True
moused = False

world_test = [[0 for x in range(40)] for j in range(40)]

def gridlines():
    [pygame.draw.line(DISPLAY, "gray", (0, i * 20), (800, i * 20)) for i in range(40)]
    [pygame.draw.line(DISPLAY, "gray", (i * 20, 0), (i * 20, 800)) for i in range(40)]

def sand():
    # for i in range(40 - 1):
        # for j in range(40):
            # if world_test[i][j] and i < 40 and not world_test[i + 1][j]:
                # world_test[i][j] = 0
                # world_test[i + 1][j] = 1
                
    for i in range(40 - 1, -1, -1): # reverse for loops for the sand, ends with -1 for it to be 0
        for j in range(40 - 1, -1, -1):
            # print(i, j)
            if world_test[i][j]:
                if i < 39 and not world_test[i + 1][j]:
                    world_test[i][j] = 0
                    world_test[i + 1][j] = 1
                    
            if world_test[i][j]:
                if j > 0 and i < 39 and world_test[i + 1][j] and not world_test[i + 1][j - 1]:
                    world_test[i][j] = 0
                    world_test[i + 1][j - 1] = 1
                
            if world_test[i][j]:
                if j < 39 and i < 39 and world_test[i + 1][j] and not world_test[i + 1][j + 1]:
                    world_test[i][j] = 0
                    world_test[i + 1][j + 1] = 1
                    
    for i in range(40):
        for j in range(40):
            mousex, mousey = pygame.mouse.get_pos()
            # print(i, j)
            test_rect = pygame.Rect(j * 20, i * 20, 20, 20)
            if abs(test_rect.center[0] - mousex) <= 10 and abs(test_rect.center[1] - mousey) <= 10 and moused:
                world_test[i][j] = 1
    
    for i in range(40):
        for j in range(40):
            if world_test[i][j]:
                pygame.draw.rect(DISPLAY, "yellow", (j * 20, i * 20, 20, 20))


while run:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moused = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moused = False

    key = pygame.key.get_pressed()
    
    DISPLAY.fill("black")
    
    sand()
    
    # gridlines()
    
    
    pygame.display.update()
    
pygame.quit()