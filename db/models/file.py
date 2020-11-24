from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base, uuid_str

from datetime import datetime


class File(Base):
    """File model table"""

    __tablename__ = 'file'

    id = Column(String, default=uuid_str, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    directory_id = Column(String, ForeignKey('directory.id'))

    sectors = relationship('Sector', backref='file')

    def __repr__(self):
        return self.name
