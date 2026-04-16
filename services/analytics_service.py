from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension
)

PROPERTY_ID = "seu_property_id"  # Ex: "123456789"

def buscar_metricas(dias=7):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        date_ranges=[DateRange(start_date=f"{dias}daysAgo", end_date="today")],
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="screenPageViews"),
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
        ]
    )

    response = client.run_report(request)
    dados = []

    for row in response.rows:
        dados.append({
            "data_referencia": row.dimension_values[0].value,
            "sessoes": int(row.metric_values[0].value),
            "usuarios": int(row.metric_values[1].value),
            "visualizacoes": int(row.metric_values[2].value),
            "taxa_rejeicao": float(row.metric_values[3].value),
            "tempo_medio_sessao": float(row.metric_values[4].value),
        })

    print(f"{len(dados)} registros buscados do Analytics!")
    return dados