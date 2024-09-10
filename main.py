import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen_width, screen_height = 1100, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spaceship Subtle Bounce")

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Load spaceship image
spaceship = pygame.image.load('spaceship.png')
spaceship = pygame.transform.scale(spaceship, (50, 50))  # Resize spaceship

# Spaceship's starting position (extreme left)
spaceship_x = 50  # Fixed X position
spaceship_y = screen_height // 2  # Start from the middle of the screen

# Set frame rate
clock = pygame.time.Clock()

# Variables for movement
y_velocity = 0
max_velocity = 5  # Cap the velocity to prevent overshooting
smooth_factor = 0.05  # How quickly the spaceship catches up
damping = 0.95  # Reduces velocity gradually for smooth stopping

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse's Y position (only the Y-coordinate matters)
    _, mouse_y = pygame.mouse.get_pos()

    # Calculate difference between spaceship and mouse y-positions
    y_diff = mouse_y - spaceship_y

    # Adjust velocity based on the difference but cap it for smoothness
    y_velocity += y_diff * smooth_factor
    y_velocity = max(min(y_velocity, max_velocity), -max_velocity)  # Cap velocity

    # Apply damping to reduce the velocity over time for a smooth stop
    y_velocity *= damping

    # Update the spaceship's Y position
    spaceship_y += y_velocity

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the spaceship at the fixed X position and updated Y position
    screen.blit(spaceship, (spaceship_x, spaceship_y - spaceship.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)