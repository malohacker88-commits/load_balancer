from starlette import status

from db.models import Configs
from web.api.internal.router import internal_router
from web.settings import settings


@internal_router.post(
    "/configs",
    responses={
        status.HTTP_200_OK: {"model": ""},
        status.HTTP_403_FORBIDDEN: {"description": "Доступ запрещен"},
    },
)
async def update_configs(
    cdn_host: str = None,
    frequency: int = None,
):
    """
    Обновить текущие значения настройек проекта.

    :return: список настроек
    """
    updates = {}
    if cdn_host:
        updates["cdn_host"] = cdn_host
    if frequency:
        updates["frequency"] = frequency
    if updates:
        configs = await Configs.first()
        await configs.update_from_dict(updates)
        await configs.save()
        settings.cdn_host = updates.get("cdn_host", settings.cdn_host)
        settings.balancing_frequency = updates.get(
            "frequency", settings.balancing_frequency
        )


@internal_router.get(
    "/configs",
    responses={
        status.HTTP_200_OK: {"model": ""},
        status.HTTP_403_FORBIDDEN: {"description": "Доступ запрещен"},
    },
)
async def get_configs():
    """
    Получить текущие значения настройек проекта.

    :return:  настроек
    """
    return await Configs.first()
