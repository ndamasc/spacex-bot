from sqlalchemy import extract
from app.models.launch import Launch


class LaunchRepository:

    def __init__(self, session):
        self.session = session

    def find_all(self, status=None, year=None, month=None):
        query = self.session.query(Launch)

        if status == "success":
            query = query.filter(Launch.success.is_(True))

        elif status == "failed":
            query = query.filter(Launch.success.is_(False))

        if year:
            query = query.filter(
                extract("year", Launch.date_utc) == year
            )

        if month:
            query = query.filter(
                extract("month", Launch.date_utc) == month
            )

        return query.order_by(Launch.date_utc.desc()).all()