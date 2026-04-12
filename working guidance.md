# working guidance

这份文件不是结果汇总，而是这个 project 后续继续推进时应遵守的工作指导。

## 核心定义

$$
Q^{\mathrm{Loop}}O:=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

`Q(O)_{bare}` 是对组合算符每个 letter 代入不模去运动方程的 raw SUSY 变换，`Q_0(O)` 是再代入 EOM 后得到的完全 onshell / classical SUSY 变换。

## 理论输入

所有跨理论的统一记号先写入 `theory/unified_notation.md`。

所有理论特有的内容继续放在：

- `theory/n1_sym_euclidean/`
- `theory/n1_general/`
- `theory/n4_sym/`

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

### Step 1: Operator set up

在动量空间引入含总动量 `p` 的外线算符 `O(p)`，并直接写出它的 momentum-space form。

### Step 2: Act supercharge Q on O (off-shell)

默认选定 `Q_-`，按莱布尼兹律作用到 `O` 上，并代入不模去运动方程的 SUSY 变换，得到

$$
Q(O)_{\mathrm{bare}}.
$$

### Step 3: Subtracting tree level Q

写出

$$
Q^{\mathrm{Loop}}O=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

若 tree level `Q_0(O)=0`，则直接写成同一步骤中的最终式。

### Step 4: All related Feynman Diagrams (Wick contractions) at this order

只放该阶所有相关 Wick contraction 图。

当前可以暂时使用占位图；后续统一替换成更好的规范绘图。

### Step 5: Estimate the Feynman Diagrams

只写图对应的 Wick contraction、传播子、顶点、内部动量分配、以及由费曼规则得到的表达式。

### Step 6: Do the regularization and Estimate the ultimate result

从 Step 5 的表达式出发施加正规化并完成积分，写出最终 momentum-space result 与 local operator result。

后续统一目标是 DR；但对尚未重算的历史文件，先保留其原正规化并按同一 Step 模板整理。

### Step 7: Simplification examples

这一步可选。

仅当当前算例额外做了 single-trace、特定表示、特定群论化简、或其他非主结果所必需的化简时，才把这些内容放入 Step 7。

## 原始材料

未经整理的总笔记、原始图、旧尝试版本，继续保留在 `source_archive/`。
