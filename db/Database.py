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
            raise Exception(f"Execution Error: {e}")

    def execute_query_and_fetch(self, query, params=None):
        """Executes INSERT, UPDATE, DELETE statements, returning the affected ID."""
        try:
            with self.engine.connect() as conn:
                insert = conn.execute(text(query), params or {})
                conn.commit()
                return insert.fetchone()
        except SQLAlchemyError as e:
            raise Exception(f"Execution Error: {e}")

    def fetch_query(self, query, params=None):
        """Executes SELECT statements and returns results as list of dicts."""
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query), params or {})
                rows = result.fetchall()
                return [dict(row._mapping) for row in rows]
        except SQLAlchemyError as e:
            raise Exception(f"Fetch Error: {e}")
