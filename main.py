"""Draft flaw: the first line simply refused the job and offered no excuse.
Revision fix: the final line invents a peace treaty that the dust bunnies pay for in crumbs."""

import os

TEXT = "I didn't skip under the couch; I was honoring its peace treaty with the dust bunnies, who now pay rent in crumbs."

assert TEXT == TEXT.strip()
assert "\n" not in TEXT
assert 1 <= len(TEXT) <= 120

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
