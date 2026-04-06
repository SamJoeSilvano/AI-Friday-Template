from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    requirement_version_id = Column(Integer, nullable=False)
    reviewer_type = Column(String, nullable=False)  # AI or HUMAN
    comments = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
