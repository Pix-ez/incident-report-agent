from datetime import datetime, timedelta
import time
import requests

LOKI_URL = "http://loki:3100"


class LokiClient:

    def query(self, query: str):

        end = int(time.time() * 1e9)

        start = int(
            (
                datetime.utcnow()
                - timedelta(minutes=30)
            ).timestamp()
            * 1e9
        )

        response = requests.get(
            f"{LOKI_URL}/loki/api/v1/query_range",
            params={
                "query": query,
                "start": start,
                "end": end,
                "limit": 100
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()