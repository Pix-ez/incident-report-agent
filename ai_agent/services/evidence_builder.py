def build_analysis_context(
    investigation
):

    metrics = investigation.metrics_data
    logs = investigation.logs_data
    history = investigation.historical_events


    #TODO for now we are just passing last 50 logs it can sometimes hide critical information
    # we can improve this.
    context = {
        "metrics": metrics,
        "history": history,
        "log_count": len(logs),
        "critical_logs": logs[:50]
    }

    return context