from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["service", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Request latency",
    ["service", "endpoint"]
)

PAYMENT_FAILURES = Counter(
    "payment_failures_total",
    "Payment failures"
)