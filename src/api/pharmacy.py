from fastapi import APIRouter, Depends

from apps.commons.manager import ManagerBase
from apps.pharmacy.schemas import PharmacyDetailed, PharmacyCreate
from sqlalchemy.ext.asyncio import AsyncSession

from apps.pharmacy.services import ServicePharmacy
from db.database import get_session

router = APIRouter(prefix='/pharmacy', tags=['Pharmacy'])


@router.post(
    path='',
    name='Create Pharmacy',
    operation_id='create_pharmacy',
    response_model=PharmacyDetailed,
    tags=['Pharmacy'],
    status_code=201,
)
async def save(
        data: PharmacyCreate,
        session: AsyncSession = Depends(get_session)
) -> PharmacyDetailed:
    manager = ManagerBase(session)
    service = ServicePharmacy(manager)
    return await service.create(data)
