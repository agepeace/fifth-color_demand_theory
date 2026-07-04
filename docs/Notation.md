# Notation

## 文档说明

本文件用于统一 Fifth-Color Demand Theory（FCD Theory）当前使用的主要记号，作为论文主稿、框架文档与后续 Volume 文档之间的共享记号表。

当前目标是先建立一个稳定骨架：既覆盖已在 papers/PAPER.md 中出现的核心记号，也为后续结构引理、传播分析与分类结果预留扩展位置。

---

## 1. 记号使用原则

1. 同一对象尽量只保留一种主记号。
2. 新记号在进入论文主稿前，应先在本文件登记其含义。
3. 若某记号存在语境依赖，应明确写出定义域或使用条件。
4. 后续 Volume2、Volume3 中若引入大量新记号，应优先从本文件继续扩展，而不是各文档独立造表。

---

## 2. 图与基本集合记号

### $G$

目标平面地图或目标平面图。

### $V(G)$

图 $G$ 的顶点集。

### $E(G)$

图 $G$ 的边集。

### $u, v, w$

图中的顶点变量，通常表示局部讨论中的顶点。

### $uv$

连接顶点 $u$ 与 $v$ 的边，或表示二者相邻。

### $N(v)$

顶点 $v$ 的邻域。

---

## 3. 结构参数记号

### $g(G)$

图 $G$ 的围长。

### $\deg(v)$

顶点 $v$ 的度数。

### $\Delta(G)$

图 $G$ 的最大度数。

说明：当前论文主稿主要使用 3-正则条件，故该记号尚未成为主叙述对象，但建议保留为后续扩展接口。

---

## 4. 着色状态记号

### $\varphi$

一个部分 4-着色状态。

### $\psi$

与 $\varphi$ 对照的另一个部分 4-着色状态，常用于表示可达变换后的状态。

### $\{1,2,3,4\}$

当前研究中的基础颜色集合。

### $D(v,\varphi)$

顶点 $v$ 在着色状态 $\varphi$ 下的可用颜色集。

定义回顾：

$$
D(v,\varphi)=\{1,2,3,4\}\setminus \{\varphi(u):u\in N(v),\ \varphi(u)\text{ 已定义}\}.
$$

### $F(v,\varphi)$

顶点 $v$ 在状态 $\varphi$ 下的第五色需求指标函数。

约定：

$$
F(v,\varphi)=
\begin{cases}
1, & D(v,\varphi)=\varnothing,\\
0, & D(v,\varphi)\neq\varnothing.
\end{cases}
$$

---

## 5. 动态与传播相关记号

### $\mathcal{S}(G)$

图 $G$ 的着色状态空间。

### $\mathcal{P}(G)$

图 $G$ 的阻碍传播图。

### $u \to v$

表示在给定传播语境下，顶点 $u$ 的需求会结构性地迫使顶点 $v$ 延续某种阻碍状态。

说明：该箭头不是原图中的边，而是传播关系记号。

### $C_5(G)$

图 $G$ 的第五色核心，即在相关可达状态中持续体现第五色需求的顶点集合。

### $\Phi(\varphi)$

着色状态 $\varphi$ 的势函数，定义为

$$
\Phi(\varphi)=\sum_{v\in V(G)} F(v,\varphi).
$$

其作用是统计一个状态中的第五色需求总量，为后续单调性分析预留接口。

---

## 6. 命题与逻辑层级中的建议记号

以下记号尚未在当前论文主稿中完全固定，但建议提前预留：

### 命题 A / Proposition A

可用于标记当前中心研究命题的工作版本。

### $\mathfrak{C}$

可作为某类候选构型族的集合记号，用于后续不可避免构型分类。

### $\mathfrak{U}$

可作为不可避免集的候选集合记号。

### $\Gamma(v)$

若后续需要区分开邻域与传播邻域，可考虑将 $\Gamma(v)$ 用作传播语境下的局部关联集合。

说明：以上记号当前属于预留槽位，尚未在主稿中完全冻结。

---

## 7. 当前双语对照重点

1. available-color set 对应 $D(v,\varphi)$
2. fifth-color demand indicator 对应 $F(v,\varphi)$
3. coloring state space 对应 $\mathcal{S}(G)$
4. obstruction propagation graph 对应 $\mathcal{P}(G)$
5. fifth-color core 对应 $C_5(G)$
6. potential function 对应 $\Phi(\varphi)$

---

## 8. 首次出现章节索引

以下索引以 papers/PAPER.md 当前章节编号为准，用于快速定位各记号首次出现或首次集中解释的位置。

- $G$: papers/PAPER.md 第 1.2 节“记号约定”
- $V(G)$: papers/PAPER.md 第 1.2 节“记号约定”
- $E(G)$: papers/PAPER.md 第 1.2 节“记号约定”
- $N(v)$: papers/PAPER.md 第 1.2 节“记号约定”
- $g(G)$: papers/PAPER.md 第 1.2 节“记号约定”
- $\deg(v)$: papers/PAPER.md 第 1.2 节“记号约定”
- $\varphi$: papers/PAPER.md 第 1.2 节“记号约定”
- $D(v,\varphi)$: papers/PAPER.md 第 1.2 节“记号约定”首次出现；第 2.2 节“颜色需求”正式定义
- $F(v,\varphi)$: papers/PAPER.md 第 1.2 节“记号约定”首次出现；第 2.3 节“第五色需求”正式说明
- $\mathcal{S}(G)$: papers/PAPER.md 第 1.2 节“记号约定”首次出现；第 2.4 节“着色状态空间”正式定义
- $\mathcal{P}(G)$: papers/PAPER.md 第 1.2 节“记号约定”首次出现；第 4.1 节“阻碍传播”集中说明
- $u \to v$: papers/PAPER.md 第 4.1 节“阻碍传播”
- $C_5(G)$: papers/PAPER.md 第 4.2 节“第五色核心”
- $\Phi(\varphi)$: papers/PAPER.md 第 4.3 节“势函数”
- $\Delta(G)$: 当前主稿尚未正式使用，仅在本记号表中预留
- $\psi$: papers/PAPER.md 第 2.8 节“局部可消除性”
- $\mathfrak{C}$: 当前主稿尚未正式使用，仅在本记号表中预留
- $\mathfrak{U}$: 当前主稿尚未正式使用，仅在本记号表中预留
- $\Gamma(v)$: 当前主稿尚未正式使用，仅在本记号表中预留

---

## 9. 扩写待办

1. 将每个记号的首次出现章节写入索引。
2. 为未来引理链预留编号和引用格式。
3. 若后续引入面、嵌入或对偶图记号，应单列“平面嵌入记号”小节。
4. 与 docs/Glossary.md 交叉维护，确保术语与记号同步冻结。
