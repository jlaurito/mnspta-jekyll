#!/usr/bin/env python3
"""
Download all site assets from the current (Neon) CDN to assets/images/.

Run this once before cancelling Neon. After the migration, images will be
served from the Jekyll repo and the Neon CDN dependency is gone.

Usage:
    python3 scripts/download_assets.py

Re-running is safe — files that already exist are skipped.
"""

from __future__ import annotations
import os
import sys
import urllib.request
import urllib.error

# Map of (local filename, source URL on Neon CDN).
# Sources verified by crawling https://www.mnspta.org/ on 2026-05-09.
ASSETS: list[tuple[str, str]] = [
    # Branding
    ("logo-wordmark.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/Website-MNS-transp2-1920w.png"),
    ("logo_200x200.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/logo_200x200-1920w.png"),

    # Home page
    ("home-banner.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/pre-kfieldday-banner-1920w.jpg"),
    ("volunteer-flyer.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/PTA-volunteer-flyer-1-274x300-1920w.jpg"),
    ("mables-logo.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/mables-logo2-300x92-1920w.png"),
    ("minted-logo.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/minted-logo-300x92-1920w.png"),
    ("annual-appeal-icon.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/annual-appeal-icon-website-224x300-1920w.png"),
    ("school-store.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/Screen-Shot-2018-09-20-at-9.39.18-PM-300x272-1920w.png"),
    ("mns-bulletin.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/MNS-bulletin-1920w.png"),

    # About page
    ("mns-front.jpeg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/mns-front-sm-230x300-1920w.jpeg"),

    # Shopping rewards
    ("minted-promo.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/pasted-image-0-1-571x1024-1920w.jpg"),
    ("mables-promo.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/pasted-image-0-792x1024-1920w.jpg"),

    # MNS Cares
    ("mns-cares.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/MNS-Cares-300x216-1920w.jpg"),
    ("john-jay-1.jpeg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/IMG_0377-1-300x225-1920w.jpeg"),
    ("john-jay-2.jpeg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/IMG_0617-1-300x224-1920w.jpeg"),

    # Events (currently unused — events page reads from _data/events.yml.
    # If you re-enable the seasonal events, place these in events/ subdir.)
    ("events/yankees-2023.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/MNS-Yankees-Game-Sept-10-2023-1-1920w.jpg"),
    ("events/mets-2023.jpg",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/MNS-Mets-Game-Oct-1-2023-1-1-1920w.jpg"),

    # Neon account
    ("did-you-know.png",
     "https://lirp.cdn-website.com/b2500da4/dms3rep/multi/opt/Did-you-know-300x162-1920w.png"),
]

DEST_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Referer": "https://www.mnspta.org/",
}


def download(url: str, dest_path: str) -> str:
    if os.path.exists(dest_path):
        return "skip (exists)"
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        return f"FAIL ({e.code} {e.reason})"
    except Exception as e:
        return f"FAIL ({e})"
    with open(dest_path, "wb") as f:
        f.write(data)
    return f"ok ({len(data):,} bytes)"


def main() -> int:
    print(f"Downloading {len(ASSETS)} assets to {os.path.abspath(DEST_DIR)}")
    failures = 0
    for name, url in ASSETS:
        dest = os.path.join(DEST_DIR, name)
        result = download(url, dest)
        print(f"  {name:32s} {result}")
        if result.startswith("FAIL"):
            failures += 1
    print()
    if failures:
        print(f"{failures} download(s) failed. URLs may have changed; "
              "open them in a browser, save manually into assets/images/.")
        return 1
    print("All assets ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
