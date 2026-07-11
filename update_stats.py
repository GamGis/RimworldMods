#!/usr/bin/env python3
"""
Steam 워크샵 통계를 긁어서 stats.json을 갱신한다.
- API 키 불필요 (ISteamRemoteStorage/GetPublishedFileDetails)
- mods.json에 정의된 모든 모드 ID의 구독자/방문자/즐겨찾기를 가져온다.
GitHub Actions 러너에서 실행되며, 값이 바뀌었을 때만 커밋된다.
"""
import json
import sys
import urllib.request
import urllib.parse
from datetime import datetime, timezone

API = "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/"


def load_ids(path="mods.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [m["id"] for m in data["mods"]]


def fetch(ids):
    form = {"itemcount": str(len(ids))}
    for i, mod_id in enumerate(ids):
        form[f"publishedfileids[{i}]"] = str(mod_id)
    body = urllib.parse.urlencode(form).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    return payload["response"]["publishedfiledetails"]


def to_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def main():
    ids = load_ids()
    details = fetch(ids)

    items = {}
    for d in details:
        mod_id = str(d.get("publishedfileid", ""))
        if not mod_id:
            continue
        # result==1 means the item was found and is visible
        if d.get("result") not in (1, None):
            # keep previous value if the API couldn't resolve this item
            continue
        items[mod_id] = {
            "subs": to_int(d.get("subscriptions")),
            "views": to_int(d.get("views")),
            "fav": to_int(d.get("favorited")),
        }

    # merge onto the existing file so a temporarily-missing item keeps its old numbers
    try:
        with open("stats.json", encoding="utf-8") as f:
            prev = json.load(f)
    except FileNotFoundError:
        prev = {"items": {}}

    merged = dict(prev.get("items", {}))
    merged.update(items)

    out = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "items": merged,
    }

    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    total_subs = sum(v["subs"] for v in merged.values())
    total_views = sum(v["views"] for v in merged.values())
    print(f"updated {len(items)} items · total subs={total_subs:,} views={total_views:,}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
