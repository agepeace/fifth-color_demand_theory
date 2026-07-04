# Bibliography

## 文档说明

本文件用于维护 Fifth-Color Demand Theory（FCD Theory）研究所依赖的核心参考文献，并为后续论文写作提供统一引用入口。

当前阶段的目标不是穷尽所有相关文献，而是先建立一套可持续扩写的参考文献骨架，使经典四色理论、一般图着色理论以及 FCD Theory 自身的文献位置彼此区分清楚。

---

## 1. 引用原则

1. 经典结论优先引用原始文献或公认标准版本。
2. 教材类文献用于统一术语、记号和背景叙述，不替代原始论文引用。
3. FCD Theory 自定义对象的正式表述，应优先回链到本仓库中的框架文档与论文主稿。
4. 参考文献条目后续应逐步补齐出版信息、页码、版本与可核查说明。

---

## 2. 经典四色理论

### 2.1 历史起点

- Kempe, A. B. 1879. "On the Geographical Problem of the Four Colours." American Journal of Mathematics 2 (3): 193-200.
  用途：四色问题历史起点，Kempe 链方法来源。

- Heawood, P. J. 1890. "Map-Colour Theorem." Quarterly Journal of Pure and Applied Mathematics 24: 332-338.
  用途：指出 Kempe 证明中的缺陷，并推动后续严格化工作。

### 2.2 计算机辅助证明阶段

- Appel, K., and W. Haken. 1977. "Every Planar Map Is Four Colorable. Part I: Discharging." Illinois Journal of Mathematics 21 (3): 429-490.
  用途：四色定理首个计算机辅助证明的主体文献之一。

- Appel, K., W. Haken, and J. Koch. 1977. "Every Planar Map Is Four Colorable. Part II: Reducibility." Illinois Journal of Mathematics 21 (3): 491-567.
  用途：与 Part I 配套，构成经典计算机辅助证明的完整叙述。

- Robertson, N., D. P. Sanders, P. Seymour, and R. Thomas. 1997. "The Four-Colour Theorem." Journal of Combinatorial Theory, Series B 70 (1): 2-44.
  用途：后续更系统的四色定理证明版本，是现代叙述中的关键参考。

---

## 3. 一般图着色理论

### 3.1 标准教材与综述

- Diestel, R. 2017. Graph Theory. 5th ed. Berlin: Springer.
  用途：图论基础、平面图基本性质、标准术语与记号来源。

- West, D. B. 2001. Introduction to Graph Theory. 2nd ed. Upper Saddle River, NJ: Prentice Hall.
  用途：图着色、平面图、基础结构论的标准教学参考。

- Jensen, T. R., and B. Toft. 1995. Graph Coloring Problems. New York: Wiley-Interscience.
  用途：一般图着色问题、变体与技术谱系的系统背景。

- Thomassen, C. 2003. "Graph Coloring Problems on Surfaces." Journal of Combinatorial Theory, Series B 88 (1): 1-18.
  用途：曲面与平面图着色、围长约束和结构性可着色结果的综述入口。

### 3.2 本节后续扩写方向

1. 补充平面图着色、列表着色、边着色与全着色的代表性文献。
2. 补充与围长、最大平均度、局部结构约束有关的经典结果。
3. 补充与可约构型、不可避免集、卸载法有关的专题综述。

---

## 4. FCD Theory 直接关联文档

### 4.1 仓库内核心文档

1. Volume1/Fifth-Color_Demand_Theory_Framework.md
	用途：FCD Theory 的理论框架、核心对象与中心命题定位。

2. papers/PAPER.md
	用途：当前论文主稿，集中给出定义系统、双语关键命题与证明路线草案。

3. ROADMAP.md
	用途：从定义、结构理论到定理化推进的阶段路线。

### 4.2 后续应补的内部文献化对象

1. 术语版本记录：跟踪 glossary 与 notation 的正式冻结版本。
2. 引理链索引：记录未来 Volume2 中每条关键引理的首次出现位置。
3. 图示索引：记录 figures 中每个示意图与主文档章节的对应关系。

---

## 5. 主题化引用槽位

### 5.1 不可避免构型与不可避免集

- Appel, K., and W. Haken. 1977. "Every Planar Map Is Four Colorable. Part I: Discharging." Illinois Journal of Mathematics 21 (3): 429-490.
  用途：不可避免集与卸载法在四色证明中的标准起点之一。

- Appel, K., W. Haken, and J. Koch. 1977. "Every Planar Map Is Four Colorable. Part II: Reducibility." Illinois Journal of Mathematics 21 (3): 491-567.
  用途：可约构型分类与不可避免集配对使用的标准参考。

- Robertson, N., D. P. Sanders, P. Seymour, and R. Thomas. 1997. "The Four-Colour Theorem." Journal of Combinatorial Theory, Series B 70 (1): 2-44.
  用途：现代四色证明中不可避免集与可约性框架的精炼版本。

### 5.2 围长、局部结构与 3-正则平面图

- Borodin, O. V., A. O. Ivanova, M. Montassier, P. Ochem, and A. Raspaud. 2005. "Acyclic Coloring of Planar Graphs with Girth at Least 5." SIAM Journal on Discrete Mathematics 19 (4): 1000-1013.
  用途：高围长平面图在局部结构压缩和着色约束上的代表性专题文献。

- Borodin, O. V., and A. N. Glebov. 2006. "On the Structure of Plane Graphs with Prescribed Girth and Bounded Degree." Diskretny Analiz i Issledovanie Operatsii 13 (1): 3-15.
  用途：围长与有界度共同作用下的平面图局部结构约束参考。

- Thomassen, C. 1994. "Every Planar Graph Is 5-Choosable." Journal of Combinatorial Theory, Series B 62 (1): 180-181.
  用途：平面图着色中局部可扩张与结构约束方法的经典参考，可作为高围长讨论的邻近背景。

### 5.3 Kempe 链与局部重着色

待补内容：

1. Kempe 链方法的原始来源与后续修正讨论。
2. 局部重着色在现代图着色中的标准用法。
3. 可作为“局部可消除性”背景支撑的代表性文献。

### 5.4 卸载法与平面局部结构分析

- Appel, K., and W. Haken. 1977. "Every Planar Map Is Four Colorable. Part I: Discharging." Illinois Journal of Mathematics 21 (3): 429-490.
  用途：卸载法进入现代四色证明的经典文献。

- Borodin, O. V. 1976. "On Decomposition of Plane Graphs into Boundary Chains." Siberian Mathematical Journal 17 (6): 826-833.
  用途：平面图局部结构与卸载分析传统中的早期代表性工作。

- Steinberg, R. 1993. "The State of the Three Color Problem." In Quo Vadis, Graph Theory?, edited by J. Gimbel, J. W. Kennedy, and L. V. Quintas, 211-248. Annals of Discrete Mathematics 55. Amsterdam: North-Holland.
  用途：卸载法、局部构型与平面图着色问题之间关系的专题综述入口。

---

## 6. 当前建议引用集

若当前就需要形成论文中的“基础参考文献”小节，可优先保留以下条目：

- Kempe 1879
- Heawood 1890
- Appel and Haken 1977, Part I
- Appel, Haken, and Koch 1977, Part II
- Robertson, Sanders, Seymour, and Thomas 1997
- Diestel, Graph Theory
- Jensen and Toft, Graph Coloring Problems
- West, Introduction to Graph Theory

---

## 7. 编目待办

1. 继续核对新补专题文献的版次、页码与期刊信息。
2. 为论文主稿中的每一处经典结论补上对应引用位置。
3. 视正文需要补入列表着色、临界图与算法着色方向的代表性条目。
4. 将本文件与 docs/Glossary.md、docs/Notation.md 交叉链接，形成文献-术语-记号的闭环。
