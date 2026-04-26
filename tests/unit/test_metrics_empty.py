import pandas as pd
from app.services.metrics_service import MetricsService


def test_should_return_zero_when_empty():
    df = pd.DataFrame()

    result = MetricsService().build(df)

    assert result["total"] == 0
    assert result["rate"] == 0