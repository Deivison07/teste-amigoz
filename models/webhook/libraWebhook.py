from typing import Any, Dict
import uuid

from pydantic import BaseModel
from sqlalchemy import JSON
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from config.database import Base

class LibraWebhook(Base):
    __tablename__ = "moedas"
    request_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    data: Mapped[dict] = mapped_column(JSON)

class LibraWebhookModel(BaseModel):
    request_id: uuid.UUID
    data: Dict[str, Any]

