from db.db import DB
from db.models.directory import Directory
import re


class DirectoryDao:
    """Data access object for Directory model"""

    @staticmethod
    def create_directory(directory, commit=True):
        """Creates a new directory record in database
        :param directory: Directory model object to be inserted
        :param commit: Specifies whether to commit to database
        """
        directory_db = DB().session.add(directory)
        if commit:
            DB().session.commit()

        return directory_db

    @staticmethod
    def delete_directory(directory, commit=True):
        """Deletes an existing directory record from the database
        :param directory: Directory model object to be deleted
        :param commit: Specifies whether to commit to database
        """
        DB().session.delete(directory)
        if commit:
            DB().session.commit()

    @staticmethod
    def _create_root_directory():
        """Creates a root directory"""
        directory_db = Directory(name='/', is_root=True)
        DB().session.add(directory_db)
        DB().session.commit()
        return directory_db

    @staticmethod
    def get_root_directory():
        """Returns root directory, creates one if it does not exist"""
        root_db = DB().session.query(Directory).filter_by(is_root=True).first()
        if root_db is None:
            root_db = DirectoryDao._create_root_directory()

        return root_db

    @staticmethod
    def get_directories_from_current_directory(current_directory):
        """Returns all directories inside a current directory
        :param current_directory: Directory model object
         specifying current directory
        """
        return DB().session.query(Directory).filter_by(
            directory_id=current_directory.id
        ).all()

    @staticmethod
    def get_directory_from_current_directory(current_directory,
                                             directory_name):
        """Returns directory model object from current directory
         with directory_name
        :param current_directory: Current directory to search for
        :param directory_name: Directory name to search for
        """
        return DB().session.query(Directory).filter_by(
            directory_id=current_directory.id, name=directory_name
        ).first()

    @staticmethod
    def is_valid_dirname(dirname):
        """Returns true if directory name does not start
        with a special char and does not contain . \\ /
        :param dirname: String specifying name of the
        directory to be validated
        """
        return not (bool(re.search(
            r'^[@!#$%^&+-=\.\/\\\*]|([\\\/\.]+)', dirname)))

    @staticmethod
    def is_unique_direname(dirname, current_directory):
        """Returns true if directory is unique within the
        directory
        :param current_directory: Directory model object
         specifying current directory
        :param filename: String specifying filename to be
        validated
        """
        directories = DirectoryDao.get_directories_from_current_directory(
            current_directory)

        for directory in directories:
            if directory.name == dirname:
                return False
        return True
