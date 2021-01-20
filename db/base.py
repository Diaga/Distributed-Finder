from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from threading import Lock

TOTAL_SIZE = 1000
SECTOR_SIZE = 10

Base = declarative_base()


def uuid_str():
    return str(uuid4())


MONITOR_MUTEX = Lock()
MUTEX_POOL = []


class Monitor:

    def __init__(self, obj_id, mode='w'):
        self.obj_id = obj_id
        self.mode = mode

        self.opened_file_metadata = None

    def acquire_lock(self):

        opened_file_metadata = next(
            (mutex_dict for mutex_dict in MUTEX_POOL if
             mutex_dict['id'] == self.obj_id),
            None
        )
        if opened_file_metadata is None:
            opened_file_metadata = {'id': self.obj_id, 'mutex': Lock(),
                                    'readers_count': 0}
            MUTEX_POOL.append(opened_file_metadata)

        self.opened_file_metadata = opened_file_metadata

        # Please visit: https://www.tutorialspoint.com/readers-writers-problem
        # for implementation details

        if self.mode == 'r':
            # Reader's Process
            MONITOR_MUTEX.acquire()

            self.opened_file_metadata['readers_count'] += 1
            if self.opened_file_metadata['readers_count'] == 1:
                self.opened_file_metadata['mutex'].acquire()

            MONITOR_MUTEX.release()

        elif self.mode == 'w':
            # Writer's Process
            self.opened_file_metadata['mutex'].acquire()

    def release_lock(self):
        if self.mode == 'r':
            MONITOR_MUTEX.acquire()
            self.opened_file_metadata['readers_count'] -= 1
            if self.opened_file_metadata['readers_count'] == 0:
                self.opened_file_metadata['mutex'].release()

            MONITOR_MUTEX.release()
        elif self.mode == 'w':
            self.opened_file_metadata['mutex'].release()

    def __enter__(self):
        self.acquire_lock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release_lock()
