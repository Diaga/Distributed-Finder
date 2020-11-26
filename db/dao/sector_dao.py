from db.models.sector import Sector
from db.db import DB


class SectorDao:
    """Data access object for Sector model"""

    @staticmethod
    def create_sector(sector, commit=True):
        """Creates a new sector record in the database
        :param sector: Sector object model to be inserted
        :param commit: Specifies whether to commit to database
        """
        sector_db = DB().session.add(sector)
        if commit:
            DB().session.commit()

        return sector_db

    @staticmethod
    def get_total_sectors_count():
        """ Returns the total sectors created in the
        daatabase at the moment.
        Used to increment order.
        """
        return DB().session.query(Sector).count()

    @staticmethod
    def create_sectors_division(sector_size, total_size):
        """Creates all the possible sector records in the
        database
        :param sector_size: Specifies the Sector size
        :param total_size: Specifies the total disk size
        """
        total_sectors = sector_size // total_size
        for sector in range(total_sectors):
            SectorDao.create_sector(Sector(
                order=SectorDao.get_total_sectors_count()
            ))

    @staticmethod
    def get_first_unused_sector():
        """ Returns the first available sector
        """
        return DB().session.query(Sector).filter_by(
            is_used=False
        ).first()

    @staticmethod
    def insert_sector_data(sector, data, is_used, file_id):
        """ Inserts the values in an already created sector
        record
        :param sector: Sector object model to be manipulated
        :param data: Specifies the data to be inserted
        :param is_used: Specifies whether sector is empty
        :param file_id: Specifies the id of the file linked
        with this sector
        """
        sector.data = data
        sector.is_used = is_used
        sector.file_id = file_id
        DB().session.commit()

    @staticmethod
    def delete_sector(sector, commit=True):
        """Deletes an existing sector record from the database
        :param sector: Sector object model to be deleted
        :param commit: Specifies whether to commit to database
        """
        DB().session.delete(sector)
        if commit:
            DB().session.commit()

    @staticmethod
    def get_sectors_linked_to_file(file):
        """Returns all the sectors where the file data
        has been saved
        :param file: file object model
        """
        return DB().session.query(Sector).filter_by(
            file_id=file.id
        ).all()

    @staticmethod
    def get_unused_sectors_count():
        """
        Returns the total count of available sectors
        """
        return len(DB().session.query(Sector).filter_by(
            is_used=False
        ).all())

    @staticmethod
    def is_memory_full():
        """
        Returns true if no more sectors
        are available
        """
        if SectorDao.get_unused_sectors_count() == 0:
            return True
        return False
