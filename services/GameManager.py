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
        try:
            errors = self.validate(game)
            if errors:
                return {"data": [], "message": "Validation failed", "details": errors}, 400

            game_id = self.repo.insert_game(game)
            return {"data": game_id, "message": "Game created successfully"}, 201

        except Exception as e:
            return {"data": [], "message": "Error creating game", "details": e.args[0]}, 500

    def get_all_games(self):
        try:
            return {"data": self.repo.list_all()}, 200
        except Exception as e:
            return {"data": [], "message": "Error fetching games list", "details": e.args[0]}, 500

    def delete_game(self, game_id: int):
        try:
            existing = self.repo.find_by_id(game_id)
            if not existing:
                return {"error": "Game not found"}, 404
            self.repo.delete(game_id)
            return {"message": "Game deleted"}, 204

        except Exception as e:
            return {"data": [], "message": "Error deleting game", "details": e.args[0]}, 500