# working guidance

这份文件不是结果汇总，而是这个 project 后续继续推进时应遵守的工作指导。

## 核心定义

$$
Q^{\mathrm{Loop}}O:=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

`Q(O)_{bare}` 是不模去运动方程的 raw SUSY 变换，`Q_0(O)` 是对应的 classical / onshell 项。

当前 project 的规范实现不再直接从“raw letter 逐项代入”出发，而统一改成：

- 用 SUSY current insertion 写 Ward identity；
- 在含 current 动量 `q` 的振幅里抽取局域项；
- 用 classical / formal-4d collapse 代表 `Q_0`；
- 用 `t^0` Taylor subtraction 之后留下的 evanescent local term 代表 `Q_{\mathrm{bare}}-Q_0`。

因此，`Q^{\mathrm{Loop}}O` 的实际计算口径统一写成 `susy current diagram / anomaly Ward identity`。

## 理论输入

所有跨理论的统一记号先写入 `theory/unified_notation.md`。

所有理论特有的内容继续放在：

- `theory/n1_sym_euclidean/`
- `theory/n1_general/`
- `theory/n4_sym/`
- `theory/superspace_approach/`

## 计算文档格式

所有具体计算继续放在 `calculation example/`，并先按理论分桶。

每个具体计算文件的标题统一采用：

- `Q_1(O)（算符内容） / DR`
- `Q_1(O)（算符内容） / PV`

每个文件保留 front matter，至少包含：

- `doc_type`
- `theory`
- `regularization`
- `supercharge`
- `loop_order`
- `operator`

每个计算子页的正文只保留：

- `Step N: title`
- 公式
- 图片

除 `Step N: title` 之外，不再添加解释性文字。

## 标准 Step 模板

### Step 1: Operator / current / vertex

写出待研究的外线算符 `O(p)`、SUSY current 或其 divergence、相关 interaction vertex、传播子、以及当前正规化约定。

### Step 2: Wick contraction

写出 current insertion 与 operator insertion 的相关 contraction。

这一步只保留真正进入 anomaly sector 的图与其振幅表达式。

### Step 3: Local part = Taylor subtraction

对发散子图做 `t^0` 局域抽取。

`Q_{\mathrm{bare}}-Q_0` 的差在这里实现为：

$$
\text{local Taylor part}
\;-\;
\text{classical / formal-4d collapse}.
$$

### Step 4: Regularization and final local anomaly

对 Step 3 剩下的局域项施加当前所用正规化并完成积分。

主线优先采用 DR / DRED-style；历史文件若仍保留 PV，则在同一步写出对应的 regulated local extraction。

### Step 5: Simplification examples

写出 single-trace、特定表示、特定群论化简、或其他非主结果所必需的化简。

## 旧文件说明

旧的 component-style 计算页里仍可能保留“先写 raw SUSY，再减 classical SUSY”的老编号。

后续新写或重写的文件，统一优先采用上面的 `current / Ward identity / local term extraction` 版本。

## Current-divergence implementation rules

1. 保持 `q\neq0`，直到 local Taylor subtraction 被明确写出。
2. 不从 ordinary triangle 的 naive `q\to0` 极限直接读取 anomaly。
3. anomaly sector 统一写成

$$
t^0(\text{relevant contractions})
\;-\;
\Gamma_{\rm cl}.
$$

4. 在 DR / DRED-style 中，有限 anomaly 系数来自 `\widehat k^2\times \Gamma(\epsilon)`。
5. 每个具体算例只保留真正相关的 supercurrent / current-divergence 分量。
6. 对 1-loop local coefficient，无关的 improvement terms 可以省略。

## N=1 SYM 当前工作约定

对 `n1_sym_euclidean`，当前统一采用 gauge-invariant FZ / Belinfante supercurrent。

若 `conventions_and_rules.md` 中

$$
\delta\lambda_\alpha=c_f\,f_{\alpha\beta}\,\varepsilon^\beta+\cdots,
$$

则 current 的 relevant piece 固定为

$$
J_{\mu\alpha}^{(f\bar\lambda)}
=
c_f\,f_{\alpha\beta}(\sigma_\mu)^{\beta\dot\beta}\bar\lambda_{\dot\beta}.
$$

对具体 supercharge `Q_1`，工作投影统一写成

$$
J^\mu_{Q_1}:=v_{Q_1}^\alpha J^\mu_\alpha,
\qquad
\partial_\mu J^\mu_{Q_1}\ \text{as the insertion}.
$$

在 diagrammatics 中，必须同时保留

$$
J^{(2)}\sim (\partial A)\bar\lambda,
\qquad
J^{(3)}\sim [A,A]\bar\lambda.
$$

对 `Q_1(f_{++}f_{++})` 及其同族页面，不把

$$
X_{\rm gf}+X_{c\bar c},
\qquad
X_{\rm Fierz},
\qquad
\partial^\nu U_{\nu\mu\alpha},
\qquad
\bar J_{\mu\dot\alpha},
\qquad
D\text{-piece}
$$

作为独立 anomaly-channel insertion。

## 原始材料

未经整理的总笔记、原始图、旧尝试版本，继续保留在 `source_archive/`。
