"""
Костыльный модуль взаимодействия с бд без класса. позже нужно сделать как класс и сократить количество функций
"""
from sqlalchemy.orm import Session

from models.models import Valentine
from models.session import DBBaseModel


from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Valentine

async def create_valentine(
    db: AsyncSession, 
    text: str, 
    recipient_email: str, 
    author_email: str, 
    is_public: bool, 
    dispatch_date: datetime = None
):
    if dispatch_date is None:
        dispatch_date = datetime.now()
    
    valentine = Valentine(
        text=text, 
        recipient_email=recipient_email,
        author_email=author_email,
        is_public=is_public,
        dispatch_date=dispatch_date
    )
    
    db.add(valentine)
    db.commit()
    db.refresh(valentine)
    return valentine

async def get_valentine(db: AsyncSession, id: int):
    result = db.execute(
        select(Valentine).where(Valentine.id == id)
    )
    return result.scalar_one_or_none()

async def get_public_valentines(db: AsyncSession):
    result = db.execute(
        select(Valentine).where(Valentine.is_public == True)
    )
    return result.scalars().all()
