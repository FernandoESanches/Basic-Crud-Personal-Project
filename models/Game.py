class Game:
    def __init__(self, game_code, name, platform, status, rating):
        self.gameCode = game_code if game_code else None
        self.name = name,
        self.platform = platform,
        self.status = status,
        self.rating = rating

