from datetime import datetime
from enum import Enum, unique
from typing import Annotated, Self

from fastapi import Form
from pydantic import BaseModel, Field

from schemas.pydantics.cfg_base_model import ConfigBaseModelResponseDTO


@unique
class StatusForm(str, Enum):
    """Статусы мероприятия"""

    PUBLISHED = "опубликовано"
    COMPLETED = "завершено"
    DRAFT = "черновик"


@unique
class CategoriesForm(str, Enum):
    """Категории мероприятия"""

    CONCERT = "Концерт"
    FESTIVAL = "Фестиваль"
    CONFERENCE = "Конференция"
    EXHIBITION = "Выставка"
    SPORT = "Спорт"
    THEATRE = "Театр"
    OTHER = "Другое"


class CreateEventDTO(BaseModel):
    """Модель данных для создания мероприятия (валентинки)"""

    text: str
    recipient_email: str
    author_email: str
    dispatch_date: datetime
    is_public: bool

    @classmethod
    def validate_form(
        cls,
        text: Annotated[
            str,
            Form(
                ...,
                description="Текст валентинки",
                examples=["Я тебя люблю!", "С днем святого Валентина!"],
                min_length=1,
                max_length=1000,
            ),
        ],
        recipient_email: Annotated[
            str,
            Form(
                ...,
                description="Email получателя",
                examples=["anna@example.com", "friend@gmail.com"],
                min_length=5,
                max_length=321,
            ),
        ],
        author_email: Annotated[
            str,
            Form(
                ...,
                description="Email автора",
                examples=["petya@example.com", "me@mail.ru"],
                min_length=5,
                max_length=321,
            ),
        ],
        dispatch_date: Annotated[
            str,  # FastAPI Form принимает строку, потом конвертируем
            Form(
                ...,
                description="Дата отправки (в формате YYYY-MM-DD HH:MM:SS)",
                examples=["2024-02-14 10:00:00", "2024-02-14 12:30:00"],
            ),
        ],
        is_public: Annotated[
            bool,
            Form(
                ...,
                description="Публичная ли валентинка",
                examples=[True, False],
            ),
        ],
    ) -> Self:
        return cls(**locals())


class CreateEventResponseDTO(ConfigBaseModelResponseDTO):
    id: int
    text: str
    recipient_email: str
    author_email: str
    dispatch_date: datetime
    is_public: bool

# [EditEvent]
class EditEventDTO(BaseModel):
    """Модель данных для редактирования мероприятия"""

    status: Annotated[StatusForm | None, Field(description="Статус мероприятия")] = None

    title: Annotated[
        str | None,
        Field(
            description="Название мероприятия",
            examples=["Конференция по Python"],
            min_length=2,
            max_length=50,
        ),
    ] = None

    description: Annotated[
        str | None,
        Field(
            description="Описание мероприятия",
            examples=["Ежегодная конференция для разработчиков"],
            min_length=10,
            max_length=10_000,
        ),
    ] = None

    address: Annotated[
        str | None,
        Field(
            description="Адрес мероприятия",
            examples=["Ул. Штурманская, д. 30"],
            min_length=5,
            max_length=100,
        ),
    ] = None


class EditEventResponseDTO(CreateEventResponseDTO):
    pass


# [AllElements]
class AllElementsResponseDTO(CreateEventResponseDTO):
    pass
