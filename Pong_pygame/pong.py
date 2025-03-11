import pygame
import sys

# Initialize Pygame and Pygame Mixer
pygame.init()
pygame.mixer.init()

# Load background music and sound effects
pygame.mixer.music.load("cozycoffeehouse.mp3")
pygame.mixer.music.play(loops=-1)

move_up_sound = pygame.mixer.Sound("paddle_sound.wav")
move_down_sound = pygame.mixer.Sound("paddle_sound.wav")
collision_sound = pygame.mixer.Sound("wallhit.mp3")
paddle_col_sound = pygame.mixer.Sound("paddlehit.mp3") 

# Screen settings
screen_width = 800
screen_height = 600
fps = 60

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
magenta = (255, 0, 255)
green = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Paddle properties
paddle_width = 20
paddle_height = 100
paddle_speed = 7

# Ball properties
ball_radius = 10
ball_speed_x = 5
ball_speed_y = 5

# Initial positions
player1_x = 20
player1_y = screen_height // 2 - paddle_height // 2
player2_x = screen_width - 20 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2
ball_x = screen_width // 2
ball_y = screen_height // 2

# Scores
score_player1 = 0
score_player2 = 0

# Font
font = pygame.font.SysFont("comicsans", 50)

# Pause variable and game over flag
paused = True
game_over = False

# Draw everything
def draw():
    screen.fill(black)
    pygame.draw.rect(screen, magenta, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, green, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    score_text1 = font.render(f"{score_player1}", True, magenta)
    score_text2 = font.render(f"{score_player2}", True, green)
    screen.blit(score_text1, (screen_width // 4, 20))
    screen.blit(score_text2, (screen_width * 3 // 4, 20))

    if paused and not game_over:
        paused_text = font.render("Paused", True, white)
        screen.blit(paused_text, (screen_width // 2 - 50, screen_height // 2))
    
    if game_over:
        winner = "Player 1" if score_player1 == 15 else "Player 2"
        game_over_text = font.render(f"{winner} Wins!", True, white)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 30))

        restart_text = font.render("Press R to Restart or Q to Quit", True, white)
        screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 30))
    
    pygame.display.update()

# Handle game over and restart/quit option
def handle_game_over():
    global game_over, score_player1, score_player2, paused
    font = pygame.font.SysFont("comicsans", 30)
    screen.fill(black)
    
    # Game over message
    winner = "Player 1" if score_player1 == 15 else "Player 2"
    game_over_text = font.render(f"{winner} Wins!", True, white)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 30))
    
    # Instructions to Restart or Quit
    restart_text = font.render("Press R to Restart or Q to Quit", True, white)
    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 30))

    pygame.display.update()
    
    # Wait for key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score_player1, score_player2 = 0, 0
                    game_over, paused = False, False
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Main game loop
def main():
    global player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, score_player1, score_player2, paused, game_over, paddle_speed
    running = True
    sound_played = {pygame.K_w: False, pygame.K_s: False, pygame.K_UP: False, pygame.K_DOWN: False}
    
    while running:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    paused = not paused
            if event.type == pygame.KEYUP:
                if event.key in sound_played:
                    sound_played[event.key] = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            running = False

        if not paused and not game_over:
            if keys[pygame.K_w] and player1_y > 0:
                player1_y -= paddle_speed
                if not sound_played[pygame.K_w]:
                    move_up_sound.play()
                    sound_played[pygame.K_w] = True
            if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
                player1_y += paddle_speed
                if not sound_played[pygame.K_s]:
                    move_down_sound.play()
                    sound_played[pygame.K_s] = True
            if keys[pygame.K_UP] and player2_y > 0:
                player2_y -= paddle_speed
                if not sound_played[pygame.K_UP]:
                    move_up_sound.play()
                    sound_played[pygame.K_UP] = True
            if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
                player2_y += paddle_speed
                if not sound_played[pygame.K_DOWN]:
                    move_down_sound.play()
                    sound_played[pygame.K_DOWN] = True

            ball_x += ball_speed_x
            ball_y += ball_speed_y

            if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
                ball_speed_y *= -1
                collision_sound.play()

            if (ball_x - ball_radius <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height):
                ball_speed_x *= -1
                ball_speed_y += (ball_y - (player1_y + paddle_height / 2)) * 0.1
                paddle_col_sound.play()

            if (ball_x + ball_radius >= player2_x and player2_y < ball_y < player2_y + paddle_height):
                ball_speed_x *= -1
                ball_speed_y += (ball_y - (player2_y + paddle_height / 2)) * 0.1
                paddle_col_sound.play()

            if ball_x - ball_radius <= 0:
                score_player2 += 1
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_speed_x, ball_speed_y = 5, 5
                ball_speed_x *= -1
                paddle_speed = 7

            if ball_x + ball_radius >= screen_width:
                score_player1 += 1
                ball_x, ball_y = screen_width // 2, screen_height // 2
                ball_speed_x, ball_speed_y = 5, 5
                ball_speed_x *= -1
                paddle_speed = 7
            
            if score_player1 == 15 or score_player2 == 15:
                game_over = True
                paused = True
                handle_game_over()
        
        draw()
    
    pygame.quit()
    sys.exit()

main()

