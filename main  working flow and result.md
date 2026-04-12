# main working flow and result

## 工作对象

当前 project 的核心对象不是普通的 classical SUSY 变换，而是组合算符在量子修正下的非莱布尼兹部分，也就是广义的 anomaly：

$$
Q^{\mathrm{Loop}}O:=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

这里

- `Q(O)_{bare}`：对组合算符的每个 letter 代入不模去运动方程的 raw SUSY 变换；
- `Q_0(O)`：再对上式代入 EOM 后得到的完全 classical / onshell SUSY 变换。

因此，全部显式计算都在回答同一个问题：这些看似只是“正规化 delta 函数”的差，在 loop level 到底给出什么局域量子修正。

## 标准工作流

下面这五步是当前 project 的主线，不只是一个粗略摘要，而是后续继续扩展到别的 SUSY 理论、别的算符、乃至更高 loop 时都应保持不变的基本算法框架。

### 0. 先固定理论输入

每次开始一个新计算，先固定：

- 记号与几何背景，目前默认是 Euclidean gauge theory；
- 费曼规则；
- 超对称变换规则，而且要明确区分：
  - 不模去运动方程的 raw SUSY 变换；
  - 模去运动方程的 onshell / classical SUSY 变换；
- BPS letters，与所选超荷，当前通常取 `Q_-`。

本项目的核心不是 onshell 后的简化结果，而是不模 EOM 的 raw 变换，因为真正的 loop anomaly 就埋在这一步与 EOM 之间的差里。

### 1. 在动量空间选定研究对象

引入一个带总注入动量 `p` 的外线组合算符 `O(p)`，把它作为当前要研究的对象。

这里的 `O` 可以是两字母算符、带导数字母的算符，或者生成函数形式的算符，但都统一看成一个带总动量注入的 composite insertion。

### 2. 先定义出真正要算的 `Q^{Loop}O`

把选定的 supercharge `Q_-` 直接按莱布尼兹律作用在 `O` 上，对 `O` 中每个 letter 代入不模去运动方程的 SUSY 变换，得到

$$
Q(O)_{\mathrm{bare}}.
$$

然后再把 `Q(O)_{\mathrm{bare}}` 中的相关部分代入运动方程，也就是改用完全 onshell 的 classical SUSY，定义

$$
Q_0(O).
$$

于是把真正要研究的量定义为

$$
Q^{\mathrm{Loop}}O:=Q(O)_{\mathrm{bare}}-Q_0(O).
$$

这一步是整个项目最关键的定义。naively 看，二者似乎只差一些平凡的正规化 delta 函数；但 loop level 的显式计算表明，这些差并不平凡，而会生成有物理内容的广义 anomaly。

### 3. 用费曼规则生成 `Q^{Loop}O` 的 connected 图

在给定 loop level，把 `Q^{\mathrm{Loop}}O` 与若干相互作用顶点做 Wick contraction。这里各个相互作用顶点都视为总注入动量为零的组合算符 `V_{\mathrm{int}}`。

Wick contraction 之后：

- 被 contract 的 letters 进入传播子与 loop；
- 没有被 contract 的 letters 作为结果的外腿保留下来。

当前 1-loop 材料中，connected 图的核心形态就是两个顶点构成的三角图。实际计算时又自然分成：

- EOM / contact sector；
- anomalous triangle sector；
- 对具体外腿排序再分成 pattern 12 与 pattern 21。

### 4. 选定正规化并完成动量积分

在动量空间上完成 loop 积分，并用正规化把局域项抽出来。

当前材料里已有两套记录：

- Pauli-Villars regularization；
- dimensional regularization。

后续准备统一采用 dimensional regularization；但从现有结果看，PV 与 DR 在核心局域 anomaly 系数上是一致的。真正重要的不是 formal collapse 本身，而是受正规化控制后留下来的 finite local term。

### 5. 把结果识别为 local operator

最终目标不是只停在某个动量积分表达式，而是把答案重写成局域组合算符，也就是 `Q^{\mathrm{Loop}}O` 的 local operator 形式。

当前已有算例表明，这一点是成立的：最终系数都是外动量的多项式，因此回到 position space 后就是某个局域 operator 的导数或 covariantized 导数表达式。这也正是把这些量理解为广义 anomaly 的关键原因。

## 当前材料的核心结论

### 1. 1-loop 图的物理分类已经比较清楚

在当前例子中，`EOM/contact` 部分负责 formal 4d collapse、树级抵消或 covariant completion；真正给出 anomaly 系数的是 anomalous triangle sector。

对 DR 来说，有限局域项来自 evanescent numerator 与 UV pole 的配合；对 PV 来说，同一个局域系数由 regulated triangle 直接抽出。

### 2. 基准算例 `Q_1(f_{++}\bar\lambda_{\dot\alpha})` 已得到稳定答案

这个算例已经做了多次尝试，最终以：

- 第三次 DR 计算；
- 第四次 PV 计算

给出同一个 1-loop local anomaly。其最紧凑的动量空间写法是

$$
\mathcal I\!\left[
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}(p)
\right]
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B(p),
$$

等价地，position-space 写成

$$
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\mathscr B(x).
$$

这说明 loop correction 确实不是“纯平凡的 delta 函数差”，而是一个有内容的局域量子修正。

### 3. 更高导数例子仍然保持局域

当前材料中的

- `Q_1(f_{++}f_{++})`
- `Q_1(f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})f_{++})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma})`

都支持同一个结构判断：1-loop anomaly 的结果仍是 local operator。

其中一个最干净的单迹例子是

$$
Q_1\,\mathrm{Tr}(f_{++}f_{++})(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\mathrm{Tr}\big(f_{++}\bar\lambda^{\dot\beta}\big)(x),
$$

并且在 1-loop 精度下可以直接做 covariantization。

### 4. 生成函数把整串导数例子统一起来了

对

- `Q_1(f_{++}e^{w\cdot\nabla}f_{++})`
- `Q_1(e^{w\cdot\nabla}f_{++}f_{++})`
- `Q_1(f_{++}e^{w\cdot\nabla}\bar\lambda_{\dot\beta})`

已经得到 exact compact kernel 的写法。`w=0` 与 `O(w)` 展开会分别退化回前面已经单独算过的低导数结果，所以这些 generating kernels 不是新猜想，而是对已知算例的统一打包。

## 目前的文件分工

- `theory/`：按理论分桶放背景输入；
- `theory/n1_sym_euclidean/`：纯 `N=1 SYM (Euclidean)` 的记号、raw SUSY、BPS letters、Feynman rules；
- `theory/n1_general/`：一般 `N=1` 理论的 matter、superpotential、general SUSY 与 BPS 数据；
- `theory/n4_sym/`：`N=4 SYM` 的作用量、SUSY、BPS letters 与 Feynman rules；
- `calculation example/n1_sym_euclidean/`：当前全部 `N=1 SYM (Euclidean)` 显式算例，且每个文件都带有 theory / regularization / operator 属性；
- `calculation example/archive/grouped_archive/`：旧的主题打包稿；
- `source_archive/`：完整原始材料，不参与重写。

## 下一步最自然的延伸

- 把当前仍保留 PV 的部分，按现有图分类统一改写成 DR；
- 在不改变主流程的前提下，替换不同理论的 SUSY 规则与 BPS letters；
- 往更高 loop level 继续沿用“raw SUSY -> connected graphs -> regularized local term”的同一算法框架。
