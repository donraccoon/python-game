import pygame  # Import the Pygame library
import sys  # Import sys to close the game properly

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800  # Width of the screen
screen_height = 600  # Height of the screen

# Colors (RGB format)
white = (255, 255, 255)
black = (0, 0, 0)
magenta = (255, 0, 255)
green = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))  # Create a screen of 800x600
pygame.display.set_caption("Pong")  # Set the title of the window

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Paddle properties
paddle_width = 20  # Width of the paddle
paddle_height = 100  # Height of the paddle
paddle_speed = 7  # Speed of the paddle

# Ball properties
ball_width = 20  # Width and height of the ball (since it's a square)
ball_speed_x = 5  # Ball speed along the x-axis
ball_speed_y = 5  # Ball speed along the y-axis

# Initial positions of the paddles and ball
player1_x = 20  # X position of player 1's paddle
player1_y = screen_height // 2 - paddle_height // 2  # Y position of player 1's paddle (centered)

player2_x = screen_width - 20 - paddle_width  # X position of player 2's paddle
player2_y = screen_height // 2 - paddle_height // 2  # Y position of player 2's paddle (centered)

ball_x = screen_width // 2 - ball_width // 2  # X position of the ball (centered)
ball_y = screen_height // 2 - ball_width // 2  # Y position of the ball (centered)

# Scores for player 1 and player 2
score_player1 = 0
score_player2 = 0

# Font for displaying scores
font = pygame.font.SysFont("comicsans", 50)  # Font for score display
menu_font = pygame.font.SysFont("comicsans", 70)  # Font for menu


# Draw paddles, ball, and scores on the screen
def draw():
    screen.fill(black)  # Fill the screen with black (clear screen)
    
    # Draw paddles (player 1 and player 2)
    pygame.draw.rect(screen, magenta, (player1_x, player1_y, paddle_width, paddle_height))  # Player 1 paddle
    pygame.draw.rect(screen, green, (player2_x, player2_y, paddle_width, paddle_height))  # Player 2 paddle
    
    # Draw ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_width, ball_width))  # Ball
    
    # Render and display the scores
    score_text1 = font.render(f"{score_player1}", True, magenta)  # Player 1's score
    score_text2 = font.render(f"{score_player2}", True, green)  # Player 2's score
    screen.blit(score_text1, (screen_width // 4, 20))  # Position player 1's score on the left
    screen.blit(score_text2, (screen_width * 3 // 4, 20))  # Position player 2's score on the right
    
    pygame.display.update()


# Display the menu and get the player's choice
def display_menu():
    run = True
    while run:
        screen.fill(black)
        title_text = menu_font.render("Choose Mode", True, white)
        one_player_text = font.render("1 Player", True, white)
        two_player_text = font.render("2 Player", True, white)
        
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
        screen.blit(one_player_text, (screen_width // 2 - one_player_text.get_width() // 2, 250))
        screen.blit(two_player_text, (screen_width // 2 - two_player_text.get_width() // 2, 350))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # 1-player mode
                    return 1
                elif event.key == pygame.K_2:  # 2-player mode
                    return 2


# Main game loop
def main():
    global player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, score_player1, score_player2
    
    player_mode = display_menu()  # Choose between 1-player or 2-player mode
    running = True

    while running:
        clock.tick(60)  # Run at 60 frames per second
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:  # Quit if ESC is pressed
            running = False
        
        # Player 1 movement
        if keys[pygame.K_w] and player1_y > 0:
            player1_y -= paddle_speed
        if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
            player1_y += paddle_speed
        
        # Player 2 movement (AI or player-controlled)
        if player_mode == 2:  # Two-player mode
            if keys[pygame.K_UP] and player2_y > 0:
                player2_y -= paddle_speed
            if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
                player2_y += paddle_speed
        else:  # AI mode for Player 2
            if player2_y + paddle_height // 2 < ball_y:  # AI moves down
                player2_y += paddle_speed
            elif player2_y + paddle_height // 2 > ball_y:  # AI moves up
                player2_y -= paddle_speed

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Ball collision with walls
        if ball_y <= 0 or ball_y >= screen_height - ball_width:
            ball_speed_y *= -1
        
        # Ball collision with paddles
        if (ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height):
            ball_speed_x *= -1
        
        if (ball_x + ball_width >= player2_x and player2_y < ball_y < player2_y + paddle_height):
            ball_speed_x *= -1
        
        # Ball out of bounds
        if ball_x <= 0:  # Player 2 scores
            score_player2 += 1
            ball_x = screen_width // 2 - ball_width // 2
            ball_y = screen_height // 2 - ball_width // 2
            ball_speed_x *= -1
        
        if ball_x >= screen_width:  # Player 1 scores
            score_player1 += 1
            ball_x = screen_width // 2 - ball_width // 2
            ball_y = screen_height // 2 - ball_width // 2
            ball_speed_x *= -1
        
        draw()
    
    pygame.quit()
    sys.exit()


# Run the game
main()
