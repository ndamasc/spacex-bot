import pandas as pd
from app.services.metrics_service import MetricsService


def test_should_calculate_metrics():
    df = pd.DataFrame(
        [
            {"success": True},
            {"success": False},
            {"success": True},
        ]
    )

    result = MetricsService().build(df)

    assert result["total"] == 3
    assert result["success"] == 2
    assert result["failed"] == 1
    assert result["rate"] == 66.67