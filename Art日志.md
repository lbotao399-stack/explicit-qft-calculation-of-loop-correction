# Art日志

## 0. 目的

这份日志记录当前费曼图生成、压缩、渲染的讨论结果与工作准则。

目标不是普通散射振幅图，而是：

$$
Q_1(O)
$$

作为复合算符插入，允许：

- `O` 含任意多个 letters
- `O` 的一部分 letters 被 Wick contraction
- 剩余未 contraction 的 letters 作为新的外腿被 probe leg 接收
- slot 上可带缀饰，如 `\nabla`、`e^{w\cdot\nabla}`，但这些缀饰不改变图的拓扑构造

当前主要样例是：

$$
N=1\ {\rm SYM\ (Euclidean)},\qquad Q_1(f_{++}f_{++}).
$$

---

## 1. 对象建模

### 1.1 Operator insertion

把 `Q_1(O)` 视为一个单独的 insertion template。

例如对

$$
Q_1(f_{++}f_{++}),
$$

使用两个 ordered templates：

$$
O_{12}:\ \big(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\big),\,f_{++},
\qquad
O_{21}:\ f_{++},\,\big(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\big).
$$

`12` 与 `21` 永远不同，不做对称化。

### 1.2 Action vertices

每个作用量顶点用 typed template 表示。

当前 `N=1 SYM` 使用：

$$
V_{A\lambda\widetilde\lambda},\qquad
V_{AAA},\qquad
V_{AAAA},\qquad
V_{\bar c A c}.
$$

### 1.3 Slots

每个 vertex 的每条腿都是一个 slot。

slot 的基本属性：

- field species
- 所属 vertex
- 在 ordered vertex 中的位置
- 显示用 label

### 1.4 Probe legs

probe leg 的本质只是“接收剩余未 contraction 的算符”。

probe leg **没有顺序**。

因此图的外腿集合只记录 field multiset 与接到哪个 port，不应人为赋予 probe 次序。

### 1.5 Decorations

像

$$
\nabla_{+\dot\alpha}f_{++},\qquad
e^{w\cdot\nabla_+}f_{++},\qquad
e^{w\cdot\nabla_+}\!\left(i\nabla_{+\dot\alpha}\widetilde\lambda^{\dot\alpha}\right)
$$

这类缀饰，在图生成阶段只当作 slot decoration 保留。

准则是：

- decoration 不改变 slot 的 field species
- decoration 不改变可 contraction 的拓扑结构
- decoration 只在 amplitude 阶段变成 phase、外动量因子或 split-slot 微分算子

---

## 2. 枚举准则

### 2.1 传播子兼容性

当前只允许：

$$
A\text{-}A,\qquad
\lambda\text{-}\widetilde\lambda,\qquad
c\text{-}\bar c.
$$

### 2.2 不允许的 contraction

当前枚举默认排除：

- insertion 内部自收缩
- 同一个 action vertex 内部自收缩

### 2.3 连通性准则

最关键的一条：

`O` 这个方框不能当作“人工连通器”。

正确做法是：

1. 在实现中可以临时保留 `O`-core，便于存储 slot
2. 做 connectedness test 时，必须去掉 `O`-core 对各 slot 的人工 incidence
3. 视 `O` 的每个 letter 默认彼此隔断
4. 只保留整个图在此意义下 **完全连通** 的 Wick contraction

这一步去掉了大量假图。

### 2.4 群指标准则

若算符是 ordered 的，

$$
AB \neq BA.
$$

不能因为图形形状相似就把两个 ordered insertion 混为一类。

### 2.5 Loop 与 explicit coupling order

当前实现按固定 loop number 与 explicit coupling order 枚举。

对 `Q_1(f_{++}f_{++})` 的一圈局域 anomaly，当前扫描的是：

$$
g^2,\qquad g^3,\qquad g^4.
$$

其中：

- `g^2` 给 anomalous seed
- `g^3, g^4` 给 covariant completion 的前两层

---

## 3. 压缩准则

### 3.1 Raw Wick contractions

第一层输出是原始 Wick contraction。

这时仍区分：

- insertion term
- 具体 contraction 选择
- identical vertex copy 的标签
- identical gauge legs 的标签

### 3.2 Strict topological classes

第二层压缩成 strict topology classes。

当前保留：

- insertion term
- action vertex type multiset
- propagator species
- operator slot attachment
- external field species

当前忘掉：

- identical action-vertex copies 的标签
- `AAA` / `AAAA` 内完全相同 gauge legs 的标签

### 3.3 Mirror-reduced analytic families

进一步为解析使用，把 `12/21` 只在需要时合并成 mirror-reduced family。

这一层适合识别“真正的解析家族”。

---

## 4. 渲染准则

目标风格是 **FeynArts-inspired**，不是随手画占位符。

### 4.1 基本元件

- composite operator：方框 `QO`
- interaction vertex：黑实点
- gauge line：平滑波浪线
- fermion line：平滑实线 + 箭头
- ghost line：虚线 + 箭头

### 4.2 线条要求

- 不用折线拼接主线
- 主线采用 smooth Bézier curve
- 波浪线沿 Bézier 曲线法向起伏
- 箭头放在线中段，不压住顶点
- 标签带白底，避免遮住线

### 4.3 正确性要求

渲染必须按真实 representative topology 连边。

不能出现：

- gauge line 在图中“变成” fermion line
- 线段重合导致不可读
- 用错误的 species 画外腿

因此：

- external `A` 应画成 gauge line
- external `\widetilde\lambda` 应画成 fermion line
- 每一类 panel 应按真实代表元单独布局，而不是强行共用一个坏模板

---

## 5. 当前 N=1 SYM `Q_1(f_{++}f_{++})` 结果

### 5.1 一圈 fully connected 计数

raw Wick contractions：

$$
N_{\rm raw}(g^2)=20,\qquad
N_{\rm raw}(g^3)=348,\qquad
N_{\rm raw}(g^4)=9152.
$$

strict topological classes：

$$
N_{\rm top}(g^2)=6,\qquad
N_{\rm top}(g^3)=20,\qquad
N_{\rm top}(g^4)=66.
$$

### 5.2 `g^3` 的 mirror-reduced analytic families

共有 `10` 个 mirror-reduced families。

它们归并成四个解析 channel：

$$
\mathcal C_1=V_{AAA}\big(V_{A\lambda\widetilde\lambda}\big)^2,
$$

$$
\mathcal C_2=\big(V_{AAA}\big)^2V_{A\lambda\widetilde\lambda},
$$

$$
\mathcal C_3=V_{AAAA}V_{A\lambda\widetilde\lambda},
$$

$$
\mathcal C_4=\big(V_{A\lambda\widetilde\lambda}\big)^3.
$$

这些正是从 anomalous seed 走向 covariant completion 的第一层。

### 5.3 物理解释

对一圈 anomaly 来说：

- `g^2` 六个类给 universal anomalous seed
- `g^3`、`g^4` 不再引入新的 anomaly 系数
- 它们实现的是把 seed 从 `\partial` completion 补到 `\nabla` completion

---

## 6. 缀饰法则的当前版本

### 6.1 单边 generating rule

对

$$
\mathcal O_w^{AB}=f_{++}^A e^{w\cdot\nabla_+}f_{++}^B,
$$

当前得到的一圈 DR 局域结果是

$$
\Gamma_{12}(w)\propto
\int_\Delta
e^{\,i w\cdot(y p_1+(x+y)p_2)}
\big(y p_1+(x+y)p_2\big)_{+\dot\beta},
$$

$$
\Gamma_{21}(w)\propto
\int_\Delta
e^{\,i w\cdot((x+y)p_1+y p_2)}
\big((x+y)p_1+y p_2\big)_{+\dot\beta}.
$$

其 local operator form 是 split-slot differential rule：

$$
e^{\,w\cdot(y\nabla^{(1)}+(x+y)\nabla^{(2)})}
\big(y\nabla^{(1)}+(x+y)\nabla^{(2)}\big),
$$

$$
e^{\,w\cdot((x+y)\nabla^{(1)}+y\nabla^{(2)})}
\big((x+y)\nabla^{(1)}+y\nabla^{(2)}\big).
$$

这说明缀饰并不是单纯“把总动量 `p` 乘上去”，而是作用在两个 slot 上的加权协变微分生成子。

### 6.2 当前必须记录的 caution

旧 simplification 里曾出现

$$
Q_1(f_{++}\nabla f_{++})\stackrel{?}{=} i p\,Q_1(f_{++}f_{++}).
$$

这不能直接当成 anomaly 的 decoration law。

因为从 exact generating kernel 的线性项得到的是

$$
-\frac{i g^2}{96\pi^2}
\Big[
\Xi_{12}\mathscr F_{12}
\Xi_{21}\mathscr F_{21}
\Big],
$$

而不是简单的

$$
i p\times
\Big[
(p_1+2p_2)\mathscr F_{12}
+
(2p_1+p_2)\mathscr F_{21}
\Big].
$$

因此：

- exact generating kernel 优先
- simplification page 只能作为局部检验，不能反过来定义 decoration rule

---

## 7. 当前脚本与文件

### 7.1 枚举与压缩

- `tools/enumerate_n1sym_q1_fpp_fpp_1loop.py`
- `tools/feynarts_style_n1sym_generator.py`

### 7.2 渲染

- `tools/render_feynarts_style_n1sym_demo.py`

### 7.3 日志与结果

- `step4_enumeration_and_render_log.md`
- `assets/step4/n1_sym_euclidean/...`

---

## 8. 下一步建议

要把 `Q_1(ff)` 的缀饰法则完全搞明白，最自然的下一步是：

1. 写出双边生成元

$$
Q_1\!\left(e^{u\cdot\nabla_+}f_{++}\,e^{w\cdot\nabla_+}f_{++}\right)
$$

的 exact kernel

2. 从它统一推出

$$
Q_1(f_{++}\nabla_+ f_{++}),\qquad
Q_1(\nabla_+ f_{++}f_{++}),\qquad
Q_1(\nabla_+^2 f_{++}f_{++}),\ \dots
$$

3. 再回头统一修正旧的 `05/08/09` 三页，使它们全部服从同一套 generating rule

---

## 9. 一句话版本

当前图生成的核心准则是：

**把 `Q_1(O)` 看成带 ordered slots 的复合算符插入；去掉人工 `O`-core 后只保留完全连通图；probe leg 无序；decorations 保留到振幅阶段；一圈 anomaly 的新系数只来自 seed triangle，后续高一阶显式 `g` 图负责把它补成 split-slot 的协变缀饰法则。**
