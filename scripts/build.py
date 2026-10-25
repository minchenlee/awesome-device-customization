"""Generate README.md (English) and README.zh-TW.md (Traditional Chinese) from data/devices.yaml."""

import re

import devices

TEXT = {
    "en": {
        "file": "README.md",
        "other": "[繁體中文](README.zh-TW.md)",
        "title": "# Awesome Device Customization [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "intro": (
            "> Community projects that customize consumer devices, organized by device model.\n\n"
            "You own a device. Which open-source projects let you do more with it? "
            "This list answers that question by model, across brands and device types: "
            "open firmware, local control, add-on apps, configuration files, and compatible accessories."
        ),
        "contents": "## Contents",
        "flags_head": "## Risk markers",
        "flags_intro": "Each project shows the markers that apply to it.",
        "columns": "| Project | What it does | ★ | Last push | License | Markers |",
        "rules_head": "## Inclusion rules",
        "rules": (
            "Included: legal customization of a device you own. Examples are open-source firmware, "
            "local control without the vendor cloud, add-on apps, configuration and recipe files, "
            "and compatible accessories.\n\n"
            "Not included: DRM removal, license key or paywall bypass, piracy, game ROMs, account sharing, "
            "and carrier unlock bypass. Projects that unlock your own device (for example an e-reader) "
            "are linked to their project page only, with the ⚠️ marker. This list gives no unlock steps "
            "and hosts no code, firmware, or files. If GitHub disables a linked repository, "
            "for example after a DMCA notice, the entry is removed. Project owners can ask for removal in an issue.\n\n"
            "Projects with no push for more than 3 years are left out or marked 📦. "
            "Stars, last push dates, and licenses come from the GitHub API "
            "(`scripts/refresh.py`); the last refresh was on {date}."
        ),
        "disclaimer_head": "## Disclaimer",
        "disclaimer": (
            "You are responsible for your own device. Modifications can damage hardware, void the warranty, "
            "or break vendor terms. In some countries, anti-circumvention law can also restrict unlocking a device. "
            "Work on mains-powered devices (⚡) can kill you: unplug the device and "
            "let a qualified person do the work if you are not sure. Obey local law and your warranty terms. "
            "The projects belong to their authors; this list does not check their code."
        ),
        "more_head": "## Further reading",
        "more": [
            ("frenck/awesome-home-assistant", "Home Assistant integrations and resources."),
            ("KindleTweaks/Awesome-Kindle", "Kindle tweaks and tools."),
            ("vitalets/awesome-smart-tv", "Smart TV app development."),
            ("Generator/Awesome-Android-TV-FOSS-Apps", "Free and open-source Android TV apps."),
            ("asapelkin/awesome-eink", "E-ink devices and software."),
        ],
        "contrib_head": "## Contributing",
        "contrib": "Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request.",
        "license_head": "## License",
        "license": "[CC0-1.0](LICENSE). To the extent possible under law, the contributors waived all copyright to this list.",
    },
    "zh": {
        "file": "README.zh-TW.md",
        "other": "[English](README.md)",
        "title": "# Awesome Device Customization（裝置客製化清單）[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "intro": (
            "> 按裝置型號整理的社群客製化專案。\n\n"
            "你有一台裝置。社群做了哪些開源專案，讓它做更多事？"
            "這份清單按型號回答，跨品牌、跨類別：開源韌體、本機控制、外掛 app、設定檔與相容配件。"
        ),
        "contents": "## 目錄",
        "flags_head": "## 風險標記",
        "flags_intro": "每個專案會顯示適用的標記。",
        "columns": "| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |",
        "rules_head": "## 收錄規則",
        "rules": (
            "收錄：對自己的裝置做合法的客製化。例如開源韌體、不經原廠雲端的本機控制、外掛 app、"
            "設定檔與配方檔、相容配件。\n\n"
            "不收錄：破解 DRM、繞過授權金鑰或付費機制、盜版、遊戲 ROM、帳號共享、繞過電信鎖。"
            "解鎖自己裝置的專案（例如電子書閱讀器）只連到專案頁，並加上 ⚠️ 標記。本清單不提供解鎖步驟，"
            "也不存放任何程式碼、韌體或檔案。連結的 repo 若被 GitHub 停用（例如收到 DMCA 通知），就會移除該筆。"
            "專案作者可以開 issue 要求移除。\n\n"
            "超過 3 年沒有更新的專案不收，或標為 📦。星數、最後更新日期與授權來自 GitHub API"
            "（`scripts/refresh.py`），最近一次更新在 {date}。"
        ),
        "disclaimer_head": "## 免責聲明",
        "disclaimer": (
            "自己的裝置自己負責。改裝可能損壞硬體、失去保固或違反原廠條款。"
            "在部分國家，解鎖裝置也可能受反規避法規限制。"
            "改裝接市電的裝置（⚡）可能致命：先拔插頭；沒有把握就交給合格的人做。"
            "請遵守當地法律與保固條款。專案屬於各自的作者，本清單不檢查它們的程式碼。"
        ),
        "more_head": "## 延伸閱讀",
        "more": [
            ("frenck/awesome-home-assistant", "Home Assistant 整合與資源。"),
            ("KindleTweaks/Awesome-Kindle", "Kindle 調校與工具。"),
            ("vitalets/awesome-smart-tv", "智慧電視 app 開發。"),
            ("Generator/Awesome-Android-TV-FOSS-Apps", "自由開源的 Android TV app。"),
            ("asapelkin/awesome-eink", "電子紙裝置與軟體。"),
        ],
        "contrib_head": "## 貢獻方式",
        "contrib": "開 pull request 前，請先讀 [CONTRIBUTING.md](CONTRIBUTING.md)。",
        "license_head": "## 授權",
        "license": "[CC0-1.0](LICENSE)。在法律允許的範圍內，貢獻者放棄本清單的所有著作權。",
    },
}


def license_text(spdx, zh):
    if spdx == "NOASSERTION":
        return "未偵測到" if zh else "Not detected"
    return spdx


def anchor(title):
    slug = re.sub(r"[^\w\- ]", "", title.lower()).strip()
    return slug.replace(" ", "-")


def render(data, lang):
    t = TEXT[lang]
    zh = lang == "zh"
    last = (devices.ROOT / "data" / "refreshed.txt").read_text().strip()
    out = [t["title"], "", t["other"], "", t["intro"], "", t["contents"], ""]
    for cat in data["categories"]:
        title = cat["title_zh"] if zh else cat["title"]
        out.append(f"- [{title}](#{anchor(title)})")
    for head in ("rules_head", "flags_head", "disclaimer_head", "more_head", "contrib_head", "license_head"):
        out.append(f"- [{t[head][3:]}](#{anchor(t[head][3:])})")
    out.append("")
    for cat in data["categories"]:
        out += [f"## {cat['title_zh'] if zh else cat['title']}", ""]
        for dev in cat["devices"]:
            out += [f"### {dev['model']}", "", t["columns"], "|---|---|---:|---|---|---|"]
            for p in dev["projects"]:
                marks = " ".join(devices.FLAGS[f][0] for f in p["flags"])
                summary = p["summary_zh"] if zh else p["summary"]
                out.append(
                    f"| [{p['name']}](https://github.com/{p['repo']}) | {summary} | "
                    f"{p['stars']:,} | {p['pushed']} | {license_text(p['license'], zh)} | {marks} |"
                )
            out.append("")
    out += [t["rules_head"], "", t["rules"].replace("{date}", last), ""]
    out += [t["flags_head"], "", t["flags_intro"], "", "| | |", "|---|---|"]
    for icon, en, zh_text in devices.FLAGS.values():
        out.append(f"| {icon} | {zh_text if zh else en} |")
    out += ["", t["disclaimer_head"], "", t["disclaimer"], "", t["more_head"], ""]
    for repo, desc in t["more"]:
        out.append(f"- [{repo.split('/')[1]}](https://github.com/{repo}) - {desc}")
    out += ["", t["contrib_head"], "", t["contrib"], "", t["license_head"], "", t["license"], ""]
    return "\n".join(out)


def main():
    data = devices.load()
    for lang, t in TEXT.items():
        (devices.ROOT / t["file"]).write_text(render(data, lang), encoding="utf-8")


if __name__ == "__main__":
    main()
