from sqlalchemy import Column, String, LargeBinary, Integer, ForeignKey

from db.base import Base, uuid_str


class Sector(Base):
    """Sector model table"""

    __tablename__ = 'sector'

    id = Column(String, default=uuid_str, primary_key=True)
    data = Column(LargeBinary)
    order = Column(Integer)

    file_id = Column(String, ForeignKey('file.id'))

    def __repr__(self):
        return f'Sector at {self.id} memory address, order is {self.order}'
