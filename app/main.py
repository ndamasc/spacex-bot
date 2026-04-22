from app.core.logger import logger
from app.services.extractor_service import ExtractorService
from app.services.transform_service import TransformService
from app.services.report_service import ReportService


def run():
    logger.info("Starting LaunchOps Bot")

    extractor = ExtractorService()
    transformer = TransformService()
    report = ReportService()

    data = extractor.collect()

    df = transformer.build_launch_dataframe(data["past"])
    kpis = transformer.generate_kpis(df)

    report.save_csv(df)

    logger.info(kpis)
    logger.info("Process finished")


if __name__ == "__main__":
    run()