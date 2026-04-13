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

## 当前核心结论

### 1. 1-loop anomaly 的核心来自局域项，不来自 naive ordinary triangle

当前材料表明，ordinary triangle 的 `q\to0` 极限本身通常不给 anomaly。

真正留下有限系数的是

$$
t^0(\text{diagram})
\;-\;
\text{classical collapse}
$$

之后的 evanescent local term。

### 2. `Q_1(f_{++}\bar\lambda_{\dot\alpha})` 已给出稳定基准

这个基准算例已经在 DR 与 PV 两种正规化下给出一致的 1-loop local anomaly，最紧凑写法是

$$
\mathcal I\!\left[
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}(p)
\right]
=
-\frac{g^2}{16\pi^2}\,
p_{+\dot\beta}\,
\mathscr B(p),
$$

等价地

$$
\mathcal O_{\dot\beta}^{(1)\,\mathrm{loc}}(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\mathscr B(x).
$$

### 3. Konishi anomaly 已并入同一工作流

对一般 `N=1` chiral matter 的基础算例

$$
K_+(p)=\frac{1}{\sqrt2}\int_k \psi_+(k)\phi^\dagger(p-k),
$$

当前已经按同一套 `Q_{\mathrm{bare}}-Q_0` / local term extraction 工作流改写成 current-diagram 形式，并得到

$$
Q_-^{\mathrm{Loop}}
\left(\frac{1}{\sqrt2}\psi_+\phi^\dagger\right)(p)
=
\frac{g^2}{16\pi^2}\,\bar\lambda^2(p).
$$

其 anomaly 来自

$$
t^0(T_1+T_2)
\;-\;
\text{classical / formal-4d collapse},
$$

而不是 ordinary triangle 的 naive `q\to0`。

### 4. `Q_1(f_{++}f_{++})` 与更高导数算例仍保持局域

当前已有的

- `Q_1(f_{++}f_{++})`
- `Q_1(f_{++}\nabla_{+\dot\gamma}\bar\lambda_{\dot\alpha})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})f_{++})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})\bar\lambda_{\dot\beta})`
- `Q_1((\nabla_{+\dot\alpha}f_{++})\nabla_{+\dot\beta}\bar\lambda_{\dot\gamma})`

都支持同一个判断：1-loop anomaly 的最终结果仍是 local operator。

其中单迹形式的一个干净例子是

$$
Q_1\,\operatorname{Tr}(f_{++}f_{++})(x)
=
\frac{g^2}{16\pi^2}\,
i\partial_{+\dot\beta}\operatorname{Tr}\big(f_{++}\widetilde\lambda^{\dot\beta}\big)(x).
$$

### 5. 生成函数统一了一串带导数算符

对

- `Q_1(f_{++}e^{w\cdot\nabla}f_{++})`
- `Q_1(e^{w\cdot\nabla}f_{++}f_{++})`
- `Q_1(f_{++}e^{w\cdot\nabla}\bar\lambda_{\dot\beta})`

已经得到 compact generating kernels。

`w=0` 与 `O(w)` 展开会退化回已经单独算过的低导数结果。

## 当前文件分工

- `theory/`：按理论分桶放背景输入；
- `theory/n1_sym_euclidean/`：`N=1 SYM (Euclidean)` 的 component 输入；
- `theory/n1_general/`：一般 `N=1` component 理论；
- `theory/n4_sym/`：`N=4 SYM` 的 component 输入；
- `theory/superspace_approach/`：独立的 superspace 公式体系；
- `calculation example/n1_sym_euclidean/`：`N=1 SYM (Euclidean)` 显式算例；
- `calculation example/n1_general/`：一般 `N=1` 理论显式算例，当前已加入 Konishi anomaly 的 DR current-diagram 版本；
- `calculation example/n4_sym/`：`N=4 SYM` 显式算例；
- `source_archive/`：完整原始材料。

## 下一步最自然的延伸

- 把现有仍保留 PV 的 component 计算逐步重写成 DR / DRED-style；
- 用同一套 current-diagram 口径继续做更一般的 `N=1` matter / superpotential 算符；
- 在 superspace approach 里建立与 component Ward-identity 计算相容的 supergraph 版本。
