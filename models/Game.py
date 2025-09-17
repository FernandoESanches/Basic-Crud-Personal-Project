class Game:
    def __init__(self, gameCode, name, platform, status, score):
        self.gameCode = gameCode if gameCode else None
        self.name = name
        self.platform = platform
        self.status = status
        self.score = score

