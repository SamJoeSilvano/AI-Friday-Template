from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.core.database import Base


class SignOff(Base):
    __tablename__ = "signoffs"

    id = Column(Integer, primary_key=True, index=True)
    requirement_version_id = Column(Integer, nullable=False)
    status = Column(String, nullable=False)  # APPROVED / REJECTED
    signed_by = Column(String, nullable=False)
    signed_at = Column(DateTime, default=datetime.utcnow)
