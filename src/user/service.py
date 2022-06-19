from typing import List, Dict
from sqlalchemy import select, delete
from sqlalchemy.future import Engine
import sqlalchemy as sa
from datetime import date, timedelta, datetime

from src.database import create_database_url
engine = sa.create_engine(
        create_database_url(),
        future=True
)
from src.tools.jservice_helper import Jservice
from src.tools.helper import parser_news
from src.database import tables
from src.user.models import (
    StatsAddV1,
    StatsAddV12,
)

class UserService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_all_id_news(self) -> Dict:
        query = select(tables.news.c.id)
        with self._engine.connect() as connection:
            ids = connection.execute(query).fetchall()
        return {t_id[0] for t_id in ids}

    def push_all_news(self):
        url = 'http://mosday.ru/news/tags.php?metro'
        all_news = parser_news(url)
        github = Jservice(self._engine)
        all_id_news = UserService.get_all_id_news(self)
        for all_new in all_news:
            for news in all_new:
                if news[0] not in all_id_news:
                    github.push_news_in_database(answer=StatsAddV12(
                                id=news[0],
                                header=news[1],
                                image=news[2],
                                date=str(datetime.strptime(news[3], "%d.%m.%Y").date()),
                                item=news[4],
                    ))

    def get_news(self, id) -> List[StatsAddV1]:
        """Get news in databases"""
        UserService.push_all_news(self)
        date_from: date = (datetime.now() - timedelta(days=id)).date(),
        date_to: date = (datetime.now()).date(),
        query = select(tables.news).where(
                tables.news.c.date.between(date_from, date_to)
        )

        with self._engine.connect() as connection:
            news = connection.execute(query)
        return [StatsAddV1(
                            header=new[1],
                            image=new[2],
                            date=str(new[3]),
        ) for new in news
        ]

    def delete_news(self) -> None:
        query = delete(tables.news)
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()
