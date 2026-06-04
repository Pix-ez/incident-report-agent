import requests

PROMETHEUS_URL = "http://prometheus:9090"


class PrometheusClient:

    def query(self, query: str):

        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={
                "query": query
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()