# scripts/publish_review.py

import argparse
import json
import os
import subprocess


def comment(pr_number, body):

    subprocess.run(
        [
            "gh",
            "pr",
            "comment",
            str(pr_number),
            "--body",
            body
        ],
        check=True
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--pr-number", required=True)
    parser.add_argument("--review-file", required=True)

    args = parser.parse_args()

    with open(args.review_file) as f:
        review = json.load(f)

    body = f"""
## 🤖 Claude AI Code Review

### Status

**{review["status"]}**

### Score

**{review["score"]}/10**

### Summary

{review["summary"]}

"""

    findings = review.get("findings", [])

    if findings:

        for finding in findings:
            body += f"""
        #### {finding.get("severity", "UNKNOWN")}: {finding.get("issue", "Code review finding")}

        **File:** `{finding.get("file", "unknown")}`  
        **Line:** `{finding.get("line", "unknown")}`

        {finding.get("explanation", "No explanation provided.")}

        **Suggested change:**

        {finding.get("suggested_fix", "No suggestion provided.")}

        ---
        """

    else:

        body += """
### Findings

No issues detected by the AI reviewer.
"""

    comment(args.pr_number, body)


if __name__ == "__main__":
    main()