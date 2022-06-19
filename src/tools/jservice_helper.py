from sqlalchemy import insert
from sqlalchemy.future import Engine

from src.user.models import StatsAddV12
from src.database import tables


class Jservice:
    """Class for push news"""
    
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def push_news_in_database(self, answer: StatsAddV12) -> None:
        query = insert(tables.news).values(
            id=answer.id,
            header=answer.header,
            image=answer.image,
            date=answer.date,
            item=answer.item,
        )
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()
