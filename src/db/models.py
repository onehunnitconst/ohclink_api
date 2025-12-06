from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.database import Base

class Link(Base):
    __tablename__ = "ol_links"

    id: Mapped[str] = mapped_column(primary_key=True)
    pathname: Mapped[str]
    original_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

