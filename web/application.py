from fastapi import FastAPI

from web.lifetime import lifespan
from web.api.router import api_router


def init_app() -> FastAPI:  # noqa: WPS213
    """
    Инициализация и получение экземпляра приложения.

    :return: экземпляр приложения.
    """
    app = FastAPI(
        title="balancer",
        description="",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )

    app.include_router(api_router)

    return app
