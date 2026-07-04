# Fifth-Color Demand Theory (FCD Theory)

> A Structural Theory of Planar Graph Coloring

---

## Project Vision

This project does not aim to re-prove the Four Color Theorem directly.

Its goal is to build a mathematical framework for describing the origin, propagation, interaction, and elimination of **Fifth-Color Demand** in planar graph coloring. The Four Color Theorem is treated as a possible application of this framework, not as its starting point.

---

## Current Status

✅ Stage 0

Foundation construction. The repository has now formed a closed working proof chain for the current central claim, while still remaining at the stage of definitions, structure, and proof refinement rather than final theorem packaging.

---

## Guiding Principles

1. Definitions come before theorems.
2. Every statement must have a clear status: Definition, Proposition, Lemma, Theorem, Corollary, Conjecture, Observation, or Open Problem.
3. Intuition must not be presented as proof.
4. Established notation should remain stable across later chapters.
5. Each chapter should be independently readable.

---

## Research Philosophy

Traditional graph coloring often follows the line

Graph -> Coloring -> Proof

FCD Theory instead emphasizes

Coloring States -> Dynamics -> Propagation -> Potential -> Structure -> Theorem

---

## Long-term Objectives

Volume 0 -> Foundations of Thinking  
Volume I -> Foundations  
Volume II -> Structure Theory  
Volume III -> Applications  
Software -> Tool Support  
AI-assisted Discovery -> Long-term research assistance

---

## Repository Structure

FCD-Theory/

├── README.md

│   项目总览、研究原则与阶段说明

├── ROADMAP.md

│   研究推进路线与阶段目标

├── CHANGELOG.md

│   版本变更记录（当前为占位）

├── LICENSE

│   仓库许可与草稿状态说明

├── CONTRIBUTING.md

│   协作规范（当前为占位）

│

├── docs/

│ ├── Glossary.md

│ │   术语表（已同步持续需求与双核结构术语）

│ ├── Notation.md

│ │   记号表（已同步持续需求与双核结构记号）

│ ├── Bibliography.md

│ │   参考文献整理（待扩充）

│ ├── OpenProblems.md

│ │   开放问题列表（待扩充）

│ └── ResearchLog.md

│     研究日志与问题跟踪

│

├── Volume0/

│   基础思想与方法论预留目录

├── Volume1/

│ └── Fifth-Color_Demand_Theory_Framework.md

│     理论框架、核心对象与中心猜想

├── Volume2/

│   结构理论与引理链预留目录

├── Volume3/

│   应用方向预留目录

│

├── examples/

│   示例图、局部构型与反例搜索预留目录

├── figures/

│   图示、结构图与论文插图预留目录

├── algorithms/

│   算法化分析与程序原型预留目录

├── software/

│   后续软件实现预留目录

├── experiments/

│   实验记录与验证输出预留目录

├── papers/

│ └── PAPER.md

│     当前论文主稿

└── archive/

	历史草稿与归档材料预留目录


Core files:

- README.md: 项目总览、研究原则与阶段说明
- ROADMAP.md: 研究推进路线与阶段目标
- papers/PAPER.md: 当前论文主稿
- Volume1/Fifth-Color_Demand_Theory_Framework.md: 理论框架与核心对象
- docs/ResearchLog.md: 研究日志与开放问题跟踪

---

## Current Milestone

Stage 0: build the mathematical language and consolidate the first paper draft.

Current tasks:

- [x] Establish notation and terminology scaffolding
- [x] Define Coloring State Space and local persistence interfaces
- [x] Align the paper structure with the repository structure
- [x] Refine the central claim into a lemma-based proof program
- [x] Enumerate the working finite double-core configuration family
- [x] Write I-IV class exclusion lemmas for the working configuration family
- [ ] Refine each exclusion lemma into tighter local configuration checks
- [ ] Convert the working proof chain into a stricter theorem-grade version

No final theorem claim should be made before these refinements are complete.

---

## Research Workflow

Every new idea should pass through the following pipeline:

Idea -> Definition -> Examples -> Counterexamples -> Properties -> Conjecture -> Proof -> Application

Ideas are never promoted directly into theorems.

---

## Citation Policy

Any result inherited from classical graph theory must cite its source. New concepts introduced by FCD Theory should explicitly indicate whether they are `Draft`, `Experimental`, or `Stable`.

---

## Paper Focus

Current paper target:

中文：在最小围长大于 3 的、3-正则的任意平面图上，最多只有一个顶点具有持续第五色需求。

English: On any cubic planar graph of girth greater than three, at most one vertex can exhibit a persistent fifth-color demand.

Current status:

The repository now contains a structured paper draft in `papers/PAPER.md`. The claim above is supported by a closed working proof chain built from definitions, connector lemmas, finite configuration compression, class-by-class exclusion, and a closing uniqueness argument. It is not yet presented as a final theorem-grade proof.

---

## License

Research Draft

Version 0.1

Last Updated

2026-07-05