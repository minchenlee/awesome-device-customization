"""Check data/devices.yaml.

- Every project has all fields, and flags are known.
- Every project URL answers HTTP 200.
- Stars, last push date, and license match the GitHub API (`gh api`).
  Stars may drift by 5% between refresh and check.

Exit code 0 when all checks pass, 1 otherwise.
"""

import sys
import time
import urllib.request

import devices
from build import TEXT
from refresh import repo_facts


def url_status(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "awesome-device-customization-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status
    except urllib.error.HTTPError as err:
        return err.code
    except OSError as err:
        return str(err)


def main():
    data = devices.load()
    errors = []
    seen = set()
    count = 0
    for cat, dev, p in devices.projects(data):
        count += 1
        where = f"{cat['id']} / {dev['model']} / {p.get('name')}"
        missing = [k for k in devices.PROJECT_FIELDS if p.get(k) in (None, "")]
        if missing:
            errors.append(f"{where}: missing {missing}")
            continue
        unknown = [f for f in p["flags"] if f not in devices.FLAGS]
        if unknown:
            errors.append(f"{where}: unknown flags {unknown}")
        if p["repo"].lower() in seen:
            errors.append(f"{where}: duplicate repo {p['repo']}")
        seen.add(p["repo"].lower())
        status = url_status(f"https://github.com/{p['repo']}")
        if status != 200:
            errors.append(f"{where}: URL status {status}")
        facts = repo_facts(p["repo"])
        if facts["pushed"][:10] != p["pushed"]:
            errors.append(f"{where}: pushed {p['pushed']} != API {facts['pushed'][:10]}")
        if abs(facts["stars"] - p["stars"]) > max(5, facts["stars"] * 0.05):
            errors.append(f"{where}: stars {p['stars']} != API {facts['stars']}")
        if facts["license"] != p["license"]:
            errors.append(f"{where}: license {p['license']} != API {facts['license']}")
        time.sleep(0.3)
    for repo, _ in TEXT["en"]["more"]:
        status = url_status(f"https://github.com/{repo}")
        if status != 200:
            errors.append(f"further reading {repo}: URL status {status}")
    for e in errors:
        print("FAIL", e)
    print(f"{count} projects checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
