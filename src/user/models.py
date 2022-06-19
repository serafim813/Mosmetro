from datetime import date, datetime

from pydantic import BaseModel, validator


class StatsAddV12(BaseModel):
    id: int
    header: str
    image: str
    item: str
    date: str


class StatsAddV1(BaseModel):
    header: str
    image: str
    date: str
