# Glossary

## 文档说明

本文件整理 Fifth-Color Demand Theory（FCD Theory）当前阶段使用的核心术语，并给出统一、可扩展的定义说明。

术语表的目标不是替代论文正文中的正式定义，而是提供一个稳定的术语入口，避免 README、Framework、PAPER 与后续 Volume 文档之间出现同名异义或多种译法并存的情况。

---

## 1. 使用原则

1. 每个术语应尽量对应唯一含义。
2. 中文名、英文名与功能描述应同时给出。
3. 若某术语已经在论文正文中形式化定义，本文件只做摘要性整理，不重复完整证明语境。
4. 后续新增术语应尽量放入已有类别，避免术语表碎片化。

---

## 2. 基础图论术语

### 平面图 / Planar Graph

可以在平面上无边交叉嵌入的图。本文当前统一以平面图作为主术语；若强调某一具体嵌入，再在上下文中显式说明。

### 顶点 / Vertex

图的基本点对象，记为 $v$、$u$ 等。

### 边 / Edge

连接两个顶点的基本关系对象，通常记为 $uv$ 或属于 $E(G)$ 的元素。

### 邻域 / Neighborhood

顶点 $v$ 的邻域，记为 $N(v)$，表示所有与 $v$ 相邻的顶点集合。

### 度数 / Degree

顶点的邻接边数量，记为 $\deg(v)$。

### 围长 / Girth

图中所有简单环长度的最小值，记为 $g(G)$。

### 3-正则 / Cubic or 3-Regular

每个顶点度数都恰为 3 的图类条件。本文的中心研究对象之一。

---

## 3. 经典四色理论相关术语

### 四色问题 / Four Color Problem

研究平面图是否总能用 4 种颜色进行合法顶点着色的问题。

### Kempe 链 / Kempe Chain

围绕两种颜色形成的连通链式结构，是经典局部重着色分析中的核心工具。

### 不可避免构型 / Unavoidable Configuration

在某个目标图族中，每张图都必须包含的局部构型。

### 不可避免集 / Unavoidable Set

若干构型组成的集合，使目标图族中的每张图都至少包含其中一个构型。

### 可约构型 / Reducible Configuration

若某种局部构型一旦出现在极小反例中即可导出矛盾，则称其为可约构型。该术语在本仓库中尚未作为 FCD Theory 的主对象，但与后续连接经典四色技术密切相关。

### 卸载法 / Discharging Method

借助局部电荷分配与 Euler 公式控制全局结构的经典平面图方法。

---

## 4. FCD Theory 核心术语

### 第五色需求 / Fifth-Color Demand

在某个部分 4-着色状态下，若顶点已无任何可用颜色，则称该顶点出现第五色需求。它是本文的中心局部对象。

### 可用颜色集 / Available-Color Set

对顶点 $v$ 与部分着色 $\varphi$，记 $D(v,\varphi)$ 为在当前状态下仍可赋给 $v$ 的颜色集合。

### 第五色需求指标 / Fifth-Color Demand Indicator

记作 $F(v,\varphi)$。当顶点 $v$ 在状态 $\varphi$ 下具有第五色需求时取值为 1，否则为 0。

### 色压 / Color Pressure

记作 $\pi(v,\varphi)$，定义为 $4-|D(v,\varphi)|$。它用于度量在当前部分着色状态下有多少颜色已被阻断。

### 广义第五色需求 / Generalized Fifth-Color Demand

记作 $F^{\dagger}(v,\varphi)$。当 $|D(v,\varphi)|\le 1$ 时取值为 1，否则为 0。它是本文在 3-正则图上继续研究第五色需求时采用的工作性扩展对象。

### 部分 4-着色 / Partial 4-Coloring

仅对部分顶点赋予 $\{1,2,3,4\}$ 中颜色、且已赋色顶点之间满足合法性的着色状态。

### 着色状态空间 / Coloring State Space

记作 $\mathcal{S}(G)$。其顶点是图 $G$ 的合法部分 4-着色状态，边表示允许的局部状态变换。

### 阻碍传播图 / Obstruction Propagation Graph

记作 $\mathcal{P}(G)$。用于描述第五色需求在状态空间中的传播、锁定或伴随关系。

### 第五色核心 / Fifth-Color Core

记作 $C_5(G)$。表示在某些可达着色状态中持续表现出第五色需求的顶点集合。

### 持续第五色需求 / Persistent Fifth-Color Demand

指某个需求并非偶发出现，而是在允许的局部变换范围内仍持续存在。

### 允许局部变换 / Allowed Local Transformation

指在给定图与当前着色状态中，被理论正式允许执行的局部重着色、交换或有限步修正操作，用以定义“可达状态邻域”与“持续性”。

### 可达状态邻域 / Reachable State Neighborhood

指从某个初始着色状态出发，在给定步数上界或不设步数上界的条件下，可由允许局部变换到达的状态集合。

### 冻结球 / Frozen Ball

指围绕某个顶点的局部球形邻域，在指定允许变换范围内保持阻塞或保持结构不变的工作性局部对象。

### 持续需求核 / Persistent Demand Core

指在允许局部变换作用下仍持续维持第五色需求的顶点或局部阻塞中心。本文第 6 节的中心命题以此为真正研究对象，而不是静态的 $F(v,\varphi)=1$ 事件。

### 工作性证明链 / Working Proof Chain

指 PAPER.md 第 6 节当前已经写出的、从对象定义经过结构化引理、有限构型压缩、逐类排除再到闭合回推的论证链。它表明中心命题已经具有连续论证主线，但尚未达到最终定理级证明。

### 局部刚性 / Local Rigidity

指某一局部接口原型或候选构型在有限冻结球内不能再被削弱、收缩或替代的性质；它是后续微型构型枚举与逐类排除中最常用的局部约束。

### 最小消除步长 / Minimal Elimination Length

指消除某个局部持续需求所需的最少允许局部变换步数，用于衡量阻塞强度与局部可消除性的距离。

### 需求见证子图 / Demand Witness Subgraph

指承载某个持续需求核的极小连通局部子图；在该子图支撑范围内执行允许局部变换，仍不能消除相应需求。

### 极小见证边界 / Minimal Witness Boundary

指某个极小需求见证子图的边界部分，并要求该边界上的每个点都对阻塞传播或阻塞锁定有实质贡献，且不能在有限冻结球内进一步局部削弱。

### 接口原型 / Interface Prototype

指极小见证边界对外连接时出现的基本局部类型。当前工作稿将其压缩为三类：单口原型、双口原型与回返原型；它们是后续 I/II/III/IV 型双核候选分类的局部来源。

其中，单口原型现已补入“局部饱和条件”，双口原型现已补入“不可冗余配对”条件，作为从第一步局部边界分析通向后续 II 型、III 型排除引理的中间刚性层。

### 双核连接体 / Double-Core Connector

指两个不同持续需求核在共存时被强迫诱导出的连通结构对象，记作 $\Xi(u,v;\varphi)=H_u\cup P\cup H_v$。

### 平面压缩约束 / Planar Compression Constraint

指由平面性、围长下界与 3-正则条件共同施加在双核连接体上的面-边-点结构限制。

### 有限构型族 / Finite Configuration Family

指在平面压缩约束下，所有剩余双核候选可被压缩进的有限个局部同构类型集合；本文记作 $\mathfrak{C}_{\mathrm{double}}$。

### 局部可消除性 / Local Eliminability

指第五色需求可通过有限次允许的局部变换被消除。

### 需求传播 / Demand Propagation

指一个需求点的存在如何迫使其他顶点继续处于高张力或空可用颜色状态的结构机制。

### 双核共存 / Dual-Core Coexistence

指两个彼此独立的第五色需求核心同时稳定存在的情形。当前研究计划的重要目标之一是排除此类结构。

### 唯一性主张 / Uniqueness Claim

指当前论文中的中心研究命题：在最小围长大于等于 5 的任意平面图上，最多只有一个顶点具有持续第五色需求，等价地说，至多存在一个持续需求核。当前将其作为工作性命题处理，并由 PAPER.md 第 6 节的工作性证明链支撑，尚未达到最终定理级证明。

---

## 5. 研究组织术语

### 理论框架 / Framework

指对对象、关系、命题层级和研究边界的整体组织方式。目前由 Volume1 文档承担。

### 论文主稿 / Research Paper

指 papers/PAPER.md，对外承担当前最完整的连续论述。该文当前仍是工作性研究论文，而不是最终定理稿。

### 路线图 / Roadmap

指 ROADMAP.md，用于描述从定义到结构理论再到定理化的阶段推进。

### 研究日志 / Research Log

指 docs/ResearchLog.md，用于记录分支问题、未定结论与推进痕迹。

---

## 6. 当前推荐统一译法

为避免同一术语出现多种写法，当前建议优先采用以下统一形式：

1. Fifth-Color Demand: 第五色需求
2. Color Pressure: 色压
3. Generalized Fifth-Color Demand: 广义第五色需求
4. Persistent Fifth-Color Demand: 持续第五色需求
5. Persistent Demand Core: 持续需求核
6. Working Proof Chain: 工作性证明链
7. Local Rigidity: 局部刚性
8. Allowed Local Transformation: 允许局部变换
9. Reachable State Neighborhood: 可达状态邻域
10. Demand Witness Subgraph: 需求见证子图
11. Double-Core Connector: 双核连接体
12. Planar Compression Constraint: 平面压缩约束
13. Finite Configuration Family: 有限构型族
14. Cubic Graph: 3-正则图 或 cubic graph

---

## 7. 首次出现章节索引

以下索引以 papers/PAPER.md 当前章节编号为准，用于快速定位术语首次被正式引入或集中说明的位置。

- 平面图 / Planar Graph: papers/PAPER.md 第 2.1 节“平面图、围长与 3-正则”
- 围长 / Girth: papers/PAPER.md 第 1.2 节首次记号出现；第 2.1 节“平面地图、围长与 3-正则”集中定义
- 度数 / Degree: papers/PAPER.md 第 1.2 节首次记号出现；第 2.1 节“平面地图、围长与 3-正则”集中说明
- 3-正则 / Cubic or 3-Regular: papers/PAPER.md 第 2.1 节“平面地图、围长与 3-正则”
- 四色问题 / Four Color Problem: papers/PAPER.md 第 1 节“引言”
- Kempe 链 / Kempe Chain: papers/PAPER.md 第 1 节“引言”首次出现；第 1.3 节“经典背景与文献定位”集中定位
- 不可避免构型 / Unavoidable Configuration: papers/PAPER.md 第 1.3 节首次出现；第 2.5 节“不可避免构型”集中定义
- 不可避免集 / Unavoidable Set: papers/PAPER.md 第 1.3 节首次出现；第 2.6 节“不可避免集”集中定义
- 第五色需求 / Fifth-Color Demand: papers/PAPER.md 第 1 节“引言”首次提出；第 2.3 节“第五色需求”正式定义
- 可用颜色集 / Available-Color Set: papers/PAPER.md 第 1 节“引言”概念性出现；第 2.2 节“颜色需求”正式定义
- 第五色需求指标 / Fifth-Color Demand Indicator: papers/PAPER.md 第 1.2 节首次记号出现；第 2.3 节“第五色需求”集中说明
- 部分 4-着色 / Partial 4-Coloring: papers/PAPER.md 第 1.2 节首次记号出现；第 2.2 节“颜色需求”与第 2.3 节“第五色需求”进入正式语境
- 着色状态空间 / Coloring State Space: papers/PAPER.md 第 1 节“引言”概念性出现；第 2.4 节“着色状态空间”正式定义
- 阻碍传播图 / Obstruction Propagation Graph: papers/PAPER.md 第 1.2 节首次记号出现；第 4.1 节“阻碍传播”集中说明
- 第五色核心 / Fifth-Color Core: papers/PAPER.md 第 4.2 节“第五色核心”
- 持续第五色需求 / Persistent Fifth-Color Demand: papers/PAPER.md 第 2.7 节“持续第五色需求”
- 允许局部变换 / Allowed Local Transformation: papers/PAPER.md 第 2.4 节“允许局部变换族”
- 可达状态邻域 / Reachable State Neighborhood: papers/PAPER.md 第 2.4 节“可达状态邻域”
- 冻结球 / Frozen Ball: papers/PAPER.md 第 2.4 节“冻结球”
- 持续需求核 / Persistent Demand Core: papers/PAPER.md 第 2.7 节“持续第五色需求”
- 最小消除步长 / Minimal Elimination Length: papers/PAPER.md 第 2.8 节“最小消除步长”
- 局部可消除性 / Local Eliminability: papers/PAPER.md 第 2.8 节“局部可消除性”
- 需求传播 / Demand Propagation: papers/PAPER.md 第 3 节“研究动机与结构转向”；第 4.1 节“阻碍传播”
- 双核共存 / Dual-Core Coexistence: papers/PAPER.md 第 3 节“研究动机与结构转向”首次提出；第 6.2 节“该命题为何合理”进入中心论证语境
- 需求见证子图 / Demand Witness Subgraph: papers/PAPER.md 第 6.7 节“第二步的起点：双核结构化引理”
- 双核连接体 / Double-Core Connector: papers/PAPER.md 第 6.7 节“第二步的起点：双核结构化引理”
- 平面压缩约束 / Planar Compression Constraint: papers/PAPER.md 第 6.8 节“第三步：平面排除引理”
- 有限构型族 / Finite Configuration Family: papers/PAPER.md 第 6.9 节“第四步：有限构型压缩命题”
- 唯一性主张 / Uniqueness Claim: papers/PAPER.md 第 6.1 节“中心命题”；第 6.3 节“当前逻辑地位”
- 理论框架 / Framework: papers/PAPER.md 第 1.1 节“文稿定位与仓库对应关系”
- 论文主稿 / Research Paper: papers/PAPER.md 第 1.1 节“文稿定位与仓库对应关系”
- 路线图 / Roadmap: papers/PAPER.md 第 1.1 节“文稿定位与仓库对应关系”
- 研究日志 / Research Log: papers/PAPER.md 第 1.1 节“文稿定位与仓库对应关系”

---

## 8. 扩写待办

1. 为每个核心术语补充首次出现位置与对应文档链接。
2. 区分“正式定义术语”和“工作性术语”。
3. 补充与 Volume2、Volume3 相关的新术语槽位。
4. 与 docs/Notation.md 建立交叉索引，避免术语与记号脱节。
