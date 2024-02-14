import pygame


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

# FUll player class with interpolated movement and fully fledged fiziks including dragforce


class Player:
    def __init__(self, startX, startY, screenWidth, screenHeight):
        self.position = pygame.Vector2(startX, startY)
        self.playerRadius = 30
        self.playerColor = pygame.Color('red')
        self.velocity = pygame.Vector2(0, -1000)
        self.acceleration = 3500
        self.maxVelocity = 800
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.dragForceIntensity = 3  # Adjust as necessary
        self.dragForce = pygame.Vector2(0, 0)
        self.sprite = pygame.image.load('Assets/player1.png')
        self.gravity = 900
        self.rect = self.sprite.get_rect(topleft=(self.position.x,self.position.y))

    def check_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.get_rect()) and self.velocity.y > 0 and self.position.y < platform.position.y:
                platform.kill()
                self.velocity.y = -2000
                pass

    def display(self, screen):
        # pygame.draw.circle(screen, self.playerColor, self.position, self.playerRadius)
        screen.blit(self.sprite, (self.position.x -
                    self.playerRadius, self.position.y - self.playerRadius))
        if (self.position.x >= self.screenWidth + self.playerRadius / 2):
            self.position.x = 0 + self.playerRadius / 2
        if (self.position.x <= -self.playerRadius / 2):
            self.position.x = self.screenWidth - self.playerRadius / 2

    def move(self, dt):
        keys = pygame.key.get_pressed()
        acceleration = self.acceleration * dt
        self.velocity.y += self.gravity * dt

        # Calculate drag force
        self.dragForce = -self.dragForceIntensity * self.velocity

        if keys[pygame.K_a]:
            self.velocity.x = clamp(
                self.velocity.x - acceleration, -self.maxVelocity, self.maxVelocity)
        if keys[pygame.K_d]:
            self.velocity.x = clamp(
                self.velocity.x + acceleration, -self.maxVelocity, self.maxVelocity)

        # Apply drag force
        self.velocity += self.dragForce * dt

        self.position += self.velocity * dt
        self.rect = self.sprite.get_rect(topleft=(self.position.x,self.position.y))
