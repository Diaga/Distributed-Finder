from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4


Base = declarative_base()


def uuid_str():
    return str(uuid4())
