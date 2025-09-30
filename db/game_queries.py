INSERT_GAME = """
        insert into games (gameName, creationUser, updateDate, updateUser, platformCode, statusCode, rating) 
        values (:name, :user, null, null, :platform_id, :status_id, :score)
        RETURNING gameCode
    """

SELECT_ALL_GAMES = """
    select * from vw_games
    order by rating desc
"""

DELETE_GAME = """
    DELETE FROM games WHERE gameCode = :gameCode
"""

UPDATE_GAME_SCORE = """
    UPDATE games set rating = :score WHERE gameCode = :gameCode
"""
