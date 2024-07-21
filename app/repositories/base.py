from fastapi import HTTPException
from sqlalchemy import delete, insert, select, update
from app.database import async_session
from app.expection import CannotAddDataToDatabase, CannotDeleteDataFromDatabase, CannotUpdateDataInDatabase, NotFoundException

class BaseRepositories:
    model = None
    
    @classmethod
    async def get_all(cls, **filter):
        try:
            async with async_session() as session:
                query = select(cls.model).filter_by(**filter)
                result = await session.execute(query)
                return result.scalars().all()
        except HTTPException:
            raise NotFoundException
            
        
    @classmethod
    async def add(cls, **data):
        try:
            async with async_session() as session:
                query = insert(cls.model).values(**data)
                await session.execute(query)
                await session.commit()
        except HTTPException:
            raise CannotAddDataToDatabase
            
    @classmethod
    async def update(cls, id: int, **data):
        try:
            async with async_session() as session:
                query = (
                    update(cls.model)
                    .where(cls.model.id == id)
                    .values(**data)
                )
                await session.execute(query)
                await session.commit()
        except HTTPException:
            raise CannotUpdateDataInDatabase
        
        
    @classmethod
    async def delete(cls, id):
        try:
            async with async_session() as session:
                query = delete(cls.model).where(cls.model.id == id)
                await session.execute(query)
                await session.commit()
        except HTTPException:
            raise CannotDeleteDataFromDatabase     
            
    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter).limit(1)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_by_id(cls, id):
        async with async_session() as session:
            query = select(cls.model).where(cls.model.id == id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
            