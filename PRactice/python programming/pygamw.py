import pygame
import random
x = pygame.init()
#print(x)
#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)


# Creating Display for python game
GW= pygame.display.set_mode((800,600))
pygame.display.set_caption("Sameer's Game")
pygame.display.update()
# Background
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GW.blit(screen_text, [x, y])    

def plot_snake(GW, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.ellipse(GW, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    with open("Highscore.txt", "r") as f:
        highscore = f.read()
    snk_list = []
    snk_length = 1    
    exitgame = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 60
    veloofx = 0
    veloofy = 0
    initial_veloofx = 5
    initial_veloofy = 5
    food_x = random.randint(20, GW.get_width()-100)   
    food_y = random.randint(20, GW.get_height()-100) 
    score = 0   
    while not exitgame:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(highscore))
            GW.fill(white)
            #text_screen("Game Over", red, GW.get_width()/2 - 100, GW.get_height()/2)
            text_screen("Game Over! Press Enter to Restart", red, 100, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        veloofx = initial_veloofx
                        veloofy = 0

                    if event.key == pygame.K_LEFT: 
                        veloofx = - initial_veloofx
                        veloofy = 0
                    if event.key == pygame.K_UP:
                        veloofy = - initial_veloofy
                        veloofx = 0
                    if event.key == pygame.K_DOWN:
                        veloofy = initial_veloofy
                        veloofx = 0
            snake_x += veloofx
            snake_y += veloofy

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score += 10
                food_x = random.randint(20, GW.get_width()-100)   
                food_y = random.randint(20, GW.get_height()-100)
                snk_length += 5
            if score>int(highscore):
                highscore = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            #snk_list.append([snake_x, snake_y])
            
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            GW.fill(white) 
            text_screen("Score: " + str(score) + "           High Score :" + str(highscore), blue, 5, 5)
            pygame.draw.rect(GW, red, [food_x, food_y, snake_size, snake_size]) 
            if snake_x < 0 or snake_x>GW.get_width() or snake_y < 0 or snake_y>GW.get_height():
                game_over = True

            plot_snake(GW,black,snk_list,snake_size)
        clock.tick(fps)
        pygame.display.update() 


    pygame.quit()
    quit()

gameloop()