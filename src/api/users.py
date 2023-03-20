from fastapi import APIRouter, Depends

from apps.commons.manager import ManagerBase
from apps.users.schemas import UserCreate, UserDetailed
from sqlalchemy.ext.asyncio import AsyncSession

from apps.users.services import ServiceUser
from db.database import get_session

router = APIRouter(prefix='/users', tags=['User'])


@router.post(
    path='',
    name='Create User',
    operation_id='create_user',
    response_model=UserDetailed,
    tags=['User'],
    status_code=201,
)
async def save(
        data: UserCreate,
        session: AsyncSession = Depends(get_session)
) -> UserDetailed:
    manager = ManagerBase(session)
    service = ServiceUser(manager)
    return await service.create(data)
