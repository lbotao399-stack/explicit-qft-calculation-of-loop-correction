# framework shift log

## 2026-04

### 1. Main shift

project 主计算口径从

- raw \(Q_{\rm bare}-Q_0\) 逐字母代入

切到

- susy current diagram
- anomaly Ward identity
- local-term extraction

### 2. Frozen principles

- `Q_{\rm bare}-Q_0` 的概念定义保留不变；
- 实现上统一通过 `\partial_\mu J^\mu` 插入与局域 Ward 项抽取；
- component current-diagram track 作为 source of truth；
- superspace track 只做 dictionary / bookkeeping；
- coefficient、selection rule、local basis 先固定，再写具体积分；
- naive ordinary triangle 的 `q\to0` 不作为 anomaly 读取方式。

### 3. Current repository policy

- 当前仓库只保留 notation、theory input、workflow definition；
- calculation pages、原始计算归档、枚举渲染脚本与中间结果不再作为当前仓库内容；
- 后续若重建 calculation，必须以现有 theory 与 guidance 文件为入口重新生成。
