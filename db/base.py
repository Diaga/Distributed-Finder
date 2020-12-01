from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

TOTAL_SIZE = 200
SECTOR_SIZE = 10

Base = declarative_base()


def uuid_str():
    return str(uuid4())
