class MetricsService:

    def build(self, df):
        total = len(df)

        success = len(df[df["success"] == True])

        failed = len(df[df["success"] == False])

        rate = round((success / total) * 100, 2) if total else 0

        return {
            "total": total,
            "success": success,
            "failed": failed,
            "rate": rate
        }