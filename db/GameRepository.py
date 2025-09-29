from db.game_queries import *
from models.Game import Game

class GameRepository:
    def __init__(self, db):
        self.db = db

    def insert_game(self, game: Game):
        result = self.db.execute_query_and_fetch(
            INSERT_GAME,
            {
                "name": game.name,
                "user": "harcoded lol",
                "score": game.score,
                "platform_id": game.platform,
                "status_id": game.status,
            }
        )
        return result[0]

    def list_all(self):
        return self.db.fetch_query(SELECT_ALL_GAMES)

    def delete(self, game_id):
        self.db.execute_query(DELETE_GAME, {"id": game_id})