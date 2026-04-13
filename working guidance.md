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

### Step 4: DR integral

对 Step 3 剩下的 evanescent local term 施加 DR / DRED-style 计算，完成极限并得到有限局域系数。

### Step 5: Final local anomaly

写出最终的 momentum-space local term、`q\to0` 极限下的 `Q^{\mathrm{Loop}}O`、以及对应的 local operator form。

### Step 6: Simplification examples

这一步可选。

仅当当前算例额外做了 single-trace、特定表示、特定群论化简、或其他非主结果所必需的化简时，才把这些内容放入这一步。

## 旧文件说明

旧的 component-style 计算页里仍可能保留“先写 raw SUSY，再减 classical SUSY”的老编号。

后续新写或重写的文件，统一优先采用上面的 `current / Ward identity / local term extraction` 版本。

## 原始材料

未经整理的总笔记、原始图、旧尝试版本，继续保留在 `source_archive/`。
