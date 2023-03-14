from fastapi import APIRouter

from .arcticles import router as router_articles
from .pharmacy import router as router_pharmacy
from .users import router as router_users


router = APIRouter()
router.include_router(router_articles)
router.include_router(router_pharmacy)
router.include_router(router_users)
