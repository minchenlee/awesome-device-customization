"""Fill stars, last push date, and license for every project from the GitHub API.

Needs the `gh` CLI, logged in. Read-only: it only calls `gh api repos/<repo>`.
"""

import json
import subprocess
import time
from datetime import date, timedelta

import devices

STALE_DAYS = 3 * 365


def repo_facts(repo):
    raw = subprocess.run(
        ["gh", "api", f"repos/{repo}", "--jq",
         "{stars: .stargazers_count, pushed: .pushed_at, license: (.license.spdx_id // \"NOASSERTION\"),"
         " archived: .archived, full_name: .full_name}"],
        check=True, capture_output=True, text=True,
    ).stdout
    return json.loads(raw)


def main():
    data = devices.load()
    cutoff = (date.today() - timedelta(days=STALE_DAYS)).isoformat()
    for _, _, proj in devices.projects(data):
        facts = repo_facts(proj["repo"])
        proj["repo"] = facts["full_name"]
        proj["stars"] = facts["stars"]
        proj["pushed"] = facts["pushed"][:10]
        proj["license"] = facts["license"]
        flags = [f for f in proj["flags"] if f != "archived"]
        if facts["archived"] or proj["pushed"] < cutoff:
            flags.append("archived")
        proj["flags"] = flags
        time.sleep(0.3)
    devices.dump(data)
    (devices.ROOT / "data" / "refreshed.txt").write_text(date.today().isoformat() + "\n")


if __name__ == "__main__":
    main()
