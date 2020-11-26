from db.db import DB
from db.models.file import File
import re


class FileDao:
    """Data access object for File model"""

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
    def delete_file(file, commit=True):
        """Deletes an existing file record from the database
        :param file: File model object to be deleted
        :param commit: Specifies whether to commit to database
        """
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
    def get_highest_order_of_sectors(file):
        if file.is_empty:
            return 0
        sector_orders = map(lambda sector: sector.order, file.sectors)
        return max(sector_orders)
