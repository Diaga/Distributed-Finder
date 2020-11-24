from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base, uuid_str

from datetime import datetime


class Directory(Base):
    """Directory model table"""

    __tablename__ = 'directory'

    id = Column(String, default=uuid_str, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    is_root = Column(Boolean, default=False)

    directory_id = Column(String, ForeignKey('directory.id',
                                             ondelete='CASCADE'))
    directory = relationship('Directory',
                             foreign_keys='Directory.directory_id')
    files = relationship('File', backref='directory')

    def __repr__(self):
        return self.name
