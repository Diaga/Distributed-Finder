import threading

from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SQLSession

from db.base import Base

from .models.directory import Directory # noqa
from .models.file import File # noqa
from .models.session import Session # noqa
from .models.sector import Sector  # noqa


CONNECTION_POOL = {}


class DB:
    _db = None
    _engine = None
    session = None

    def connect(self, db_path):
        """Start a connection to database
        :param db_path: Path to sqlite database
        """
        self._engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self._engine)

        self.session = SQLSession(self._engine)
        self.session.expire_on_commit = False

    def __new__(cls):
        """Singleton constructor for DB connection"""
        if threading.current_thread() is threading.main_thread():
            if cls._db is None:
                cls._db = super(DB, cls).__new__(cls)

            return cls._db
        else:
            db = CONNECTION_POOL.get(threading.current_thread().name, None)
            if db is None:
                db = super(DB, cls).__new__(cls)
                db.connect('finder.db')
            CONNECTION_POOL[threading.current_thread().name] = db

            return db
