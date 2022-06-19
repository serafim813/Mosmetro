import sys
sys.path = ['', '..'] + sys.path[1:]
from src.core.settings import logger
import asyncio
import sqlalchemy as sa

from src.database import create_database_url
from src.api.protocols import UserServiceProtocol
from fastapi import Depends
from src.user.service import UserService

engine = sa.create_engine(
        create_database_url(),
        future=True
)
service = UserService(engine)
logger.info("Start update!!!")

def add_answer(
    #user_service: UserServiceProtocol = Depends()
):
    return service.get_all_news()

logger.info("Finish update!!!")

if __name__ == "__main__":
    asyncio.run(add_answer())
