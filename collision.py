import sys,pygame

BLACK=(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED=(255,0,0)
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("moving box")

clock = pygame.time.Clock()

box_y = 300
box_a = 30
box_dir1 = 6
box_x=300
box_dir2=6
box_z = 300
box_dir2 = 6
box_w=300
box_dir1=6
box_y1 = 30
box_dir1 = 6
box_x1=300
box_dir2=6
box_z1 = 300
box_dir2 = 6
box_w1=300
box_dir1=6
x_coord=320
y_coord=200
x_speed=0
y_speed=0

     
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
 
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
 
        
        elif event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
        
    if abs(x_coord-30)<30 and abs(y_coord-box_y)<30:
        pygame.quit()
    if abs(x_coord-100)<65 and abs(y_coord-box_w)<30:
        pygame.quit()
    if abs(x_coord-170)<20 and abs(y_coord-box_z)<30:
        pyagme.quit()
    if abs(x_coord-230)<30 and abs(y_coord-box_x)<30:
        pygame.quit()
    if abs(x_coord-290)<30 and abs(y_coord-box_y1)<30:
        pygame.quit()
    if abs(y_coord-80)<30 and abs(x_coord-box_w1)<30:
        pygame.quit()
    if abs(y_coord-170)<30 and abs(x_coord-box_z1)<30:
        pygame.quit()
    if abs(y_coord-280)<30 and abs(x_coord-box_x1)<30:
        pygame.quit()    

    screen.fill(BLACK)

    box_y+=box_dir1
    if box_y>=460: 
        box_y=460
        box_dir1=-6

    elif box_y<=0:
        box_y=0
        box_dir2=6

    box_x+=box_dir2
    if box_x>=460:
        box_x=460
        box_dir2=-6

    elif box_x<=0:
        box_x=0
        box_dir2=6
    box_z+=box_dir1
    if box_z>=460:
        box_z=460
        box_dir1=-6
    elif box_z<=0:
        box_z=0
        box_dir2=6
        
    box_w+=box_dir2
    if box_w>=460:
        box_w=460
        box_dir2=-6

    elif box_w<=0:
        box_w=0
        box_dir2=6
    

    box_y1+=box_dir1
    if box_y1>=460:
        box_y1=460
        box_dir1=-6

    elif box_y1<=0:
        box_y1=0
        box_dir2=6

    box_x1+=box_dir2
    if box_x1>=4640:
        box_x1=640
        box_dir2=-6

    elif box_x1<=0:
        box_x1=0
        box_dir2=6
    box_z1+=box_dir1
    if box_z1>=640:
        box_z1=640
        box_dir2=-6
    elif box_z1<=0:
        box_z1=0
        box_dir1=6
        
    box_w1+=box_dir2
    if box_w1>=640:
        box_w1=640
        box_dir2=-6

    elif box_w1<=0:
        box_w1=0
        box_dir2=6
    
 
 
    pygame.draw.rect(screen,GREEN,pygame.Rect(30,box_y,30,30))
    pygame.draw.rect(screen,WHITE,pygame.Rect(x_coord,y_coord,30,30))
     

    pygame.draw.rect(screen,RED,pygame.Rect(100,box_w,30,30))
    pygame.draw.rect(screen,RED,pygame.Rect(170,box_z,30,30))
    pygame.draw.rect(screen,RED,pygame.Rect(230,box_x,30,30))

    pygame.draw.rect(screen,GREEN,pygame.Rect(290,box_y1,30,30))

    pygame.draw.rect(screen,GREEN,pygame.Rect(box_w1,80,30,30))
    pygame.draw.rect(screen,RED,pygame.Rect(box_z1,170,30,30))
    pygame.draw.rect(screen,GREEN,pygame.Rect(box_x1,280,30,30))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()


sys.exit()
