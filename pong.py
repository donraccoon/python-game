import pygame  # Import the Pygame library
import sys  # Import sys to close the game properly

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800  # Width of the screen
screen_height = 600  # Height of the screen
fps = 60

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
paddle_speed = 7  # Speed of the player paddle

# Ball properties
ball_radius = 10  # Radius of the ball (for a circle)
ball_speed_x = 5  # Ball speed along the x-axis
ball_speed_y = 5  # Ball speed along the y-axis

# Initial positions of the paddles and ball
player1_x = 20  # X position of player 1's paddle
player1_y = screen_height // 2 - paddle_height // 2  # Y position of player 1's paddle (centered)

player2_x = screen_width - 20 - paddle_width  # X position of player 2's paddle
player2_y = screen_height // 2 - paddle_height // 2  # Y position of player 2's paddle (centered)

ball_x = screen_width // 2  # X position of the ball (centered)
ball_y = screen_height // 2  # Y position of the ball (centered)

# Scores for player 1 and player 2
score_player1 = 0
score_player2 = 0

# Font for displaying scores
font = pygame.font.SysFont("comicsans", 50)  # Font for score display

# Pause variable
paused = True

# Create a transparent surface for the trail effect
trail_surface = pygame.Surface((screen_width, screen_height))
trail_surface.set_alpha(30)  # Set transparency (0 = fully transparent, 255 = fully opaque)
trail_surface.fill(black)  # Trail is black


# Draw paddles, ball, and scores on the screen
def draw():
    # Apply the trail effect (leaves a slight fade of old frames)
    screen.blit(trail_surface, (0, 0))  # Apply the transparent surface
    
    # Draw paddles (player 1 and player 2)
    pygame.draw.rect(screen, magenta, (player1_x, player1_y, paddle_width, paddle_height))  # Player 1 paddle
    pygame.draw.rect(screen, green, (player2_x, player2_y, paddle_width, paddle_height))  # Player 2 paddle
    
    # Draw ball (as a circle)
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    
    # Render and display the scores
    score_text1 = font.render(f"{score_player1}", True, magenta)  # Player 1's score
    score_text2 = font.render(f"{score_player2}", True, green)  # Player 2's score
    screen.blit(score_text1, (screen_width // 4, 20))  # Position player 1's score on the left
    screen.blit(score_text2, (screen_width * 3 // 4, 20))  # Position player 2's score on the right

    # If paused, display "Paused" message
    if paused:
        paused_text = font.render("Paused", True, white)
        screen.blit(paused_text, (screen_width // 2 - paused_text.get_width() // 2, screen_height // 2 - paused_text.get_height() // 2))
    
    pygame.display.update()


# Main game loop
def main():
    global player1_y, player2_y, ball_x, ball_y, ball_speed_x, ball_speed_y, score_player1, score_player2, paused, fps
    
    running = True

    while running:
        clock.tick(fps)  # Run at 60 frames per second  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Toggle pause
                    paused = not paused

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:  # Quit if ESC is pressed
            running = False

        if not paused:  # Only move if the game is not paused
            # Player 1 movement
            if keys[pygame.K_w] and player1_y > 0:
                player1_y -= paddle_speed
            if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
                player1_y += paddle_speed
            
            # Player 2 movement (manual control)
            if keys[pygame.K_UP] and player2_y > 0:
                player2_y -= paddle_speed
            if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
                player2_y += paddle_speed

            if fps <= 200:
                fps += 0.001
                print(fps)


            # Move the ball
            ball_x += ball_speed_x
            ball_y += ball_speed_y
            
            # Ball collision with walls
            if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
                ball_speed_y *= -1
            
            # Ball collision with paddles
            if (ball_x - ball_radius <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height):
                ball_speed_x *= -1
            
            if (ball_x + ball_radius >= player2_x and player2_y < ball_y < player2_y + paddle_height):
                ball_speed_x *= -1
        
        # **Scoring system works even if paused**
        if ball_x - ball_radius <= 0:  # Player 2 scores
            score_player2 += 1
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            ball_speed_x *= -1
            fps == 30

        if ball_x + ball_radius >= screen_width:  # Player 1 scores
            score_player1 += 1
            ball_x = screen_width // 2
            ball_y = screen_height // 2
            ball_speed_x *= -1
            fps == 30
        
        draw()
    
    pygame.quit()
    sys.exit()


# Run the game
main()
