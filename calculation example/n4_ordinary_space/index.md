# N=4 ordinary-space calculation index

当前阶段只做 no-derivative bi-letter \(2\to1\) triangle kernel，并先在 raw off-shell conventions 下提取 seed coefficients，再转换到 normalized kernel。

## Seed pages

1. `01_q1_triangle__xx_to_psi.md`
   - raw seed coefficient \(a_{\rm raw}\) for \(X_iX_j\to \Psi_{\rm raw}^k\), then \(a=-2i\,a_{\rm raw}\)
2. `02_q1_triangle__xpsi_to_f.md`
   - raw seed coefficient \(b_{L,{\rm raw}}\) for \(X_i\Psi_{\rm raw}^j\to F_{\rm raw}\), then \(b_L=-2\sqrt2\,i\,b_{L,{\rm raw}}\)
3. `03_q1_triangle__psix_to_f.md`
   - raw seed coefficient \(b_{R,{\rm raw}}\) for \(\Psi_{\rm raw}^jX_i\to F_{\rm raw}\), then \(b_R=-2\sqrt2\,i\,b_{R,{\rm raw}}\)

## Closure / lift pages

4. `04_q1_triangle__zero_channels_summary.md`
   - all zero channels by quantum numbers
5. `05_q1_triangle__nilpotency_check.md`
   - low-length \((Q_1^{\rm full})^2=0\) checks
6. `06_q1_triangle__lift_to_long_words.md`
   - planar single-trace lift from ordered bi-letters to long words
