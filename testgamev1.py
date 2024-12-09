import pygame  # Imports the Pygame library to create games and graphical applications before using pygame make sure to install it (pip install pygame)
pygame.init()  # Initializes all Pygame modules to prepare them for use

# Set the screen dimensions
screenWidth = 500  # The width of the screen in pixels
screenHeight = 500  # The height of the screen in pixels

# Create the game window with the specified width and height
win = pygame.display.set_mode((screenWidth, screenHeight))  # Creates the window with a 500x500 pixel size

# Set the title of the window
pygame.display.set_caption("First game")  # Sets the caption of the game window to "First game"

# Define the initial position, size, and speed of the player character
x = 50  # The starting x-coordinate of the character (horizontal position)
y = 425  # The starting y-coordinate of the character (vertical position)
width = 40  # The width of the character in pixels
height = 60  # The height of the character in pixels
vel = 5  # The velocity (speed) at which the character moves in pixels per frame

# Main game loop control variable
run = True  # Variable to keep the game loop running

# Start of the game loop
while run:
    pygame.time.delay(50)  # Delays the loop by 50 milliseconds to control frame rate
    
    # Check for events (like pressing the close button)
    for event in pygame.event.get():  # Loops through all events in the event queue
        if event.type == pygame.QUIT:  # Checks if the event is a quit event (close button)
            run = False  # Ends the game loop by setting run to False

    # Get the current state of all keys (which keys are currently pressed)
    keys = pygame.key.get_pressed()  # Returns a list of all pressed keys
    
    # Movement controls using arrow keys
    if keys[pygame.K_LEFT] and x > vel:  # Move left if the left arrow key is pressed and x > vel
        x -= vel  # Decrease x-coordinate to move the character left
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:  # Move right if right arrow key is pressed and within screen bounds
        x += vel  # Increase x-coordinate to move the character right
    if keys[pygame.K_UP] and y > vel:  # Move up if up arrow key is pressed and y > vel
        y -= vel  # Decrease y-coordinate to move the character up
    if keys[pygame.K_DOWN] and y < screenHeight - height - vel:  # Move down if down arrow key is pressed and within screen bounds
        y += vel  # Increase y-coordinate to move the character down

   
    win.fill((0, 0, 0))  # Fills the window with a black background (RGB color (0, 0, 0))
    pygame.draw.rect(win, (255, 0, 255), (x, y, width, height))  # Draws a magenta rectangle at (x, y) with size (width, height)
    pygame.display.update()  # Updates the screen to reflect changes
    

pygame.quit()  # Ends the Pygame instance and closes the window
