from fastapi import APIRouter

from web.api.internal.router import internal_router
from web.api.public.router import public_router

api_router = APIRouter()
api_router.include_router(public_router)
api_router.include_router(internal_router, prefix="/internal")
