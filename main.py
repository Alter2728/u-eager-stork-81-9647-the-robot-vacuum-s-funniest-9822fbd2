"""Draft blames a full dustbin, an excuse any appliance could make.
Revision gives the vacuum a lost fight, a dock, and a sock it cannot explain."""

import os

TEXT = "I skipped that corner: the dog owns it, and last time he won I woke on my dock in a sock."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT and "\r" not in TEXT
assert 1 <= len(TEXT) <= 120

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
