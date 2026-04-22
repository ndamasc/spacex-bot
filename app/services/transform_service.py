import pandas as pd


class TransformService:

    def build_launch_dataframe(self, launches):
        rows = []

        for item in launches:
            rows.append({
                "name": item.get("name"),
                "date_utc": item.get("date_utc"),
                "success": item.get("success")
            })

        return pd.DataFrame(rows)

    def generate_kpis(self, df):
        total = len(df)
        success = len(df[df["success"] == True])

        return {
            "total_launches": total,
            "success_rate": round((success / total) * 100, 2) if total else 0
        }