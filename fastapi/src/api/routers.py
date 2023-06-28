from fastapi import APIRouter

from api.endpoints.apartment import router_apartment
from api.endpoints.group import router_group

router = APIRouter()

router.include_router(router_apartment)
router.include_router(router_group)
