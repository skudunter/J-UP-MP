import pygame

# platform base class,the base class from which all platforms will inherit
class Platform:
    def __init__(self, x, y, sprite_image, sprite_image_secondary):
        self.position = pygame.Vector2(x, y)
        self.sprites = [pygame.image.load(sprite_image).convert_alpha(), pygame.image.load(sprite_image_secondary).convert_alpha()]
        self.hp = 1
        self.rect = self.sprites[0].get_rect(topleft=(x, y))

    def get_rect(self):
        return self.rect

    def display(self, screen):
        screen.blit(self.sprites[self.hp], (self.position.x, self.position.y))

    def kill(self):
        if self.hp > 0:
            self.hp -= 1
        else:
            print('killed')
            self.position = pygame.Vector2(-1000, -1000)
            self.rect = self.sprites[0].get_rect(topleft=(-1000, -1000))

# class for moving platforms,these platforms will move left and right inherited from the platform class
class MovingPlatform(Platform):
    def __init__(self, x, y, sprite_image, sprite_image_secondary, speed, distance):
        super().__init__(x, y, sprite_image, sprite_image_secondary)
        self.speed = speed
        self.distance = distance
        self.direction = 1

    def move(self, dt):
        self.position.x += self.speed * self.direction * dt
        if self.position.x > self.distance or self.position.x < 0:
            self.direction *= -1