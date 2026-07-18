#!/usr/bin/env python3
"""Batch replace girth condition: cubic planar girth>3 -> planar girth>=5"""
import pathlib, sys

base = pathlib.Path(r'C:\workspace\projects\fifth-color_demand_theory')

files = [
    'papers/PAPER.md',
    'README.md',
    'ROADMAP.md',
    'Volume1/Fifth-Color_Demand_Theory_Framework.md',
    'docs/Glossary.md',
    'docs/Notation.md',
    'docs/Bibliography.md',
    'docs/OpenProblems.md',
    'docs/ResearchLog.md',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
]

# Ordered replacements (most specific first to avoid partial matches)
replacements = [
    # Chinese: most specific multi-word patterns first
    ("\u6700\u5c0f\u56f4\u957f\u5927\u4e8e 3 \u7684 3-\u6b63\u5219\u5e73\u9762\u56fe", "\u6700\u5c0f\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5 \u7684\u5e73\u9762\u56fe"),
    ("\u56f4\u957f\u5927\u4e8e 3 \u4e14 3-\u6b63\u5219\u7684\u5e73\u9762\u56fe", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5 \u7684\u5e73\u9762\u56fe"),
    ("\u56f4\u957f\u5927\u4e8e 3 \u7684 3-\u6b63\u5219\u5e73\u9762\u56fe", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5 \u7684\u5e73\u9762\u56fe"),
    # LaTeX condition with 3-正则
    ("$g(G)>3$ \u7684 3-\u6b63\u5219\u5e73\u9762\u56fe", "$g(G)\\ge 5$ \u7684\u5e73\u9762\u56fe"),
    ("$g(G) > 3$ \u7684 3-\u6b63\u5219\u5e73\u9762\u56fe", "$g(G)\\ge 5$ \u7684\u5e73\u9762\u56fe"),
    # Standalone LaTeX condition
    ("$g(G)>3$", "$g(G)\\ge 5$"),
    ("$g(G) > 3$", "$g(G)\\ge 5$"),
    # Chinese girth (remaining standalone)
    ("\u56f4\u957f\u5927\u4e8e $3$", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e $5$"),
    ("\u56f4\u957f\u5927\u4e8e 3", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5"),
    # English conditions
    ("cubic planar graphs of girth greater than three", "planar graphs of girth at least five"),
    ("cubic planar graph with girth greater than three", "planar graph with girth at least five"),
    ("planar cubic graphs with girth greater than three", "planar graphs with girth at least five"),
    ("planar cubic graph of girth greater than three", "planar graph of girth at least five"),
    ("planar cubic maps with girth greater than 3", "planar graphs with girth at least 5"),
    ("girth greater than three", "girth at least five"),
    ("girth greater than 3", "girth at least 5"),
]

total_changes = 0
for f in files:
    p = base / f
    if not p.exists():
        print(f"SKIP (not found): {f}")
        continue
    text = p.read_text(encoding="utf-8", newline="")
    original = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != original:
        p.write_text(text, encoding="utf-8", newline="\n")
        print(f"Updated: {f}")
        total_changes += 1
    else:
        print(f"No changes: {f}")

print(f"\nTotal files changed: {total_changes}")
