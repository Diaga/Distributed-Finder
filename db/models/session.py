from sqlalchemy import Column, String, DateTime

from db.base import Base, uuid_str

from datetime import datetime


class Session(Base):
    """Session model table"""

    __tablename__ = 'session'

    id = Column(String, default=uuid_str, primary_key=True)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f'Last login at {self.created_at.strftime("%a %b %d %H:%M:%S")}'
