from collections import Counter
from statistics import mean


class EvidenceBuilder:

    def build(self, investigation):

        return {
            "metrics": self.build_metrics(
                investigation.metrics_data
            ),
            "logs": self.build_logs(
                investigation.logs_data
            ),
            "historical_events": self.build_history(
                investigation.historical_events
            )
        }

    ##################################################
    # METRICS
    ##################################################

    def build_metrics(self, metrics):

        if not metrics:
            return {}

        summary = {}

        for metric_name, metric in metrics.items():

            if metric is None:
                continue

            summary[metric_name] = metric

        return summary
    ##################################################
    # LOGS
    ##################################################

    def build_logs(self, logs):

        if not logs:
            return {}

        severity_counter = Counter()
        service_counter = Counter()
        reason_counter = Counter()
        message_counter = Counter()

        recent_errors = []

        for log in logs:

            if not isinstance(log, dict):
                continue

            severity = log.get("severity", "unknown")

            service = log.get("service", "unknown")

            reason = log.get("reason", "unknown")

            message = log.get("message", "")

            severity_counter[severity] += 1
            service_counter[service] += 1
            reason_counter[reason] += 1
            message_counter[message] += 1

            if (
                severity.lower()
                in ["critical", "error", "warning"]
            ):

                if len(recent_errors) < 5:

                    recent_errors.append({

                        "service": service,

                        "severity": severity,

                        "reason": reason,

                        "message": message
                    })

        return {

            "total_logs": len(logs),

            "severity_distribution":
                dict(severity_counter),

            "affected_services":
                dict(service_counter),

            "top_failure_reasons":
                dict(
                    reason_counter.most_common(5)
                ),

            "top_messages":
                dict(
                    message_counter.most_common(5)
                ),

            "recent_errors":
                recent_errors
        }

    ##################################################
    # HISTORY
    ##################################################

    def build_history(self, events):

        if not events:
            return {}

        event_counter = Counter()
        severity_counter = Counter()

        for event in events:

            if not isinstance(event, dict):
                continue

            event_counter[
                event.get(
                    "event_type",
                    "unknown"
                )
            ] += 1

            severity_counter[
                event.get(
                    "severity",
                    "unknown"
                )
            ] += 1

        return {

            "total_events": len(events),

            "event_distribution":
                dict(event_counter),

            "severity_distribution":
                dict(severity_counter),

            "recent_events":
                events[-5:]
        }