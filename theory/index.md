# theory index

当前理论输入分成三层：

- 跨理论统一记号；
- component approach 下的各理论桶；
- superspace approach 下的独立理论桶。

## 统一记号

- `unified_notation.md`
  - 与理论无关的 spinor-vector、动量积分、delta 函数、Fourier 约定。

## Component approach

- `n1_sym_euclidean/`
  - 纯 `N=1 SYM (Euclidean)` 的记号、raw SUSY、BPS letters、Feynman rules，以及 current-divergence 工作约定。
- `n1_general/`
  - 一般 `N=1` component 理论，包含 chiral matter、superpotential、general SUSY 与 BPS 数据。
- `n4_sym/`
  - `N=4 SYM` 的作用量、SUSY、BPS letters 与 Feynman rules。
- `n4_ordinary_space/`
  - 当前 ordinary-space AWI 路线下的 `N=4 SYM` no-derivative bi-letter kernel master pages。

## Superspace approach

- `superspace_approach/`
  - 独立于 component-style 理论桶的 superspace 公式体系与后续 supergraph 工作流。

## 设计原则

- “理论”是一级分类，不再把不同理论的记号混到同一文档里。
- component 与 superspace 两套工作方式在目录层面分开，不混放。
- 同一理论下可以有多个文档，但都共享同一个 theory 或 approach 标记。
- 如果后续新增别的理论，优先新建一个新的理论桶，再往里添加具体文档。
