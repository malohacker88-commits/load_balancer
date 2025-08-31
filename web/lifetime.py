from contextlib import asynccontextmanager

import asyncpg
from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise

from db.config import TORTOISE_CONFIG
from db.models import Configs
from web.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    await setup_db(app)
    async with RegisterTortoise(
        app,
        config=TORTOISE_CONFIG,
        add_exception_handlers=True,
        generate_schemas=False,
    ):
        yield
    configs = await Configs.first()
    if configs:
        if configs.cdn_host:
            settings.cdn_host = configs.cdn_host
        if configs.frequency:
            settings.balancing_frequency = configs.frequency
    yield
    await close_db(app)


async def setup_db(app: FastAPI) -> None:
    """
    Creates connection pool for postgres.

    :param app: current FastAPI app.
    """

    app.state.service_db_pool = await asyncpg.create_pool(
        dsn=str(settings.service_db_url),
        max_size=settings.service_db_pool_max_size,
    )


async def close_db(app: FastAPI) -> None:
    """
    Close connection pool for timescaledb.

    :param app: current FastAPI app.
    """
    await app.state.service_db_pool.close()
