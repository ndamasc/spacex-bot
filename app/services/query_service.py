import pandas as pd

from app.core.database import SessionLocal
from app.repositories.launch_repository import LaunchRepository


class QueryService:

    def get_launches(self, status=None, year=None, month=None):
        session = SessionLocal()

        try:
            repo = LaunchRepository(session)

            launches = repo.find_all(status, year, month)

            data = [
                {
                    "id": item.id,
                    "name": item.name,
                    "date_utc": item.date_utc,
                    "success": item.success,
                }
                for item in launches
            ]

            return pd.DataFrame(data)

        finally:
            session.close()