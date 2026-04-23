import pandas as pd


class FilterService:

    def apply(self, df, status=None, year=None, month=None):
        result = df.copy()

        if status == "success":
            result = result[result["success"] == True]

        elif status == "failed":
            result = result[result["success"] == False]

        if year:
            result["date_utc"] = pd.to_datetime(result["date_utc"])
            result = result[result["date_utc"].dt.year == year]

        if month:
            result["date_utc"] = pd.to_datetime(result["date_utc"])
            result = result[result["date_utc"].dt.month == month]

        return result