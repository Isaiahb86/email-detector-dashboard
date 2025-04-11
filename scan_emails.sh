#!/bin/bash

echo "Scanning emails..."
> results.csv

for file in emails/*.txt; do
    if yara yara_rules/email_rules.yar "$file" > /dev/null 2>&1; then
        echo "$(basename $file),Malicious" >> results.csv
    else
        echo "$(basename $file),Clean" >> results.csv
    fi
done

echo "Scan complete. Results saved to results.csv."
