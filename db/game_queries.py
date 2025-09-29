INSERT_GAME = """
        insert into games (gameName, creationUser, updateDate, updateUser, platformCode, statusCode, rating) 
        values (:name, :user, null, null, :platform_id, :status_id, :score)
        RETURNING gameCode
    """

SELECT_ALL_GAMES = """
    SELECT gameCode, gameName, score
    FROM games
    ORDER BY score DESC
"""

DELETE_GAME = """
    DELETE FROM games WHERE gameCode = :gameCode
"""

UPDATE_GAME_SCORE = """
    UPDATE games set score = :score WHERE gameCode = :gameCode
"""

GAME_TABLE = """
    select * from vw_games
"""