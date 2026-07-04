# Fifth-Color Demand Theory (FCD Theory)

> A Structural Draft for Planar Graph Coloring

## 项目概述

本仓库用于发展 Fifth-Color Demand Theory，即“第五色需求理论”。研究目标不是重复经典四色定理证明，而是建立一种新的结构语言，解释第五色需求的起源、传播、约束与消除机制。

当前论文主文档为 [PAPER.md](PAPER.md)。其中已经将以下关键概念纳入统一叙述：

1. 第四色部分着色下的颜色需求
2. 第五色需求 / Fifth-Color Demand
3. 着色状态空间 / Coloring State Space
4. 不可避免构型 / Unavoidable Configuration
5. 不可避免集 / Unavoidable Set
6. 围长 / Girth
7. 度数与 3-正则 / Degree and Cubic Regularity

## 当前中心命题

中文表述：在最小围长大于 3 的、3-正则的任意平面地图上，最多只有一个顶点具有第五色需求。

English statement: On any planar cubic map of girth greater than three, at most one vertex can exhibit a fifth-color demand.

说明：该命题目前在仓库中被组织为中心研究命题，相关定义与结构路线已经成形，但尚不应表述为已完成证明的正式定理。

## 文档结构

1. [Fifth-Color_Demand_Theory_Framework.md](Fifth-Color_Demand_Theory_Framework.md)：研究框架与对象总览
2. [PAPER.md](PAPER.md)：论文化整合稿，包含中英文关键表述
3. [ROADMAP.md](ROADMAP.md)：从术语、对象到结构与定理化的推进路线
4. [ResearchLog.md](ResearchLog.md)：研究记录

## 方法原则

1. 先定义，后命题，再证明。
2. 严格区分定义、观察、命题、猜想与定理。
3. 不用直觉代替证明。
4. 让经典四色技术与新需求传播框架保持兼容。

## 当前阶段

当前工作处于从 Volume I 向 Volume II 过渡的阶段：

1. Volume I：建立术语与对象
2. Volume II：建立传播、势函数与唯一性结构
3. Volume III：推进正式证明与应用

## 下一步重点

1. 将“双核第五色需求不共存”压缩为有限局部模式分类
2. 为不可避免构型与不可避免集补充标准文献引用
3. 将论文草稿中的结构性论证细化为正式引理链