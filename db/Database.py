from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class DataBase:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)

    def execute_query(self, query, params=None):
        """Executes INSERT, UPDATE, DELETE statements."""
        try:
            with self.engine.connect() as conn:
                conn.execute(text(query), params or {})
                conn.commit()
        except SQLAlchemyError as e:
            print(f"Execution Error: {e}")

    def fetch_query(self, query, params=None):
        """Executes SELECT statements and returns results as list of dicts."""
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query), params or {})
                rows = result.fetchall()
                return [dict(row._mapping) for row in rows]
        except SQLAlchemyError as e:
            print(f"Fetch Error: {e}")
            return []