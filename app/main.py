import argparse

from app.core.logger import logger
from app.core.database import Base, engine

from app.services.extractor_service import ExtractorService
from app.services.transform_service import TransformService
from app.services.report_service import ReportService
from app.services.filter_service import FilterService
from app.services.db_service import DBService


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--status", choices=["success", "failed"])
    parser.add_argument("--year", type=int)
    parser.add_argument("--month", type=int)

    return parser.parse_args()


def run():
    args = parse_args()

    Base.metadata.create_all(bind=engine)

    logger.info("Starting Spacex Bot")

    extractor = ExtractorService()
    transformer = TransformService()
    reporter = ReportService()
    filters = FilterService()
    db = DBService()

    data = extractor.collect()

    df = transformer.build_launch_dataframe(data["past"])

    db.save_launches(df.to_dict(orient="records"))

    filtered_df = filters.apply(
        df,
        status=args.status,
        year=args.year,
        month=args.month
    )

    kpis = transformer.generate_kpis(filtered_df)

    reporter.save_csv(filtered_df)

    logger.info(kpis)
    logger.info(f"Rows after filters: {len(filtered_df)}")
    logger.info("Process finished")


if __name__ == "__main__":
    run()