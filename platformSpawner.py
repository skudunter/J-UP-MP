import random
from platformz import Platform
# Platform Spawner
class PlatformSpawner:
    def __init__(self, max_platforms, screenWidth, screenHeight):
        self.max_platforms = max_platforms
        self.platforms = []
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def spawn_platforms(self):
        for _ in range(self.max_platforms):
            x = random.randint(0, self.screenWidth)
            y = random.randint(0, self.screenHeight)
            platform = Platform(x, y, 'Assets/platform1.png','Assets/platform0.png')
            self.platforms.append(platform)

    def display(self, screen):
        for platform in self.platforms:
            platform.display(screen)