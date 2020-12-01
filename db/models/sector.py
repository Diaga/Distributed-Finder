from sqlalchemy import Column, String, Integer, ForeignKey

from db.base import Base, uuid_str


class Sector(Base):
    """Sector model table"""

    __tablename__ = 'sector'

    id = Column(String, default=uuid_str, primary_key=True)
    data = Column(String)
    order = Column(Integer)
    file_id = Column(String, ForeignKey('file.id'))

    def __repr__(self):
        return f'sector:{self.id}'
