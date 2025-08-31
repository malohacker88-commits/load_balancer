from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "configs" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cdn_host" TEXT NOT NULL,
    "frequency" INT NOT NULL
);
COMMENT ON TABLE "configs" IS 'Модель для хранения настроек в БД.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
