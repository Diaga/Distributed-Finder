from db.db import DB
from db.models.session import Session


class SessionDao:
    """Data access object for Session model"""

    @staticmethod
    def create_session(session, commit=True):
        """Creates a new session record in database
        :param session: Session model object to be inserted
        :param commit: Specifies whether to commit to database
        """
        session_db = DB().session.add(session)
        if commit:
            DB().session.commit()

        return session_db

    @staticmethod
    def get_last_session():
        """Returns the latest session from database"""
        return DB().session.query(Session).order_by(
            Session.created_at.desc()
        ).first()
