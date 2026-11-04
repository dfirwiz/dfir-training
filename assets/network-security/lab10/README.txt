Independent synthetic case-record exercise. All evidence is fictional.

Place case-start.json, case-reviewed.json and review_case.py in one folder.
Python 3 is required; no external packages, network access or TheHive are used.

python review_case.py case-start.json
Expected exit code: 2. T2 is unfinished and lacks result/evidence; summary is empty.

python review_case.py case-reviewed.json
Expected exit code: 0. Output: REVIEW READY (record checks only).

The script only reads the selected file. It does not change the input, close a
case, contact a service, resolve a domain or execute any response action.
This is not a TheHive API payload, schema validator or real investigation.
Passing the record checks does not validate evidence, prove an absence of
compromise or establish that recovery is complete.
