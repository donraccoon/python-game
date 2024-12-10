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


# Draw paddles and ball on the screen
def draw():
    screen.fill(black)  # Fill the screen with black (clear screen)
    
    # Draw paddles (player 1 and player 2)
    pygame.draw.rect(screen, white, (player1_x, player1_y, paddle_width, paddle_height))  # Player 1 paddle
    pygame.draw.rect(screen, white, (player2_x, player2_y, paddle_width, paddle_height))  # Player 2 paddle
    
    # Draw ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_width, ball_width))  # Ball
    
    # Update the display
    pygame.display.update()


# Main game loop
running = True
while running:
    clock.tick(60)  # Run at 60 frames per second
    
    # Event loop to check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicks the close button
            running = False  # End the game loop
    
    # Get pressed keys for paddle movement
    keys = pygame.key.get_pressed()
    
    # Player 1 movement (W and S keys)
    if keys[pygame.K_w] and player1_y > 0:  # Move up if W is pressed and paddle is not at the top
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:  # Move down if S is pressed and paddle is not at the bottom
        player1_y += paddle_speed
    
    # Player 2 movement (Up and Down arrow keys)
    if keys[pygame.K_UP] and player2_y > 0:  # Move up if UP arrow is pressed and paddle is not at the top
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:  # Move down if DOWN arrow is pressed and paddle is not at the bottom
        player2_y += paddle_speed
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= screen_height - ball_width:  # If ball touches top or bottom
        ball_speed_y *= -1  # Reverse the ball's vertical direction
    
    # Ball collision with paddles
    if (ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height):  # Ball hits player 1 paddle
        ball_speed_x *= -1  # Reverse the ball's horizontal direction
    
    if (ball_x + ball_width >= player2_x and player2_y < ball_y < player2_y + paddle_height):  # Ball hits player 2 paddle
        ball_speed_x *= -1  # Reverse the ball's horizontal direction
    
    # Ball goes out of bounds (score system could be added here)
    if ball_x <= 0 or ball_x >= screen_width:  # Ball goes off-screen (left or right)
        ball_x = screen_width // 2 - ball_width // 2  # Reset ball to the center
        ball_y = screen_height // 2 - ball_width // 2  # Reset ball to the center
        ball_speed_x *= -1  # Reverse ball direction to give it to the other player
    
    # Draw everything on the screen
    draw()

# Quit Pygame properly
pygame.quit()
sys.exit()
