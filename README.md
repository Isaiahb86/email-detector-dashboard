# Malicious Email Detector Dashboard

This project is a Python-based dashboard that automates the detection of malicious emails. It uses YARA rules to scan email files for suspicious content and displays the results in an interactive web dashboard built with Dash.

## Features

- **Email Generation**: A script (`generate_emails.py`) creates fake emails—some containing malicious content.
- **Email Scanning**: A Bash script (`scan_emails.sh`) uses custom YARA rules to scan emails for malicious patterns.
- **Interactive Dashboard**: A Dash application (`app.py`) displays scan results in a table that auto-refreshes every 10 seconds.
