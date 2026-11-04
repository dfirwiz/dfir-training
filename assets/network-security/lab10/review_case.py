"""Offline checks for this course's synthetic JSON format, not a TheHive client."""
from pathlib import Path
import json
import sys


def review(case):
    issues = []
    if not case.get("owner", "").strip():
        issues.append("case: owner missing")
    evidence_ids = {item["id"] for item in case.get("evidence", [])}
    for task in case.get("tasks", []):
        if not task.get("required", False):
            continue
        task_id = task["id"]
        if task.get("status") != "completed":
            issues.append(f"{task_id}: not completed")
        if not task.get("result", "").strip():
            issues.append(f"{task_id}: result missing")
        refs = set(task.get("evidence_refs", []))
        if not refs or not refs.issubset(evidence_ids):
            issues.append(f"{task_id}: evidence missing or unknown")
    for observable in case.get("observables", []):
        refs = set(observable.get("evidence_refs", []))
        if not refs or not refs.issubset(evidence_ids):
            issues.append(f"{observable['id']}: origin missing or unknown")
    if not case.get("summary", "").strip():
        issues.append("case: summary missing")
    return issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python review_case.py case-start.json")
        return 2
    try:
        case = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        issues = review(case)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print("INPUT ERROR:", type(error).__name__)
        return 2
    for issue in issues:
        print(issue)
    print("REVIEW BLOCKED" if issues else "REVIEW READY (record checks only)")
    return 2 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
