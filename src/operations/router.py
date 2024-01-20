from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from src.operations.schemas import OperationCreate
from src.database import get_async_session
from src.operations.models import operation

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    new_operation.date = new_operation.date.replace(tzinfo=timezone.utc).astimezone(timezone.utc).replace(tzinfo=None)
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}