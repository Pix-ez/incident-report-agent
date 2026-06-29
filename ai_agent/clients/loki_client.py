from datetime import datetime, timedelta
import time
import json
import requests

LOKI_URL = "http://loki:3100"

MAX_LOGS = 50


class LokiClient:

    def query(self, query: str):

        end = int(time.time() * 1e9)

        start = int(
            (
                datetime.utcnow() - timedelta(minutes=30)
            ).timestamp()
            * 1e9
        )

        response = requests.get(
            f"{LOKI_URL}/loki/api/v1/query_range",
            params={
                "query": query,
                "start": start,
                "end": end,
                "limit": MAX_LOGS
            },
            timeout=10
        )

        response.raise_for_status()

        return self._parse_logs(response.json())

    def _parse_logs(self, response):

        parsed_logs = []

        streams = response.get("data", {}).get("result", [])

        for stream in streams:

            labels = stream.get("stream", {})

            service = (
                labels.get("service")
                or labels.get("container")
                or labels.get("compose_service")
                or "unknown"
            )

            for timestamp, log_line in stream.get("values", []):

                log = {
                    "timestamp": datetime.fromtimestamp(
                        int(timestamp) / 1e9
                    ).isoformat(),
                    "service": service,
                    "severity": "info",
                    "message": "",
                    "reason": None
                }

                # Docker JSON log format
                try:

                    docker_log = json.loads(log_line)

                    message = docker_log.get("log", "").strip()

                except Exception:

                    message = log_line.strip()

                # Try parsing your application's JSON logs
                try:

                    app_log = json.loads(message)

                    log["severity"] = app_log.get(
                        "level",
                        app_log.get("severity", "info")
                    )

                    log["message"] = app_log.get(
                        "message",
                        message
                    )

                    log["reason"] = app_log.get("reason")

                    if "service" in app_log:
                        log["service"] = app_log["service"]

                except Exception:

                    log["message"] = message

                # Prevent extremely long log messages
                log["message"] = log["message"][:300]

                parsed_logs.append(log)

                if len(parsed_logs) >= MAX_LOGS:
                    return parsed_logs

        return parsed_logs