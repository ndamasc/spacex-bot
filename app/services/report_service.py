# app/services/report_service.py
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus

import plotly.express as px
from jinja2 import Template


class ReportService:

    def _build_filename(self, status=None, year=None, month=None):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")

        parts = ["report"]

        if status:
            parts.append(status)

        if year:
            parts.append(str(year))

        if month:
            parts.append(f"m{month}")

        parts.append(ts)

        return "_".join(parts) + ".html"

    def generate(self, df, metrics, status=None, year=None, month=None):
        Path("reports").mkdir(exist_ok=True)

        if df.empty or "success" not in df.columns:
            html = f"""
            <html>
            <head>
                <meta charset="utf-8">
                <title>Spacex Launches Report</title>
                <style>
                    body {{
                        background:#0f172a;
                        color:white;
                        font-family:Arial;
                        padding:40px;
                    }}

                    .card {{
                        background:#1e293b;
                        padding:20px;
                        border-radius:14px;
                        display:inline-block;
                        margin-right:12px;
                        min-width:180px;
                    }}
                </style>
            </head>

            <body>
                <h1>Spacex Launches Report</h1>

                <div class="card">Total: {metrics["total"]}</div>
                <div class="card">Success: {metrics["success"]}</div>
                <div class="card">Failed: {metrics["failed"]}</div>
                <div class="card">Rate: {metrics["rate"]}%</div>

                <h2 style="margin-top:30px;">No data found for selected filters.</h2>
            </body>
            </html>
            """

            filename = self._build_filename(status, year, month)
            filepath = f"reports/{filename}"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)

            return filepath

        # -------- PIE --------
        pie_df = df["success"].value_counts(dropna=False).reset_index()
        pie_df.columns = ["status", "count"]

        pie_df["status"] = pie_df["status"].map(
            {
                True: "Success",
                False: "Failed"
            }
        )

        pie = px.pie(
            pie_df,
            names="status",
            values="count",
            title="Mission Status"
        )

        # -------- LINE --------
        line_df = df.copy()
        line_df["year_month"] = line_df["date_utc"].dt.to_period("M").astype(str)

        line_df = (
            line_df.groupby("year_month")
            .size()
            .reset_index(name="launches")
        )

        line = px.line(
            line_df,
            x="year_month",
            y="launches",
            markers=True,
            title="Launches Over Time"
        )

        for fig in [pie, line]:
            fig.update_layout(
                paper_bgcolor="#0f172a",
                plot_bgcolor="#0f172a",
                font_color="white"
            )

        pie_html = pie.to_html(full_html=False, include_plotlyjs="cdn")
        line_html = line.to_html(full_html=False, include_plotlyjs=False)

        html = """
        <html>
        <head>
        <meta charset="utf-8">
        <title>Spacex Launches Report</title>

        <style>
        body{
            background:#0f172a;
            color:white;
            font-family:Arial;
            padding:40px;
        }

        h1,h2{
            margin-bottom:20px;
        }

        .cards{
            display:flex;
            gap:20px;
            flex-wrap:wrap;
            margin-bottom:30px;
        }

        .card{
            background:#1e293b;
            padding:20px;
            border-radius:14px;
            min-width:180px;
        }

        .charts{
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:20px;
            margin-bottom:30px;
        }

        table{
            width:100%;
            border-collapse:collapse;
        }

        th,td{
            padding:12px;
            border-bottom:1px solid #334155;
            text-align:left;
        }

        th{
            background:#1e293b;
        }
        </style>
        </head>

        <body>

        <h1>Spacex Launches Report</h1>

        <div class="cards">
            <div class="card">Total: {{ m.total }}</div>
            <div class="card">Success: {{ m.success }}</div>
            <div class="card">Failed: {{ m.failed }}</div>
            <div class="card">Rate: {{ m.rate }}%</div>
        </div>

        <div class="charts">
            <div>{{ pie | safe }}</div>
            <div>{{ line | safe }}</div>
        </div>

        <h2>Recent Launches</h2>

        <table>
            <tr>
                <th>Name</th>
                <th>Date</th>
                <th>Success</th>
            </tr>

            {% for row in rows %}
            <tr>
                <td>{{ row["name"] }}</td>
                <td>{{ row["date_utc"] }}</td>
                <td>{{ row["success"] }}</td>
            </tr>
            {% endfor %}
        </table>

        </body>
        </html>
        """

        content = Template(html).render(
            m=metrics,
            pie=pie_html,
            line=line_html,
            rows=df.tail(20).to_dict(orient="records")
        )

        filename = self._build_filename(status, year, month)
        filepath = f"reports/{filename}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        return filepath