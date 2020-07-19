import pygame
from tkinter import messagebox
from circle import Circle

pygame.init()

gameDisplay = pygame.display.set_mode((800,800))
overlay = pygame.Surface((800,800))

pygame.display.set_caption("painting app")
clock = pygame.time.Clock()
crashed = False

def detect_movement():
    x, y = pygame.mouse.get_rel()
    if x > 0 or y > 0:
        return True
    else:
        return False

brush = Circle(overlay, (0, 0, 255), (400,400), 50)
guide = Circle(gameDisplay, (255, 255, 255), (400,400), 50, 1)

crashed = False

alt = False

drawMode = False

while not crashed:
    guide.color = brush.color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key  == pygame.K_ESCAPE:
                crashed = True
            if event.key == pygame.K_r:
                brush.color = (255, 0, 0)
            if event.key == pygame.K_LEFTBRACKET:
                brush.update_radius(brush.radius-5)
                guide.update_radius(guide.radius-5)
            if event.key == pygame.K_RIGHTBRACKET:
                brush.update_radius(brush.radius+5)
                guide.update_radius(guide.radius+5)              
            if event.key == pygame.K_b:
                brush.color = (0,0,255)
            if event.key == pygame.K_LALT:
                alt = True
                guide.color = (255,0,0) 
            if event.key == pygame.K_SEMICOLON:
                drawMode = not drawMode
            if event.key == pygame.K_g:
                brush.color = (0, 153, 51)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT:
                alt = False
                guide.color = (255,255,255)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawMode = True
            if event.button == 4:
                brush.radius += 4 
                guide.radius += 4
            if event.button == 5:
                brush.radius -= 4
                guide.radius -= 4
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawMode = False
        print(event)
    
    brush.center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    guide.center = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
   
    if not alt and drawMode:
       brush.draw() 
       guide.color = (255,255,255)
    else:
        guide.color = (128,128,128)
    guide.draw() 

    pygame.display.update()
        
    gameDisplay.blit(overlay, [0,0]) 
   
    clock.tick(10000)

pygame.quit()
quit()
