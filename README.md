# Explicit QFT Calculation of Loop correction

这个目录把当前已有材料按“理论输入 / 显式计算 / 原始归档”三层整理，尽量只重排，不改写原始推导。

## 目录说明

- `main  working flow and result.md`
  - 工作入口。强调标准工作流、核心对象定义、最重要的几个已得结论。
- `working guidance.md`
  - 工作指导文件。把这套算法流程固定成后续继续扩展时的统一口径。
- `theory/`
  - 按理论分桶放背景输入。当前主桶是 `n1_sym_euclidean/`、`n1_general/`、`n4_sym/`。
- `calculation example/`
  - 放显式 loop 计算。现在先按理论分桶，再在桶内按“一个具体计算一个文件”组织。
- `source_archive/`
  - 保留未拆分的原始总笔记和原图，作为完整归档与对照源。

## 当前拆分方式

### theory

- `theory/index.md`
- `theory/n1_sym_euclidean/`
- `theory/n1_general/`
- `theory/n4_sym/`

### calculation example

- `index.md`
- `n1_sym_euclidean/`
- `n1_general/`
- `n4_sym/`
- `archive/grouped_archive/`（旧的合集稿归档）

## 建议阅读顺序

1. 先看 `working guidance.md`
2. 再看 `main  working flow and result.md`
3. 然后按理论进入 `theory/`
4. 最后通过 `calculation example/index.md` 和对应理论子目录进入具体算例

## 备注

- 原始图像链接已经改成相对 `source_archive/` 的路径，拆分后的算例文件仍可直接对照图。
- 当前材料里同时保留了 DR 与 PV 的计算记录；后续若统一到 DR，可以在现有分类下继续往更高 loop 或别的 SUSY 理论扩展。
