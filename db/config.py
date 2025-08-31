from typing import List

from web.settings import settings

MODELS_MODULES: List[str] = ["db.models"]  # noqa: WPS407

TORTOISE_CONFIG = {
    "connections": {
        "default": str(settings.service_db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
