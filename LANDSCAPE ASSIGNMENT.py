import pygame, random, time


# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rainy Day Scene")

def makecloud(cloudxy):
    pygame.draw.circle(window, (162, 162, 162), cloudxy, 40)
    pygame.draw.circle(window, (162,162,162), [cloudxy[0]+30, cloudxy[1]+30], 40)
    pygame.draw.ellipse(window, (162,162,162),(cloudxy[0]-80, cloudxy[1], 150, 75) , 0) 
# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Clouds
cloudxy=[]
for _ in range(random.randint(1,5)):
    cloudxy.append((random.randint(0,1200), random.randint(0, 150)))

# Raindrops
raindrops = []
for _ in range(100):
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    raindrops.append([x, y])
#road lines
roaddown=1

# Main loop
clock = pygame.time.Clock()
finished = False
recwid=1
reclen=1
recwid2=1
reclen2=1
loops=0
while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    # Mouse pos
    mousepos=pygame.mouse.get_pos()
    # Update raindrops
    for i, drop in enumerate(raindrops):
        drop[1] += 5  # Fall down
        if drop[1] > WINDOW_HEIGHT:
            # Reset raindrop position when it reaches the bottom
            drop[1] = random.randint(-20, -1)
            drop[0] = random.randint(0, WINDOW_WIDTH)

    # Draw background
    window.fill(GRAY)
    i=0
    # Draw clouds
    for element in cloudxy:
        makecloud(element)
        hitbox1=element[0]-80
        hitbox2=element[0]+70
        hitbox3=element[1]-40
        hitbox4=element[1]+74
        if mousepos[0]>=hitbox1 and mousepos[0]<=hitbox2 and mousepos[1]>=hitbox3 and mousepos[1]<=hitbox4:
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.draw.line(window, 'yellow', (element[0], element[1]+60), (element[0]-50, element[1]+114), 25)
                pygame.draw.line(window, 'yellow', (element[0]-60, element[1]+114), (element[0]+50, element[1]+114), 10)
                pygame.draw.line(window, 'yellow', (element[0]+50, element[1]+125), (element[0]-50, element[1]+200), 25)

    def non_negative(num):
        return max(num, 0)
#        if mousepos
    # Draw raindrops
    for drop in raindrops:
        pygame.draw.line(window, BLUE, (drop[0], drop[1]), (drop[0], drop[1] + 5), 3)

    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     print(pygame.mouse.get_pos())
    #     time.sleep(1)
    # #draw the road
    pygame.draw.polygon(window, 'black', [(200,750), (1000,750), (600, 300)], 0)
    roadlines= []

    y=720
    width=20
    length=50
    roaddown+=5
    if roaddown>=85:
        roaddown=1
    for _ in range(100):
        roadlines.append([(600+width+non_negative(0.01*(y-325)), y+roaddown+(0.1*roaddown)), (600-width-non_negative(0.01*(y-325)),y+roaddown+(0.1*roaddown)), (600-width,y-length+roaddown), (600+width,y-length+roaddown)])
        length=length*0.8
        width=width*0.8
        y=y*0.9
        if y+roaddown<=300:
            break
    for element in roadlines:
        pygame.draw.polygon(window, 'yellow', (element[0], element[1], element[2], element[3]), 0)
    # pygame.draw.line(window, 'yellow', (600, 300), (600, 750), 20)

    #draw house

    pygame.draw.rect(window, "beige", (600-recwid*2.9, 300+reclen, recwid, reclen))
    pygame.draw.polygon(window, "red", ((600-recwid*2.9, 300+reclen), (600-recwid*1.9, 300+reclen), (600-recwid*2.4,300+reclen*0.6)), 0)
    pygame.draw.rect(window, 'black', (600-recwid*2.8, 300+reclen*1.1, recwid*0.4, reclen*0.4))
    pygame.draw.rect(window, 'blue', (600-recwid*2.75, 300+reclen*1.15, recwid*0.3, reclen*0.3))

    pygame.draw.line(window, 'black', (600-recwid*2.62, 300+reclen*1.15), (600-recwid*2.62, 300+reclen*1.44), 5)
    pygame.draw.line(window, 'black', (600-recwid*2.8, 300+reclen*1.30), (600-recwid*2.44, 300+reclen*1.30), 5)
    
    pygame.draw.rect(window, 'brown', (600-recwid*2.3, 300+reclen*1.4, recwid*0.3, reclen*0.6))

    pygame.draw.line(window, "brown", (600+recwid2*2, 300+reclen2*1.30), (600+recwid2*2, 300+reclen2*2), int(recwid2*0.2))
    pygame.draw.circle(window, 'green',(600+recwid2*2.02, 300+reclen2*1.2), recwid2*0.4, 0)
    if recwid2>=325:
        recwid2=0
        reclen2=0
    elif loops>=50:
        recwid2+=1
        reclen2+=1
    else:
        loops+=1
    
    if recwid>=325:
        recwid=0
        reclen=0
    else:
        recwid+=1
        reclen+=1


    pygame.display.update()
    clock.tick(60)  # Limit frame rate
    
pygame.quit()

