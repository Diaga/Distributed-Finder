from db.db import DB
from db.models.file import File


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
            DB().session.add(file_db)

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
    def get_files_from_current_directories(current_directory):
        """Return all files with in the current directory
        :param current_directory: Directory model object
        specifying current directory
        """
        return DB().session.query(File).filter_by(
            directory_id=current_directory.id
        ).all()
