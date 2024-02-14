class GameManager():
    def __init__(self):
        self.running = True

    def getGameOver(self):
        return self.running

    def checkIfGameOver(self, player, screenHeight):
        if (player.position.y > screenHeight):
            self.running = False
