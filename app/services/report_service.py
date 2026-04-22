from pathlib import Path


class ReportService:

    def save_csv(self, df):
        Path("reports").mkdir(exist_ok=True)
        df.to_csv("reports/launches.csv", index=False)