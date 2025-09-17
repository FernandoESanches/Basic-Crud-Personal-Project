from models.Game import Game
from db.GameRepository import GameRepository

class GameManager:
    def __init__(self, db):
        self.repo = GameRepository(db)

    def validate(self, game: Game):
        errors = {}
        if game.score is not None and not ('0' <= game.score <= '5'):
            errors["score"] = "Score must be between 0 and 5"
        if not game.platform:
            errors["platform"] = "Platform is required"
        return errors

    def create_game(self, game: Game):
        errors = self.validate(game)
        if errors:
            return {"error": "Validation failed", "details": errors}, 400

        game_id = self.repo.insert(game)
        return {"message": "Game created", "id": game_id}, 201

    def get_all_games(self):
        return {"data": self.repo.list_all()}, 200

    def delete_game(self, game_id: int):
        existing = self.repo.find_by_id(game_id)
        if not existing:
            return {"error": "Game not found"}, 404
        self.repo.delete(game_id)
        return {"message": "Game deleted"}, 204