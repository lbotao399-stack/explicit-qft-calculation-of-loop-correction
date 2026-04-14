# main working flow and result

## 工作对象

当前 project 的核心对象不是 ordinary classical SUSY 变换，而是组合算符在量子修正下的非莱布尼兹部分：

$$
Q^{\mathrm{Loop}}O:=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

这里

- `Q(O)_{bare}`：不模去运动方程的 raw SUSY 变换；
- `Q_0(O)`：对应的 classical / onshell SUSY 项。

当前的规范实现已经切到：

- 用 SUSY current insertion 建立 Ward identity；
- 在含 current 动量 `q` 的图里抽取局域项；
- 把 classical / formal-4d collapse 视为 `Q_0`；
- 把 subtraction 后留下的 evanescent local term 视为 `Q_{\mathrm{bare}}-Q_0`。

## 标准工作流

### 0. 固定理论输入

- 记号与几何背景；
- 费曼规则；
- SUSY current 与 Ward identity；
- raw SUSY 与 classical / onshell 项的对应关系；
- BPS letters 与所选超荷。

### 1. 选定算符与 current insertion

引入带总动量 `p` 的外线算符 `O(p)`，并引入带动量 `q` 的 SUSY current insertion。

ordinary triangle 振幅先保留 `q\neq0`。

不能把 anomaly 直接从 naive `q\to0` 的 ordinary triangle 读出来。

### 2. 用 Ward identity 实现 `Q_{\mathrm{bare}}-Q_0`

概念定义仍是

$$
Q^{\mathrm{Loop}}O=Q(O)_{\mathrm{bare}}-Q_0(O),
$$

但计算上统一改写成

$$
\text{local Taylor part}
\;-\;
\text{classical / formal-4d collapse}.
$$

### 3. 只保留 connected anomaly diagrams

在给定 loop level，只保留真正进入 anomaly sector 的 connected 图。

当前 1-loop 情形最常见的是 current insertion、operator insertion 与一个 interaction vertex 组成的三角图。

### 4. 用 DR / DRED-style 抽取 evanescent local term

对发散子图做 `t^0` Taylor subtraction，并保留 subtraction 后的 evanescent local term，例如

$$
\frac{\widehat k^2}{(k^2)^3}.
$$

后续主线统一采用 DR / DRED-style。

在这个口径下，有限 anomaly 系数来自

$$
\widehat k^2\times \Gamma(\epsilon).
$$

### 5. 取 `q\to0` 并识别为 local operator

先得到含 `q` 的局域 Ward 振幅，再取 `q\to0`，读出

$$
Q_-^{\mathrm{Loop}}O(p),
$$

最后改写成 position-space 的 local operator。

## 当前固定原则

### 1. anomaly 只从局域项读取

ordinary triangle 的 naive `q\to0` 极限不作为 anomaly 的定义。

工作上只保留

$$
t^0(\text{diagram})
\;-\;
\text{classical / formal-4d collapse}
$$

之后留下的局域项。

### 2. current insertion 是统一入口

后续 calculation 若重新建立，统一从

$$
\partial_\mu J^\mu
$$

的 Ward identity 插入出发，而不再回到旧的“逐字母 raw 代入”主线。

### 3. component track 与 superspace track 分开

- component current-diagram track：作为 coefficient 与 local basis 的 source of truth
- superspace track：只做 dictionary 与 bookkeeping，不回写 component divergence pages

## 当前文件分工

- `theory/`：按理论分桶放背景输入；
- `theory/n1_sym_euclidean/`：`N=1 SYM (Euclidean)` 的 component 输入；
- `theory/n1_general/`：一般 `N=1` component 理论；
- `theory/n4_sym/`：`N=4 SYM` 的 component 输入；
- `theory/n4_ordinary_space/`：`N=4 SYM` 在 ordinary-space AWI 路线下的 no-derivative bi-letter kernel master pages；
- `theory/superspace_approach/`：独立的 superspace 公式体系；

## 当前双轨组织

- component current-diagram track
  - source of truth：`theory/n1_sym_euclidean/component_diagram_master_targets.md`
  - frozen convention：`Q_1\equiv Q_-`, `\kappa_A=i/2`, `\partial_\mu J_-^\mu` 只作 WT insertion
  - diagram pages 只负责把局域短程项重组回 explicit classical target
- superspace track
  - 只做 operator dictionary 与 anomaly multiplet bookkeeping
  - 不把 superspace anomaly equation 直接回写到 component divergence pages

## 后续重建原则

- 若重新建立 calculation pages，先固定 operator、classical target、local basis 与 relevant current branches。
- 具体积分与正规化只在 theory / workflow 已冻结后再写。
- 所有新 calculation 文档都应被视为可重建产物，而不是当前仓库的 source of truth。
