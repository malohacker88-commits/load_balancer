from tortoise import fields
from tortoise.models import Model


class Configs(Model):
    """Модель для хранения настроек в БД."""

    cdn_host = fields.TextField()
    frequency = fields.IntField()
