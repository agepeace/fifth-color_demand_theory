#!/usr/bin/env python3
"""Second pass: carefully replace remaining 3-正则 references.
Only handle clear mechanical patterns; leave substantive proof arguments for manual editing."""
import pathlib

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

replacements = [
    # Section titles
    ("\u5e73\u9762\u56fe\u3001\u56f4\u957f\u4e0e 3-\u6b63\u5219", "\u5e73\u9762\u56fe\u4e0e\u56f4\u957f"),
    ("\u5e73\u9762\u6027\u3001\u56f4\u957f\u4e0e 3-\u6b63\u5219\u5e26\u6765\u7684\u538b\u7f29\u673a\u5236", "\u5e73\u9762\u6027\u4e0e\u56f4\u957f\u5e26\u6765\u7684\u538b\u7f29\u673a\u5236"),
    ("\u4e3a\u4f55\u7279\u522b\u5f3a\u8c03\u5e73\u9762\u6027\u3001\u56f4\u957f\u4e0e 3-\u6b63\u5219", "\u4e3a\u4f55\u7279\u522b\u5f3a\u8c03\u5e73\u9762\u6027\u4e0e\u56f4\u957f"),
    # Lemma hypotheses: "设 G 为 3-正则平面图" -> "设 G 为平面图"
    ("\u8bbe $G$ \u4e3a 3-\u6b63\u5219\u5e73\u9762\u56fe", "\u8bbe $G$ \u4e3a\u5e73\u9762\u56fe"),
    # "3-正则条件" -> "围长条件"
    ("3-\u6b63\u5219\u6761\u4ef6", "\u56f4\u957f\u6761\u4ef6"),
    # "cubic regularity" in English
    ("cubic regularity", "girth constraints"),
    # Framework.md: "3-regular (cubic)" line
    ("3-regular (cubic): every vertex has degree exactly 3.", "girth at least 5: no triangles and no 4-cycles."),
    # "无三角且 3-正则的条件下" -> "围长大于等于 5 的条件下"
    ("\u65e0\u4e09\u89d2\u4e14 3-\u6b63\u5219\u7684\u6761\u4ef6\u4e0b", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5 \u7684\u6761\u4ef6\u4e0b"),
    # "无三角 3-正则平面图" -> "围长大于等于 5 的平面图"
    ("\u65e0\u4e09\u89d2 3-\u6b63\u5219\u5e73\u9762\u56fe", "\u56f4\u957f\u5927\u4e8e\u7b49\u4e8e 5 \u7684\u5e73\u9762\u56fe"),
    # "度数与 3-正则" -> "度数与围长"
    ("\u5ea6\u6570\u4e0e 3-\u6b63\u5219", "\u5ea6\u6570\u4e0e\u56f4\u957f"),
    # "利用 Euler 公式、面长度下界与 3-正则条件" -> already handled by 3-正则条件 replacement
    # "平面 3-正则嵌入" -> "平面嵌入"
    ("\u5e73\u9762 3-\u6b63\u5219\u5d4c\u5165", "\u5e73\u9762\u5d4c\u5165"),
    # "对 3-正则平面图而言" -> "对目标平面图而言"
    ("\u5bf9 3-\u6b63\u5219\u5e73\u9762\u56fe\u800c\u8a00", "\u5bf9\u76ee\u6807\u5e73\u9762\u56fe\u800c\u8a00"),
    # "由于 G 是 3-正则平面图" -> "由于 G 是平面图"
    ("\u7531\u4e8e $G$ \u662f 3-\u6b63\u5219\u5e73\u9762\u56fe", "\u7531\u4e8e $G$ \u662f\u5e73\u9762\u56fe"),
    # "在 3-正则条件下" -> "在围长条件下" (in proof arguments)
    ("\u5728 3-\u6b63\u5219\u6761\u4ef6\u4e0b", "\u5728\u56f4\u957f\u6761\u4ef6\u4e0b"),
    # "3-正则平面图中" -> "平面图中"
    ("3-\u6b63\u5219\u5e73\u9762\u56fe\u4e2d", "\u5e73\u9762\u56fe\u4e2d"),
    # "3-正则图" standalone (in Corollary 6.6.1 etc) - leave for manual handling
    # "3-正则" standalone in proofs - leave for manual handling
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
