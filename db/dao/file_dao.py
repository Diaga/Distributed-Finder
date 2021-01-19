from db.db import DB
from db.dao.directory_dao import DirectoryDao
from db.models.directory import Directory
from db.base import SECTOR_SIZE
from db.dao.sector_dao import SectorDao
from db.models.file import File
from math import ceil
import re
from threading import Lock


class FileDao:
    """Data access object for File model"""
    POOL = []

    @staticmethod
    def write_lock_of_file(file):
        accessed_file = next(
            (item for item in FileDao.POOL if item['id'] == file),
            None
        )
        if (accessed_file is None):
            mutex = Lock()
            FileDao.POOL.append({
                'id': file,
                'mutex': mutex
            })
            return mutex
        return accessed_file['mutex']

    @staticmethod
    def write_unlock_of_file(file):
        accessed_file = next(
            item for item in FileDao.POOL if item['id'] == file
        )
        mutex: Lock = accessed_file['mutex']
        FileDao.POOL.remove(accessed_file)
        return mutex

    @staticmethod
    def read_lock_of_file(file):
        accessed_file = next(
            (item for item in FileDao.POOL if item['id'] == file), None)
        if (accessed_file is None):
            return None
        return accessed_file['mutex']

    @staticmethod
    def create_file(file, commit=True):
        """Creates a new file record in the database
        :param file: File model object to be inserted
        :param commit: Specifies whether to commit to database
        """
        file_db = DB().session.add(file)
        if commit:
            DB().session.commit()

        return file_db

    @staticmethod
    def insert_data_in_file(file, data, order=None):
        """inserts the data in the available sectors
        :param file: File model object whose data is
        to be stored
        :param data: The data to insert
        :param order: The preceding order number
        """
        FileDao.write_lock_of_file(file).acquire()
        divs = []
        for cap in range(0, len(data), SECTOR_SIZE):
            divs.append(data[cap: cap + SECTOR_SIZE])
        if order is None:
            order = FileDao.get_highest_order_of_sectors(file)
        for div in divs:
            if SectorDao.is_memory_full():
                raise MemoryError(
                    'Memory is full! ' +
                    'All available sectors used up!')

            order += 1
            sector = SectorDao.get_first_unused_sector()
            SectorDao.insert_sector_data(
                sector, data=div, order=order, file_id=file.id)
        FileDao.write_unlock_of_file(file).release()
        return order

    @staticmethod
    def remove_data_in_file(file, commit=True):
        """Removes the data in the sectors of the file
        :param file: File model object whose data is
        to be removed
        :param commit: Specifies whether to commit
        to database
        """
        FileDao.write_lock_of_file(file).acquire()
        for sector in file.sectors:
            sector.data = None
            sector.order = 0
            sector.file_id = None
        if commit:
            DB().session.commit()
        FileDao.write_unlock_of_file(file).release()

    @staticmethod
    def delete_file(file, commit=True):
        """Deletes an existing file record from the database
        :param file: File model object to be deleted
        :param commit: Specifies whether to commit to database
        """

        FileDao.remove_data_in_file(file)
        DB().session.delete(file)
        if commit:
            DB().session.commit()

    @staticmethod
    def get_file_from_current_directory(current_directory, filename):
        return DB().session.query(File).filter_by(
            directory_id=current_directory.id,
            name=filename
        ).first()

    @staticmethod
    def get_files_from_current_directory(current_directory):
        """Return all files with in the current directory
        :param current_directory: Directory model object
        specifying current directory
        """
        return DB().session.query(File).filter_by(
            directory_id=current_directory.id
        ).all()

    @staticmethod
    def is_unique_filename(filename, current_directory):
        """Returns true if file is unique within the
        directory
        :param current_directory: Directory model object
        specifying current directory
        :param filename: String specifying filename to be
        validated
        """
        directory_files = FileDao.get_files_from_current_directory(
            current_directory)

        for file in directory_files:
            if file.name == filename:
                return False
        return True

    @staticmethod
    def is_valid_filename(filename):
        """Returns true if filename does not start with
        a special char and does not contain \\ /
        :param filename: String specifying filename
        to be validated
        """
        return not (bool(re.search(
            r'^[@!#$%^&+-=\.\/\\\*]|([\\\/]+)', filename)))

    @staticmethod
    def get_all_files():
        return DB().session.query(File).all()

    @staticmethod
    def get_path(obj):
        isFile = isinstance(obj, File)
        if isFile:
            current = DB().session.query(Directory).get(obj.directory_id)
        else:
            current = obj.context.current_directory

        path = str(current)
        root = DirectoryDao.get_root_directory()
        restore = current
        while (current != root):
            parent = current.directory
            str_parent = str(parent)
            path = str_parent+'/'+path
            current = parent
        current = restore
        path = path+'/' + (obj.name if isFile else '')
        return path

    @staticmethod
    def get_highest_order_of_sectors(file):
        if file.is_empty:
            return 0
        sector_orders = map(lambda sector: sector.order, file.sectors)
        return max(sector_orders)

    @staticmethod
    def get_file_size(file):
        if file.is_empty:
            return 0
        sector_orders = map(lambda sector: len(sector.data), file.sectors)
        return sum(sector_orders)

    @staticmethod
    def read_from_file(file, index=0, size=None):
        mutex: Lock = FileDao.read_lock_of_file(file)
        if mutex is not None:
            mutex.acquire()
        if file.is_empty:
            raise ValueError('File is empty! No contents to show')
        file_size = FileDao.get_file_size(file)
        if size is None:
            size = file_size

        if index == 0:
            content = ''
            file_sectors = file.sectors
            file_sectors.sort(key=lambda sector: sector.order)
            content = ''
            for sector in file_sectors:
                content += sector.data
        else:
            if (index >= file_size):
                raise ValueError(
                    'Index larger than content in file!')
            # The sector from which data is to be read
            start_read_sector_order = ceil((index + 1) / SECTOR_SIZE)
            start_read_sector = [
                sector for sector in
                file.sectors if sector.order == start_read_sector_order][0]

            # The remaining sectors to be read
            end_sectors = [
                sector for sector in file.sectors
                if sector.order > start_read_sector_order
            ]

            # Sorting the remaining sectors by order
            end_sectors.sort(key=lambda sector: sector.order)

            # Read content of the sector from the specified index
            start_read_sector_data = start_read_sector.data
            start_index = index % SECTOR_SIZE
            content = start_read_sector_data[start_index:]

            # Read the content till the size specified
            count = 0
            while count < len(end_sectors):
                content += end_sectors[count].data
                count += 1
        if mutex is not None:
            mutex.release()
        return content[:size]
