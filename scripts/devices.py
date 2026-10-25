"""Read and write data/devices.yaml with the standard library only.

The file uses a small YAML subset: nested mappings and lists of mappings,
plain or double-quoted scalars, and inline lists like [a, b].
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "devices.yaml"

FLAGS = {
    "mains": ("⚡", "Mains voltage inside the device", "裝置內有市電"),
    "opens": ("🔧", "Requires opening the device or soldering", "需要拆機或焊接"),
    "warranty": ("🛡️", "Likely voids the warranty", "可能失去保固"),
    "archived": ("📦", "Archived or not pushed for over 3 years", "已封存或超過 3 年未更新"),
    "review": ("⚠️", "Unlocks the device; read the project page and local law first", "會解鎖裝置；請先讀專案頁並確認當地法律"),
}

PROJECT_FIELDS = ["name", "repo", "summary", "summary_zh", "flags", "stars", "pushed", "license"]


def _scalar(text):
    text = text.strip()
    if text.startswith('"'):
        return json.loads(text)
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        return [_scalar(p) for p in inner.split(",")] if inner else []
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    return text


def _parse(lines, i, indent):
    """Parse the block starting at lines[i] with the given indent."""
    if lines[i][1].startswith("- "):
        result = []
        while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
            # A list item is a mapping whose first key sits after "- ".
            first = lines[i][1][2:]
            lines[i] = (indent + 2, first)
            item, i = _parse(lines, i, indent + 2)
            result.append(item)
        return result, i
    result = {}
    while i < len(lines) and lines[i][0] == indent and not lines[i][1].startswith("- "):
        key, _, rest = lines[i][1].partition(":")
        i += 1
        if rest.strip():
            result[key] = _scalar(rest)
        else:
            result[key], i = _parse(lines, i, lines[i][0])
    return result, i


def load(path=DATA):
    lines = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        lines.append((len(raw) - len(raw.lstrip(" ")), raw.strip()))
    data, _ = _parse(lines, 0, 0)
    return data


def _dump_scalar(value):
    if isinstance(value, list):
        return "[" + ", ".join(value) + "]"
    if isinstance(value, int):
        return str(value)
    text = str(value)
    if re.fullmatch(r"[A-Za-z0-9][\w./ -]*", text) and not text.endswith(" "):
        return text
    return json.dumps(text, ensure_ascii=False)


def dump(data, path=DATA):
    out = ["# Generated layout; edit values by hand or with scripts/refresh.py.", "categories:"]
    for cat in data["categories"]:
        out.append(f"  - id: {cat['id']}")
        for key in ("title", "title_zh"):
            out.append(f"    {key}: {_dump_scalar(cat[key])}")
        out.append("    devices:")
        for dev in cat["devices"]:
            out.append(f"      - model: {_dump_scalar(dev['model'])}")
            out.append("        projects:")
            for proj in dev["projects"]:
                first = True
                for key in PROJECT_FIELDS:
                    prefix = "          - " if first else "            "
                    out.append(f"{prefix}{key}: {_dump_scalar(proj[key])}")
                    first = False
    Path(path).write_text("\n".join(out) + "\n", encoding="utf-8")


def projects(data):
    for cat in data["categories"]:
        for dev in cat["devices"]:
            for proj in dev["projects"]:
                yield cat, dev, proj
