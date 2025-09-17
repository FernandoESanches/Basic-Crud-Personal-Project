from db.game_queries import *
from models.Game import Game

class GameRepository:
    def __init__(self, db):
        self.db = db

    def insert(self, game: Game):
        self.db.execute_query(
            INSERT_GAME,
            {
                "name": game.name,
                "user": "harcoded lol",
                "score": game.score,
                "platform": game.platform,
                "status": game.status,
            }
        )

        result = self.db.fetch_query("SELECT LAST_INSERT_ID() as id")
        return result[0]["id"]

    def list_all(self):
        return self.db.fetch_query(SELECT_ALL_GAMES)

    def delete(self, game_id):
        self.db.execute_query(DELETE_GAME, {"id": game_id})