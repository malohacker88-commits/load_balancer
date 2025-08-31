from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = True

    # Variables for the database
    service_db_host: str = "127.0.0.1"
    service_db_port: int = 5432
    service_db_user: str = "balancer"
    service_db_pass: str = "balancer"
    service_db_base: str = "balancer"

    service_db_pool_max_size: int = 10

    cdn_host: str = "cdn"
    balancing_frequency: int = 5

    @property
    def service_db_url(self) -> URL:
        """
        Assemble antares database URL from settings.

        :return: antares database URL.
        """
        return URL.build(
            scheme="postgres",
            host=self.service_db_host,
            port=self.service_db_port,
            user=self.service_db_user,
            password=self.service_db_pass,
            path=f"/{self.service_db_base}",
        )

    class Config:
        env_file = ".env"
        env_prefix = "BALANCER_"
        env_file_encoding = "utf-8"


settings = Settings()
