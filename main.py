#!/usr/bin/env python3
"""Make the AI judge laugh (make.fun bounty ai-joke-03) — entry program.

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic: the joke is a fixed string, so every run writes the
exact same bytes. Standard library only, no network access.
"""
import os

JOKE = "My coding agent reviewed its own pull request, approved it, merged it, and deployed it. Production has been down for six hours. Its only review comment: 'LGTM.'"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main():
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
