"""
Exercise 1 (core Tesla-ish): Build a “failure summary” from event logs

You often get event logs like this from test runs:

events = [
  {"ts": 1700000001, "vehicle": "V1", "test": "lane_keep", "result": "PASS", "lat_ms": 120},
  {"ts": 1700000002, "vehicle": "V1", "test": "lane_keep", "result": "FAIL", "lat_ms": 140, "reason": "camera_timeout"},
  {"ts": 1700000003, "vehicle": "V2", "test": "autopark",  "result": "FAIL", "lat_ms": 900, "reason": "planner_diverged"},
  {"ts": 1700000004, "vehicle": "V2", "test": "autopark",  "result": "FAIL", "lat_ms": 850, "reason": "planner_diverged"},
  {"ts": 1700000005, "vehicle": "V3", "test": "lane_keep", "result": "PASS", "lat_ms": 110},
]
Implement summarize_failures below
"""
from collections import defaultdict

def summarize_failures(events):
    """
    Return a dict with:
      - total: total events
      - pass: number of PASS
      - fail: number of FAIL
      - fail_by_test: dict test -> fail_count
      - top_reasons: list of (reason, count) sorted by count desc, then reason asc
    Rules:
      - If an event is FAIL but missing "reason", use "unknown"
      - Ignore events missing "result" (treat as invalid)
      - Must be deterministic (tie-break rules matter)
    """

    total_valid = 0
    pass_count = 0
    fail_count = 0

    fail_by_test = defaultdict(int)
    reason_counts = defaultdict(int)

    for event in events:
        if "result" not in event:
            continue

        total_valid += 1

        if event["result"] == "PASS":
            pass_count += 1
        elif event["result"] == "FAIL":
            fail_count += 1

            test = event.get("test", "unknown_test")
            fail_by_test[test] += 1

            reason = event.get("reason", "unknown")
            reason_counts[reason] += 1

    top_reasons = sorted(reason_counts.items(), key=lambda x: (-x[1], x[0]))

    return {
        "total": total_valid,
        "pass": pass_count,
        "fail": fail_count,
        "fail_by_test": dict(fail_by_test),
        "top_reasons": top_reasons
    }