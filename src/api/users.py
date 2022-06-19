from fastapi import APIRouter, status, Depends, Path
from typing import List, Dict
from datetime import date, timedelta, datetime

from src.api.protocols import UserServiceProtocol

from src.user.models import StatsAddV1, StatsAddV12
from src.user.service import UserService

router = APIRouter(
    tags=['Users']
)
#
# @router.post(
#     path='/v1/user',
#     status_code=status.HTTP_201_CREATED,
#     summary='Добавить вопросы',
#     description='Добавляет заданное количество вопросов в бд',
# )
# async def add_answer(
#     num: StatsAddV1,
#     user_service: UserServiceProtocol = Depends()
# ):
#     id_answer = await user_service.push_answers(num.questions_num)
#
#     return user_service.get_last_answer(id_answer)
#
#
# @router.get(
#     path='/v1/user',
#     #response_model=List[StatsAddV1],
#     summary='Добавить вопросы',
#     description='Добавляет заданное количество вопросов в бд',
# )
# def add_answer(
#     user_service: UserServiceProtocol = Depends()
# ):
#     return user_service.get_all_news()

@router.get(
    path='/metro/news/{id}',
    response_model=List[StatsAddV1],
    summary='Новости, которые опубликованы за выбранное количество дней',
    description='Новости, которые опубликованы за выбранное количество дней',
)
def get_user_stats(
    id: int = Path(..., ge=1),
    user_service: UserServiceProtocol = Depends(),
):
    return user_service.get_news(id)
#
# @router.get(
#     path='/v1/users/stats1',
#     response_model=List[StatsAddV1],
#     summary='Статистика пользователя за указанный период',
#     description='Статистика пользователя за указанный период',
# )
# def get_user_stats(
#     user_service: UserServiceProtocol = Depends(),
# ):
#     return user_service.delete_user_by_id()
#
#
# @router.get(
#     path='/v1/users/stats12',
#     summary='Статистика пользователя за указанный период',
#     description='Статистика пользователя за указанный период',
# )
# def get_user_stats(
#     user_service: UserServiceProtocol = Depends(),
# ):
#     return user_service.get_all_id_news()