import pandas as pd
from sqlalchemy import create_engine
from app.core.config import DB_URL

engine = create_engine(DB_URL)


class QueryService:

    def get_launches(self, status=None, year=None, month=None):
        df = pd.read_sql("SELECT * FROM launches", engine)

        df["date_utc"] = pd.to_datetime(df["date_utc"], utc=True).dt.tz_localize(None)

        if status == "success":
            df = df[df["success"] == True]

        elif status == "failed":
            df = df[df["success"] == False]

        if year:
            df = df[df["date_utc"].dt.year == year]

        if month:
            df = df[df["date_utc"].dt.month == month]

        return df