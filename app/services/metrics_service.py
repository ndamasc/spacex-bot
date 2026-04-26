class MetricsService:

    def build(self, df):
        if df.empty or "success" not in df.columns:
            return {
                "total": 0,
                "success": 0,
                "failed": 0,
                "rate": 0
            }

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