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
    def delete_sector(sector, commit=True):
        """Deletes an existing sector record from the database
        :param sector: Sector object model to be deleted
        :param commit: Specifies whether to commit to database
        """
        DB().session.delete(sector)
        if commit:
            DB().session.commit()
