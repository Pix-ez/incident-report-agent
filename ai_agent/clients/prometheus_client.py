import requests

PROMETHEUS_URL = "http://prometheus:9090"


class PrometheusClient:

    def query(self, query: str):

        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={"query": query},
            timeout=10
        )

        response.raise_for_status()

        return self._parse(response.json())

    def _parse(self, response):

        results = (
            response
            .get("data", {})
            .get("result", [])
        )

        if not results:
            return None

        values = []

        for result in results:

            value = result.get("value")

            if not value:
                continue

            try:
                values.append(float(value[1]))
            except Exception:
                continue

        if not values:
            return None

        return {
            "current": values[-1],
            "max": max(values),
            "min": min(values)
        }