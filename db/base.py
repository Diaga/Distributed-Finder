from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4


Base = declarative_base()


def uuid_str():
    return str(uuid4())


def total_size():
    return 200


def sector_size():
    return 10
